# -*- coding: utf-8 -*-

import os

DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.urandom(24)
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'message_board'
USERNAME = 'root'
PASSWORD = 'lgh1519'
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
# SQLALCHEMY_DATEBASE_URI = "mysql://root:lgh1519:3306/message_board?charset=utf8"