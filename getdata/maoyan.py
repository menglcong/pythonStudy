# -*- coding:utf-8 -*-
import requests
import json
import time
import random
from MongoDB.MongoDB import mongo

#下载第一页数据
def get_one_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    return None

#解析第一页数据
def parse_one_page(html):
    data = json.loads(html)['cmts']
    for item in data:
        yield{
            'comment':item['content'].replace("\n",""),
            'day':item['time'].split(' ')[0],
            'score':item['score'],
            'cityName':item['cityName'],
            'nickname':item['nickName'],
            'time':item['time']
        }

#保存数据到文本文档
def save_data():
    reptile = mongo()
    reptile.connect("mongodb://localhost:27017/","movie","XieBuYaZheng")
    for i in range(1,1001):
        url = 'http://m.maoyan.com/mmdb/comments/movie/248566.json?_v_=yes&offset=' + str(i)
        html = get_one_page(url)
        print('正在保存第%d页。'% i)
        for item in parse_one_page(html):
            reptile.insert_one(item)
            reptile.update(item, { "$set": item}, True)


if __name__ == '__main__':
    save_data()
