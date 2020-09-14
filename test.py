def get_content() -> str:
        """
        collect_info['alert_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        collect_info['alert_env'] = env
        collect_info['alert_status'] = alert.get('status','')
        match_obj = re.match(r'(.+-temp)-(.*)', (title := alert['labels']['alertname']))
        collect_info['alert_title'] = match_obj.group(2) if match_obj is not None else title
        collect_info['alert_detail'] = alert['annotations']['detail']

        生成目标：
        【Tiger报警】younggc-cost
        【告警环境】PROD
        【告警时间】2020-08-13 20:54:13
        【告警状态】恢复
        【告警详情】bp-operation-center-group-846c9bc6c4-cv52z，5分钟内平均单个young gc耗时超0.1s，当前值为0.11099999999999977
        :return:
        """
        content = '【Tiger报警】' '\n'
        content += '【告警环境】'  '\n'
        content += '【告警时间】'  '\n'
        content += '【告警状态】'  '\n'
        content += '【告警详情】'
        return content


print(get_content())
