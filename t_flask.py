# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :t_flask.py
# @Time      :2024/11/13 19:50:35
# @Author    :flower

from flask import Flask, request
import json
app = Flask(__name__)


@app.route('/login', methods=['GET'])
def login():
    # request请求上下文，args从参数中
    username = request.args.get("username")
    password = request.args.get("password")
    request.json
    if username and password:
        data = json.dumps({
            "username": username,
            "password": password,
            "code": 1000,
            "message": "参数成功"
        }, ensure_ascii=False)
    else:
        data = json.dumps({
            "code": 1001,
            "message": "参数未传递"
        }, ensure_ascii=False)
    return data


if __name__ == "__main__":
    app.run()
