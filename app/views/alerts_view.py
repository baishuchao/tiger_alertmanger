#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time: 2020/9/14 3:14 下午
# @Author: John.bai
from flask import request
from flask_restplus import Resource
from app.dto.alerts_dto import AlertsDTO
from app.service.alerts_service import add_alerts

api = AlertsDTO.api


@api.route('')
@api.response(200, 'SUCCESS')
@api.response(400, 'BAD REQUEST')
@api.response(401, 'NOT AUTHORIZED')
@api.response(404, 'NOT FOUND')
class Alerts(Resource):
    def post(self):
        """接口告警信息"""
        data = add_alerts(request.json)
        return data

