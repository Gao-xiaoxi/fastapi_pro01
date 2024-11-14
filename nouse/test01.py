# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test01.py
# @Time      :2024/11/13 12:59:31
# @Author    :flower

import json
import requests

url = 'http://localhost:8337/model/property/listByKeys'
headers = {
    "Host": "localhost:8337",
    "Connection": "keep-alive",
    "Content-Type": "application/json"

}
json_ = {"projectId": "18c1foju-144-1zx", "modelId": "81622159838481472", "keys": ["DiagramTable-scope"]}
response = requests.post(url=url, json=json_)
# print(response.text)

# 数据格式化处理
json_show = json.dumps(response.json(), indent=2, ensure_ascii=False)

if __name__ == "__main__":
    print(json_show)
