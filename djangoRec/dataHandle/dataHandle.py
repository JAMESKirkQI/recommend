# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/27 11:19
@File ：dataHandle.py
@IDE ：PyCharm
@Author ： KirkQI

"""
from datetime import datetime
from sqlalchemy import create_engine
import pandas as pd

def func(x):
    try:
        return datetime.strptime(str(x), "%Y-%m-%d %H:%M:%S").hour
    except:
        return 0

# URL统计
def fullURL(sql):
    c = [i['fullURL'].value_counts() for i in sql]  # 分块统计各个IP的出现次数
    counts = pd.concat(c).groupby(level=0).sum()  # 合并统计结果，level=0表示按index分组

    counts = counts.reset_index()  # 重新设置index，将原来的index作为counts的一列。
    counts.columns = ['fullURL', 'num']  # 重新设置列名，主要是第二列，默认为0
    counts.sort_values('fullURL', inplace=True, ascending=True)  # 降序排列
    counts=counts[counts["num"]>100]
    print(counts)
    counts.to_sql('fullurl', engine, index=False, if_exists='replace')


# 每日访问时间高峰
def times(sql):
    c = [i['timestamp_format'].value_counts() for i in sql]  # 分块统计各个IP的出现次数
    counts = pd.concat(c).copy()
    # counts.sort_values(inplace=True, ascending=False)  # 降序排列
    counts = counts.reset_index()  # 重新设置index，将原来的index作为counts的一列。
    counts.columns = ['timestamp', 'num']  # 重新设置列名，主要是第二列，默认为0
    counts["timestamp"] = counts["timestamp"].apply(lambda x: func(x))
    print(counts)
    counts = counts.groupby("timestamp")["num"].sum()  # 合并统计结果，level=0表示按index分组
    counts = counts.reset_index()  # 重新设置index，将原来的index作为counts的一列。
    counts.columns = ['timestamp', 'num']  # 重新设置列名，主要是第二列，默认为0
    print(counts)
    counts.to_sql('timestamp', engine, index=False, if_exists='replace')


# 历来时间统计
def ymd(sql):
    c = [i['ymd'].value_counts() for i in sql]  # 分块统计各个IP的出现次数
    counts = pd.concat(c).groupby(level=0).sum()  # 合并统计结果，level=0表示按index分组

    counts = counts.reset_index()  # 重新设置index，将原来的index作为counts的一列。
    counts.columns = ['ymd', 'num']  # 重新设置列名，主要是第二列，默认为0
    counts.sort_values('ymd', inplace=True, ascending=True)  # 降序排列
    print(counts)
    counts.to_sql('ymd', engine, index=False, if_exists='replace')


# 针对来源入口进行分析
def source(sql):
    # 统计点击次数
    c = [i['source'].value_counts() for i in sql]  # 分块统计各个IP的出现次数
    counts = pd.concat(c).groupby(level=0).sum()  # 合并统计结果，level=0表示按index分组
    counts.sort_values(inplace=True, ascending=False)  # 降序排列
    counts = counts.reset_index()  # 重新设置index，将原来的index作为counts的一列。
    counts.columns = ['source', 'num']  # 重新设置列名，主要是第二列，默认为0
    counts = counts[counts['num'] > 500]  # 重新设置列名，主要是第二列，默认为0

    print(counts)
    counts.to_sql('source', engine, index=False, if_exists='replace')


# 地区统计
def userOS(sql):
    # 统计点击次数
    c = [i['userOS'].value_counts() for i in sql]  # 分块统计各个IP的出现次数
    counts = pd.concat(c).groupby(level=0).sum()  # 合并统计结果，level=0表示按index分组
    counts.sort_values(inplace=True, ascending=False)  # 降序排列
    counts = counts.reset_index()  # 重新设置index，将原来的index作为counts的一列。
    counts.columns = ['userOS', 'num']  # 重新设置列名，主要是第二列，默认为0
    counts = counts[counts['num'] > 500]  # 重新设置列名，主要是第二列，默认为0

    print(counts)
    counts.to_sql('userOS', engine, index=False, if_exists='replace')


# 地区统计
def userAgent(sql):
    # 统计点击次数
    c = [i['userAgent'].value_counts() for i in sql]  # 分块统计各个IP的出现次数
    counts = pd.concat(c).groupby(level=0).sum()  # 合并统计结果，level=0表示按index分组
    counts.sort_values(inplace=True, ascending=False)  # 降序排列
    counts = counts.reset_index()  # 重新设置index，将原来的index作为counts的一列。
    counts.columns = ['userAgent', 'num']  # 重新设置列名，主要是第二列，默认为0
    counts = counts[counts['num'] > 100]
    print(counts)
    counts.to_sql('useragent', engine, index=False, if_exists='replace')


# 地区统计
def areaCode(sql):
    # 统计点击次数
    c = [i['realAreacode'].value_counts() for i in sql]  # 分块统计各个IP的出现次数
    counts = pd.concat(c).groupby(level=0).sum()  # 合并统计结果，level=0表示按index分组
    counts.sort_values(inplace=True, ascending=False)  # 降序排列
    counts = counts.reset_index()  # 重新设置index，将原来的index作为counts的一列。
    counts.columns = ['area', 'num']  # 重新设置列名，主要是第二列，默认为0
    counts = counts[counts['num'] > 500]
    print(counts)
    counts.to_sql('areacode', engine, index=False, if_exists='replace')


# 用户点击一次浏览网站统计
def ones_web(sql,df):
    # 统计点击次数
    c = [i['realIP'].value_counts() for i in sql]  # 分块统计各个IP的出现次数
    counts = pd.concat(c).groupby(level=0).sum()  # 合并统计结果，level=0表示按index分组
    counts = pd.DataFrame(counts)
    counts = counts.reset_index()
    counts.columns = ['realIP', 'num']

    counts = counts[counts["num"] == 1].drop_duplicates(keep="first")
    message=pd.merge(counts["realIP"],df[["realIP","fullURL"]]).copy()
    print(message)
    message['num'] = 1
    message=message.groupby("fullURL")["num"].sum().reset_index()
    message.columns = ['fullURL', 'num']
    message.sort_values("num",inplace=True, ascending=False)
    message=message[message["num"]>100]
    print(message)
    counts.to_sql('ones_web', engine, index=False, if_exists='replace')


# 真实次数统计
def realIP(sql):
    # 统计点击次数
    c = [i['realIP'].value_counts() for i in sql]  # 分块统计各个IP的出现次数
    counts = pd.concat(c).groupby(level=0).sum()  # 合并统计结果，level=0表示按index分组
    counts = pd.DataFrame(counts)
    counts['num'] = 1
    counts = counts.groupby('realIP')['num'].sum().reset_index()
    counts.columns = ["count", "num"]
    counts["count"][counts["count"] > 7] = "7次以上"
    counts = counts.groupby("count")["num"].sum().reset_index()
    counts.columns = ["count", "num"]
    print(counts)
    counts.to_sql('realip', engine, index=False, if_exists='replace')


# 标题类型关键字
def PageTitleKw(sql):
    counts = [i['pageTitleKw'].value_counts() for i in sql]  # 逐块统计
    counts = pd.concat(counts).groupby(level=0).sum()  # 合并统计结果，把相同的统计项合并（即按index分组并求和）
    counts = counts.reset_index()  # 重新设置index，将原来的index作为counts的一列。
    counts.columns = ['page', 'num']  # 重新设置列名，主要是第二列，默认为0
    counts = counts[counts["page"] != "-1"]
    counts.sort_values('num', inplace=True, ascending=False)  # 降序排列
    counts = counts.reset_index(drop=True)  # 重新设置index
    counts = counts[counts['num'] > 500]
    print(counts)
    counts.to_sql('pagetitlekw', engine, index=False, if_exists='replace')


# 标题类型名称
def pageTitleCategoryName(sql):
    counts = [i['pageTitleCategoryName'].value_counts() for i in sql]  # 逐块统计
    counts = pd.concat(counts).groupby(level=0).sum()  # 合并统计结果，把相同的统计项合并（即按index分组并求和）
    counts = counts.reset_index()  # 重新设置index，将原来的index作为counts的一列。
    counts.columns = ['page', 'num']  # 重新设置列名，主要是第二列，默认为0
    counts.sort_values('num', inplace=True, ascending=False)  # 降序排列
    counts = counts.reset_index(drop=True)  # 重新设置index
    print(counts)
    counts.to_sql('pagetitlecategoryname', engine, index=False, if_exists='replace')


# 统计瞎逛人员
def web_xiaguang_count(df):
    counts = df

    counts = counts[["fullURL", "fullURLId"]][counts["fullURL"].str.contains(".html") == False].copy()
    counts["num"] = 1
    counts = counts.groupby("fullURLId")["num"].sum()  # 合并统计结果，把相同的统计项合并（即按index分组并求和）
    counts = counts.reset_index()  # 重新设置index，将原来的index作为counts的一列。
    counts.columns = ['index', 'num']  # 重新设置列名，主要是第二列，默认为0
    print(counts)
    counts.sort_values(by="num", replace=True, ascending=False)
    print(counts)
    counts.to_sql('web_xiaguang_count', engine, index=False, if_exists='replace')


# 统计网页类型
def web_info_count(sql):
    counts = [i['fullURLId'].value_counts() for i in sql]  # 逐块统计
    counts = pd.concat(counts).groupby(level=0).sum()  # 合并统计结果，把相同的统计项合并（即按index分组并求和）
    counts = counts.reset_index()  # 重新设置index，将原来的index作为counts的一列。
    counts.columns = ['index', 'num']  # 重新设置列名，主要是第二列，默认为0
    counts['type'] = counts['index'].str.extract('(\d{3})', expand=True)  # 提取前三个数字作为类别id
    counts_ = counts[['type', 'num']].groupby('type').sum()  # 按类别合并
    counts_.sort_values('num', ascending=False)  # 降序排列
    counts_ = counts_.reset_index()  # 重新设置index，将原来的index作为counts的一列。
    counts_.columns = ['index', 'num']  # 重新设置列名，主要是第二列，默认为0
    print(counts_)
    counts_.to_sql('web_info_count', engine, index=False, if_exists='replace')


def count101web(sql):
    counts = [i['fullURLId'].value_counts() for i in sql]  # 逐块统计
    counts = pd.concat(counts).groupby(level=0).sum()  # 合并统计结果，把相同的统计项合并（即按index分组并求和）
    counts = counts.reset_index()  # 重新设置index，将原来的index作为counts的一列。
    counts.columns = ['index', 'num']  # 重新设置列名，主要是第二列，默认为0
    counts = counts[counts["index"].str.contains("10100")]
    counts["type"] = "其他"
    counts["type"][counts["index"].str.contains("101001")] = u'知识首页'
    counts["type"][counts["index"].str.contains("101002")] = u'知识列表页'
    counts["type"][counts["index"].str.contains("101003")] = u'知识内容页'
    counts = counts[["type", "num"]]
    counts = counts.groupby("type")["num"].sum().reset_index()
    counts.columns = ['type', 'num']
    counts.sort_values('num', ascending=False)  # 降序排列
    print(counts)
    counts.to_sql('count101web', engine, index=False, if_exists='replace')


# 统计107类别的情况
def count107(i):  # 自定义统计函数
    j = i[['fullURL']][i['fullURLId'].str.contains('107')].copy()  # 找出类别包含107的网址
    j['type'] = None  # 添加空列
    j['type'][j['fullURL'].str.contains('info/.+?/')] = u'知识首页'
    j['type'][j['fullURL'].str.contains('info/.+?/.+?')] = u'知识列表页'
    j['type'][j['fullURL'].str.contains('/\d+?_*\d+?\.html')] = u'知识内容页'
    return j['type'].value_counts()


if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3307/recommend?charset=utf8')
    sql = pd.read_sql('all_gzdata', engine, chunksize=10000)
    df = pd.read_sql('all_gzdata', engine)
    '''
    
    用create_engine建立连接，连接地址的意思依次为“数据库格式（mysql）+程序名（pymysql）+账号密码@地址端口/数据库名（test）”，最后指定编码为utf8；
    all_gzdata是表名，engine是连接数据的引擎，chunksize指定每次读取1万条记录。这时候sql是一个容器，未真正读取数据。
    '''

    # count107web(sql)
    # print("count107web======done")
    # count101web(sql)
    # print("count101web======done")
    # web_xiaguang_count(df)
    # print("web_xiaguang_count======done")
    # web_info_count(sql)
    # print("web_info_count======done")
    # pageTitleCategoryName(sql)
    # print("pageTitleCategoryName======done")
    # PageTitleKw(sql)
    # print("PageTitleKw======done")
    # realIP(sql)
    # print("realIP======done")
    # ones_web(sql,df)
    # print("ones_web======done")
    # areaCode(sql)
    # print("areaCode======done")
    # userAgent(sql)
    # print("userAgent======done")
    # userOS(sql)
    # print("userOS======done")
    # ymd(sql)
    # print("ymd======done")
    # source(sql)
    # print("source======done")
    # times(sql)
    # print("times======done")
    # fullURL(sql)
    # print("fullURL======done")