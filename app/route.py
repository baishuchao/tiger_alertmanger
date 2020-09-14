#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time: 2020/9/14 11:31 上午
# @Author: John.bai

from flask import Blueprint
from flask_restplus import Api
from app.config.base_config import app_config
from app.views.user_view import api as user
from app.views.alerts_view import api as alerts

# 创建蓝图
blueprint = Blueprint('api', __name__)
# 创建REST API
api = Api(blueprint, **app_config)

api.add_namespace(user, path='/api/v1/user')
api.add_namespace(alerts, path='/api/v1/alerts')

