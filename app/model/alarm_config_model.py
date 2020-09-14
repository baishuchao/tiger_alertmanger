from app import db
from datetime import datetime


# 告警介质配置
class AlermConfig(db.Model):
    __tablename__ = 'alerm_config'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    environment = db.Column(db.String(128), nullable=True, default=None)   # 环境
    email = db.Column(db.String(128), nullable=True, default=None)  # email
    ding_token = db.Column(db.String(128), nullable=True, default=None)  # email
    ding_secret = db.Column(db.String(128), nullable=True, default=None)  # email
    create_time = db.Column(db.DateTime, default=datetime.now, comment='每条记录创建的当前时间')
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='每条记录更新的当前时间')
