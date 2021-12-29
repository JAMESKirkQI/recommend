# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/27 15:59
@File ：datPreprocessing.py
@IDE ：PyCharm
@Author ： KirkQI

"""
import pandas as pd
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3307/recommend?charset=utf8')
    sql = pd.read_sql('all_gzdata', engine, chunksize=10000)
    for i in sql:
        d = i[i['fullURL'].str.contains('\.html')].copy()  # 只要含有.html的网址
        d = d[d['pageTitleKw'] != "-1"]
        d['userAgent'] = d['userAgent'].str.strip()
        # d['fullURL'] = d['fullURL'].str.replace('_\d{0,2}.html', '.html')  # 将下划线后面部分去掉，规范为标准网址
        # d = d.drop_duplicates()  # 删除重复记录
        d['type_1'] = d['fullURL']  # 复制一列
        d['type_1'][d['fullURL'].str.contains('(ask)|(askzt)')] = 'ask'
        # 保存到数据库的cleaned_gzdata表中（如果表不存在则自动创建）
        print(d.info())
        d.to_sql('cleaned_data', engine, index=False, if_exists='append')
