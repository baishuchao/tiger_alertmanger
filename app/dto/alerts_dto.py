#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time: 2020/9/14 3:19 下午
# @Author: John.bai

from flask_restplus import Namespace, fields


class AlertsDTO(object):
    api = Namespace('告警信息', description='告警信息处理相关')
