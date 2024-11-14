# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :t_flask_2.py
# @Time      :2024/11/14 19:26:17
# @Author    :flower
import json

from flask import Flask, request

app = Flask(__name__)


# get请求
@app.route('/get_req_url', methods=['GET'])
def get_req_url():
    par_1 = request.args.get('par_1')
    par_2 = request.args.get('par_2')
    if par_1 and par_2:
        data = json.dumps({
            'code': 200,
            'message': "请求成功",
            'par_1': par_1,
            'par_2': par_2
        }, ensure_ascii=False)
    elif not par_1 and par_2:
        data = json.dumps({
            'code': 201,
            'message': "请求失败，参数缺失",
        }, ensure_ascii=False)
    elif par_1 and not par_2:
        data = json.dumps({
            'code': 202,
            'message': "请求失败，参数缺失",
        }, ensure_ascii=False)
    else:
        data = json.dumps({
            'code': 203,
            'message': "请求失败，参数缺失",
        }, ensure_ascii=False)
    return data


# post请求
@app.route('/post_req_json', methods=['POST'])
def post_req_json():
    method_ = request.method
    if method_ == 'POST':
        par_1 = request.json['par_1']
        par_2 = request.json['par_2']
        if par_1 and par_2:
            data = json.dumps({
                'code': 200,
                'message': "请求成功",
                'par_1': par_1,
                'par_2': par_2
            }, ensure_ascii=False)
        else:
            data = json.dumps({
                'code': 201,
                'message': "请求体数据不正确",
            }, ensure_ascii=False)
    else:
        data = json.dumps({
            'code': 201,
            'message': '请求方法不合法'
        }, ensure_ascii=False)
    return data


if __name__ == "__main__":
    app.run()
