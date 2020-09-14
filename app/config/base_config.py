#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time: 2020/9/14 11:33 上午
# @Author: John.bai

import pymysql
app_config = {
    'title': 'Tiger AlertManager',
    'version': '1.0',
    'description': 'Tiger Alertmanger 的RESTful API服务'

}


class Config(object):
    SECRET_KEY = '5e8bca1c9aaa34aed6d069be3dfccd31'
    # 连接mysql数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = False   # 关闭警告信息
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    DEBUG_LOG = True