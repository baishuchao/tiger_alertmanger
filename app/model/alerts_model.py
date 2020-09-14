#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time: 2020/9/14 3:52 下午
# @Author: John.bai
from app import db
from datetime import datetime


# prometheus 告警信息
class Alerts(db.Model):
    __tablename__ = 'alerts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=True, default=None)   # alert name
    status = db.Column(db.Integer, nullable=True, default=None)  # 状态0未发送，状态1已发送
    environment = db.Column(db.String(128), nullable=True, default=None)   # 环境
    detail = db.Column(db.String(255), nullable=True, default=None)   # 详情
    alarm_time = db.Column(db.String(128), nullable=True, default=None)  # 告警时间
    recovery_time = db.Column(db.String(128), nullable=True, default=None)  # 恢复时间
    create_time = db.Column(db.DateTime, default=datetime.now, comment='每条记录创建的当前时间')
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='每条记录更新的当前时间')



