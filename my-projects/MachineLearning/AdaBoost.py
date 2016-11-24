__author__ = 'Mentu'

import numpy as np
from math import log

def loadDataset():
    datamat = np.matrix([[1.,2.1],[2.,1.1],[1.3,1.],[1.,1.],[2.,1.]])
    classlabel = [1.0,1.0,-1.0,-1.0,1.0]
    D = np.mat(np.ones((5, 1))/5)
    return datamat, classlabel, D

def stumpClassify(datamat, dimen, threshval, threshineq):
    '''
    将数据集中的原始数据分类，所有原始小于threshval的都赋值为-1且threshineq的状态为'lt'，反正也是这样
    :param datamat: 需要分类的数据集
    :param dimen: 数据集中的那一列需要被分类
    :param threshval: 分类阀值
    :param threshineq: 分类的状态表示是大于还是小于
    :return:
    '''
    retarray = np.ones((np.shape(datamat)[0], 1))
    if threshineq == 'lt':
        retarray[datamat[:, dimen] <= threshval] = -1.0#numpy数组或矩阵可以直接在下标中写条件选出符合条件的元素
    else:
        retarray[datamat[:, dimen] > threshval] = -1.0
    return retarray

def buildStump(dataset, classlabel, D):
    '''
    该方法主要是找出分类错误率最小的列向量，并且保存满足错误率最小的列向量时对应的条件，包括列向量索引，选取的阀值，比较的情况，最小错误率，以及对应的分类结果
    :param dataset: 原始数据集，类型为：[[],[],[]]
    :param classlabel: 原始数据集的类标号，类型为：[]
    :param D: 训练集每行样本的权重
    :return: 列向量索引，选取的阀值，比较的情况，最小错误率，以及对应的分类结果
    '''
    datamat = np.mat(dataset)
    labelmat = np.mat(classlabel).T#等价于np.mat(classlabel).Transpose
    m, n = np.shape(datamat)
    numstep = 10.0#步长增长速率，这里是按0.1增长，也就是说，1~2就要增长10次
    beststump = {}
    bestclassest = np.mat(np.zeros((m, 1)))
    minerror = np.inf
    for i in range(n):#针对每一列数据
        rangeMin = datamat[:, i].min()#该列数据的最小值
        rangeMax = datamat[:, i].max()#该列数据的最大值
        stepSize = (rangeMax - rangeMin)/numstep#步长增长速率，这里是按0.1增长，也就是说，1~2就要增长10次
        for j in range(-1, int(numstep) + 1):
            for inequal in ['lt', 'gt']:
                threshval = (rangeMin + float(j) * stepSize)#计算分类阀值，就是从训练数据集中最小的值按照步长增长率依次递增直到最大值
                predictedvals = stumpClassify(datamat, i, threshval, inequal)#每次将列向量针对阀值进行分类
                errarr = np.mat(np.ones((m, 1)))
                errarr[predictedvals == labelmat] = 0#将分类错误的设置为1
                weightedError = D.T * errarr#计算该阀值以及该列向量在该阀值分类的错误率大小，选择分类错误率最小的，而这个错误率是依靠训练数据集的权值来计算的
                if weightedError < minerror:
                    minerror = weightedError
                    bestclassest = predictedvals.copy()
                    beststump['dim'] = i
                    beststump['thresh'] = threshval
                    beststump['ineq'] = inequal
    return beststump, minerror, bestclassest

def adaBoostTrainDB(dataset, classlabel, maxloop=40):
    '''
    AdaBoost算法主函数，其基本思想为：通过弱分类器对原始数据集进行分类，求出分类的错误率，错误率是根据训练集样本的权重与真实错误率相乘所得
    然后利用公式1/2*ln(1-error/error)求出alpha的值，其次更新训练集样本权重的值，D=D*e-alpha/D.sum，并判断该次分类的正确率，
    如果正确率为0则退出计算，否则要等最大循环次数结束后才退出运算
    :param dataset: 原始数据集，类型为：[[],[],[]]
    :param classlabel: 原始数据集的类标号，类型为：[]
    :param maxloop: 最大循环次数
    :return: 列向量索引，选取的阀值，比较的情况，alpha的值
    '''
    weakClassArr = []
    m = np.shape(dataset)[0]
    D = np.mat(np.ones((m,1))/m)#原始数据集每个样本的权重
    aggclassest = np.mat(np.zeros((m,1)))#保存最佳分类结果
    for i in range(maxloop):
        beststump, error, classest = buildStump(dataset, classlabel, D)
        alpha = float(0.5 * log((1- error)/max(error, 1e-16)))
        beststump['alpha'] = alpha
        weakClassArr.append(beststump)
        expon = np.multiply(-1 * alpha * np.mat(classlabel).T, classest)#两个矩阵相乘,如果不符合矩阵乘法，那就对应位置相乘
        D = np.multiply(D, np.exp(expon))#更新权值的计算方法
        D = D/D.sum()
        aggclassest += alpha * classest#累计每个训练样本的分类结果权重？
        aggErrors = np.multiply(np.sign(aggclassest) != np.mat(classlabel).T, np.ones((m,1)))
        errorrate = aggErrors.sum()/m#计算错误率的方法
        if errorrate == 0.0:
            break
    return weakClassArr

def adaClassifyUT(datatoclass, classifierarr):
    datamat = np.mat(datatoclass)
    m = np.shape(datamat)[0]
    aggclassest = np.mat(np.zeros((m,1)))
    for i in range(len(classifierarr)):
        classest = stumpClassify(datamat, classifierarr[i]['dim'], classifierarr[i]['thresh'], classifierarr[i]['ineq'])
        aggclassest += classifierarr[i]['alpha'] * classest
    return np.sign(aggclassest)#求分类结果？
