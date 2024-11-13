# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :t_flask.py
# @Time      :2024/11/13 19:50:35
# @Author    :flower

from flask import Flask
import json
app = Flask(__name__)


@app.route('/login')
def login():
    data = json.dumps({
        "username": "gao",
        "password": "123456"
    }, indent=2)
    return data


if __name__ == "__main__":
    app.run()
