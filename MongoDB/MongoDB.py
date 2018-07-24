# -*- coding:utf-8 -*-
import pymongo

class mongo:
    def __int__(self):
        pass

    def connect(self, mongo_url, databse, table_name):
        self.client = pymongo.MongoClient(mongo_url)
        self.database = self.client[databse]
        self.table_cliet = self.database[table_name]


    #查询
    def find(self, *args):
        return self.table_cliet.find(*args)

    #插入一条
    def insert_one(self, data):
        self.table_cliet.insert_one(data)

    #插入多条
    def insert_many(self, data):
        self.table_cliet.insert_many(data)

    #更新
    def update(self):
        self.table_cliet.update_many()

    #删除
    def delete(self, *args):
        self.table_cliet.delete_many(*args)


    #删除集合
    def drop(self):
        self.table_cliet.drop()

if __name__ == "__main__":
    test = mongo()
    test.connect("mongodb://localhost:27017/","car","tianjin")
    myquery = { "city_name": "tianjin" }
    data = test.find(myquery)
    for x in data:
        print(x)