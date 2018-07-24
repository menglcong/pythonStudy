# -*- coding:utf-8 -*-
from MongoDB.MongoDB import mongo
from pyecharts import Pie
reptile = mongo()
reptile.connect("mongodb://localhost:27017/","movie","XieBuYaZheng")

score = []
for item in reptile.find():
    score.append(item['score'])

#饼状图
attr = ["五星", "四星", "三星", "二星", "一星"]

#分别代表各星级评论数
v1 = [score.count(5)+score.count(4.5),
      score.count(4)+score.count(3.5),
      score.count(3)+score.count(2.5),
      score.count(2)+score.count(1.5),
      score.count(1)+score.count(0.5)]

pie = Pie("饼图-邪不压正猫眼评分", title_pos='center', width=900)
pie.add("邪不压正猫眼评分", attr, v1, center=[50, 50],
        radius=[30, 75], rosetype='area',
        is_legend_show=False, is_label_show=True)

pie.render(path='pie.html')