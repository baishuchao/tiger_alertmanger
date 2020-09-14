#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time: 2020/9/14 11:37 上午
# @Author: John.bai
from flask import jsonify
from datetime import datetime, timedelta


# 继承自dict，实现可以通过.来操作元素
class AttrDict(dict):
    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __getattr__(self, item):
        return self.__getitem__(item)

    def __delattr__(self, item):
        self.__delitem__(item)


def json_response(status='', data='', msg='', error=''):
    content = AttrDict(status=status, msg=msg, data=data, error=error)
    if error:
        content.data = ''
    return jsonify(content)



def human_tz_time(value):
    """
    2020-06-01T03:06Z UTC转北京时间2019-07-26 16:20:54
    :param value:
    :return:
    """
    utc_date = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    local_date = utc_date + timedelta(hours=8)
    local_date_str = datetime.strftime(local_date, '%Y-%m-%d %H:%M:%S')
    return local_date_str


def human_format_time(value):
    """
    2020-08-04T19:15:05.14243857+08:00 转为2020-08-05 03:15:05
    :param value:
    :return:
    """
    replace_str = str('.' + value.split('.')[-1])
    tz_time = value.replace(replace_str, 'Z')
    local_date_str = human_tz_time(tz_time)
    return local_date_str




