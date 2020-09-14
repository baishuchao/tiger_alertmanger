import requests
import time
import hashlib
import hmac
import base64
import re

def SendMessage(message = ''):

    # secret：密钥，机器人安全设置页面，加签一栏下面显示的SEC开头的字符串，例如：SECxxxxxxxx
    secret = 'SECfff73eb101bcf0195345471bfee35b04af527cc209dfa09820351eb427c9e1a4'
    # access_token：创建完钉钉机器人之后会自动生成，例如：access_tokenxxxx
    access_token = 'fef21b0e24ba7f8563dc7bb47f8c9a9a71007849a7065148822a1a81d33b121e'
    # timestamp：当前时间戳，单位是毫秒，与请求调用时间误差不能超过1小时
    timestamp = int(round(time.time() * 1000))

    # 加密，获取sign和timestamp
    data = (str(timestamp) + '\n' + secret).encode('utf-8')
    secret = secret.encode('utf-8')
    signature = base64.b64encode(hmac.new(secret, data, digestmod=hashlib.sha256).digest())
    reg = re.compile(r"'(.*)'")
    signature = str(re.findall(reg,str(signature))[0])

    # 发送信息
    url = 'https://oapi.dingtalk.com/robot/send?access_token=%s&sign=%s&timestamp=%s' % (access_token,signature,timestamp)
    headers = {"Content-Type": "application/json ;charset=utf-8 "}
    try:
        response = requests.post(url, headers = headers, json = message, timeout = (3,60))
        print(response)
        response_msg = str(response.status_code) + ' ' + str(response.content)
        print(response_msg)
    except Exception as error_msg:
        print('error_msg==='+str(error_msg))
        response_msg = error_msg

    return response_msg

if __name__ == "__main__":
    content = {"告警信息": 'test1',"环境": "生产"}
    msg = {"msgtype": "text", "text": {"content":content}, "at":{"isAtAll":False}}
    SendMessage(msg)


