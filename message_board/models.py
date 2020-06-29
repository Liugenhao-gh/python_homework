# -*- coding: utf-8 -*-

from  exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
# 用户模型
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Email = db.Column(db.String(30),nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    # 密码加密
    def __init__(self,*args, **kwargs):
        Email = kwargs.get('Email')
        username = kwargs.get('username')
        password = kwargs.get('password')
        self.Email = Email
        self.username = username
        self.password = generate_password_hash(password)

    # 检查密码是否相同
    def check_password(self,raw_password):
        result = check_password_hash(self.password, raw_password)
        return  result
# 留言模型
class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String(150), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', backref=db.backref('message'))