#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time: 2020/9/14 3:33 下午
# @Author: John.bai
from app.util.common import human_format_time,json_response
from app import db
from app.model.alerts_model import Alerts


def add_alerts(data):
    for i in data:
        data = {"name": i['labels']['alertname'],
                "detail": i['annotations']['detail'],
                "alarm_time": human_format_time(i['startsAt']),
                "environment": i['labels']['task'],
                "alarm_status": "告警"}
        print(i)
        # db.session.add(db_data)
        # db.session.commit()


    data = Alerts.query.filter_by(id=1).all()
    print(data)

    return json_response(status=0, msg="添加成功")

