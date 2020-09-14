import requests
import time
import hashlib
import hmac
import base64
import re


class AlertTail:
    def __init__(self, access_token, secret, send_mgs):
        self.access_token = access_token
        self.secret = secret
        self.send_mgs = send_mgs
        self.message = self.get_content(send_mgs)
        self.send_mgs = send_mgs
    def get_alert_ding(self):
        """
        获取钉钉发送地址
        :return:
        """
        pass

    def get_alert_email(self):
        """
        获取邮件接受地址
        :return:
        """
        pass

    def send_dingtalk(self):
        """
        发送DingDing机器人
        :return:
        """
        timestamp = int(round(time.time() * 1000))
        # 加密，获取sign和timestamp
        data = (str(timestamp) + '\n' + self.secret).encode('utf-8')
        secret = self.secret.encode('utf-8')
        signature = base64.b64encode(hmac.new(secret, data, digestmod=hashlib.sha256).digest())
        reg = re.compile(r"'(.*)'")
        signature = str(re.findall(reg, str(signature))[0])

        # 发送信息
        url = 'https://oapi.dingtalk.com/robot/send?access_token=%s&sign=%s&timestamp=%s' % (
        self.access_token, signature, timestamp)
        headers = {"Content-Type": "application/json ;charset=utf-8 "}
        try:
            response = requests.post(url, headers=headers, json=self.message, timeout=(3, 60))
            print(response)
            response_msg = str(response.status_code) + ' ' + str(response.content)
            print(response_msg)
        except Exception as error_msg:
            print('error_msg===' + str(error_msg))
            response_msg = error_msg

        return response_msg

    def get_content(self, send_mgs):
        content = '【Tiger报警】' + self.send_mgs['name'] + '\n'
        content += '【告警环境】' + self.send_mgs['environment'] + '\n'
        content += '【告警时间】' + self.send_mgs['alarm_time'] + '\n'
        content += '【告警状态】' + self.send_mgs['alarm_status'] + '\n'
        content += '【告警详情】' + self.send_mgs['detail']
        print(send_mgs)

        msg = {"msgtype": "text", "text": {"content": content}, "at": {"isAtAll": False}}
        return msg


if __name__ == '__main__':
    data = {"name": "kubernetes-temp-wulu-pod-memory",
            "detail": "mp-transit-notification-service-85c44dc776-tdvpt: 内存已使用过高于2G (当前值: 2477)",
            "alarm_time": '2020-08-01 01:51:05', "environment": "wulu-prod", "alarm_status": "告警"}
    data = AlertTail(access_token='fef21b0e24ba7f8563dc7bb47f8c9a9a71007849a7065148822a1a81d33b121e',
                     secret='SECfff73eb101bcf0195345471bfee35b04af527cc209dfa09820351eb427c9e1a4',
                     send_mgs=data)
    print(data.send_dingtalk())

