# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/29 12:53
@File ：recommend.py
@IDE ：PyCharm
@Author ： KirkQI

"""
import numpy as np


def Jaccard(a, b):  #欧氏距离
    return 1.0 * (a * b).sum() / (a + b - a * b).sum()


class Recommender():
    sim = None  # 初始化

    def similarity(self, x, distance):  # 计算矩阵相关
        y = np.ones((len(x), len(x)))
        for i in range(len(x)):
            for j in range(len(x)):
                y[i, j] = distance(x[i], x[j])
        return y

    def fit(self, x, distance=Jaccard):  # 距离计算
        self.sim = self.similarity(x, distance)

    def recommend(self, a):  # 推荐矩阵协同算法
        return np.dot(self.sim, a) * (1 - a)
