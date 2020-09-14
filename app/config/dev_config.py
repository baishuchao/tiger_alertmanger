#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time: 2020/9/14 11:34 上午
# @Author: John.bai

from app.config.base_config import Config


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ops:Admin@1234@10.0.10.193:3306/alertmanger?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
