__author__ = 'Mentu'

import numpy as np
import random

def loadDataset():
    datamat = []
    labelmat = []
    fr = open(r'dataset/testSet.txt')
    for line in fr.readlines():
        linecontent = line.rstrip().split()
        datamat.append([1, float(linecontent[0]), float(linecontent[1])])
        labelmat.append(int(linecontent[2]))
    return datamat, labelmat

def sigmoid(inx):
    '''
    sigmoid函数，sigmoid = 1/1+exp(-z)
    :param inx:
    :return:
    '''
    return 1.0/(1+np.exp(-inx))

def gradAsent(dataset, labelset):
    '''
    梯度上升求回归函数系数的主函数，其过程为初始化一个回归函数的系数，然后把训练集中的数据带入该系数构成的回归函数，求出其值，
    并带入Sigmoid函数求出分类结果，然后用训练集中的分类标号减去求出的标号的误差作为梯度上升迭代求系数步骤的方向，最后用公式
    w:=w+a*f'(x)*error，a为递增步长，f'(x)是分别对回归函数的不同变量求偏导，error是w移动方向迭代回归函数的系数。
    梯度上升求回归函数系数的方法中，每一次迭代都必须把所有的训练集中的数据迭代一次，算法相当耗时
    :param dataset: 原始数据集，类型为：[[],[],[]]
    :param labelset: 原始数据集的类标号，类型为：[]
    :return: 回归函数的系数，类型为：[]
    '''
    datamat = np.mat(dataset)
    labelmat = np.mat(labelset).transpose()#矩阵转置
    m, n = np.shape(datamat)
    alpha = 0.001#梯度递增系数
    maxloop = 500
    weight = np.ones((n,1))#回归函数的系数初始化为1
    for k in range(maxloop):#开始迭代求回归函数系数
        h = sigmoid(datamat*weight)#求训练集中所有数据的分类结果
        error = labelmat - h#求分类误差，确定梯度上升的方向
        weight = weight + alpha * datamat.transpose() * error#更新回归函数的系数
    return weight

def stocGradAscent(dataset, labelset):
    '''
    随机梯度上升求回归函数系数的主函数，其求值过程与梯度上升求回归函数系数的方法一致，只不过每次迭代的时候只需要求
    训练集中的一行数据，而且不需要矩阵转置等操作，速度提升好高。该函数中实际上没有随机遍历训练集中的数据，在下个函数中进行改进
    :param dataset: 原始数据集，类型为：[[],[],[]]
    :param labelset: 原始数据集的类标号，类型为：[]
    :return: 回归函数的系数，类型为：[]
    '''
    m, n = np.shape(dataset)
    datamat = np.array(dataset)
    alpha = 0.01
    weight = np.ones(n)
    for i in range(m):
        h = sigmoid(sum(datamat[i]*weight))
        error = labelset[i] - h
        weight = weight + alpha * error * datamat[i]
    return weight

def improveStocGradAscent(dataset, labelset, maxloop=150):
    '''
    随机梯度上升求回归函数系数主函数，改进版，真正的随机选取训练集中的数据进行更新，并且减小收敛周期的波动
    :param dataset: 原始数据集，类型为：[[],[],[]]
    :param labelset: 原始数据集的类标号，类型为：[]
    :param maxloop: 最大的循环次数
    :return: 回归函数的系数，类型为：[]
    '''
    m, n = np.shape(dataset)
    datamat = np.array(dataset)
    weight = np.ones(n)
    for i in range(maxloop):
        randindex = list(range(m))#获得随机的下标
        for j in range(m):
            alpha = 4/(1.0+i+j)+0.01 #这个有点不懂其原理
            rand = int(random.uniform(0, len(randindex))) #获得计算训练集中随机一行的下标
            h = sigmoid(sum(datamat[rand]*weight))
            error = labelset[rand] - h
            weight = weight + alpha * error * datamat[rand]
            del randindex[rand]
    return weight
