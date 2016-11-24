__author__ = 'Mentu'

import numpy as np

def loadDataset(filename):
    '''
    加载数据集
    :param filename:
    :return:
    '''
    numfeat = len(open(filename).readline().split('\t')) - 1 #确定特征值的数量，最后一列为参考标准
    datamat = []
    labelmat = []
    fy = open(filename)
    for line in fy.readlines():
        linearr = []
        curline = line.rstrip().split('\t')
        for i in range(numfeat):
            linearr.append(float(curline[i]))
        datamat.append(linearr)
        labelmat.append(float(curline[-1]))
    return datamat, labelmat

def standRegression(dataset, laberset):
    '''
    线性回归主函数，主要是利用公式w=(XT*X)-1XTy，求线性函数的系数
    其中w表示结果，就是线性函数的系数；X是所有训练集中的数据，y是所有训练集中数据对应的原始预测值
    :param dataset: 原始训练集，类型为：[[],[],[]]
    :param laberset: 原始训练集对应的真实结果， 类型为[]
    :return: 线性函数的系数，类型为：[]
    '''
    datamat = np.mat(dataset)
    labermat = np.mat(laberset).T
    xTx = datamat.T * datamat
    if np.linalg.det(xTx) == 0.0:#计算矩阵的行列式值是不是0，如果是0则该矩阵不是满秩矩阵不能求矩阵的逆
        return
    w = xTx.I * (datamat.T * labermat)
    return w

def lwlr(testdata, dataset, laberset, k=1.0):
    '''
    局部加权线性回归主函数，主要利用了公式w=(XT*W*X)-1XT*Wy和公式W(i,i)=exp(|xi-x|/-2k2)求解线性函数系数
    通过测试数据根据公式W(i,i)求出每个训练集中样本数据的权值，然后根据公式w求回归系数
    :param testdata: 测试数据，是训练集中每一个样本数据就是一个测试数据
    :param dataset: 原始训练集，类型为：[[],[],[]]
    :param laberset: 原始训练集对应的真实结果， 类型为[]
    :param k: 高斯核控制参数，主要控制训练集中有多少数据是对结果产生影响，该参数越小越容易过拟合，越大越容易欠拟合
    :return:
    '''
    datamat = np.mat(dataset)
    labermat = np.mat(laberset).T
    m = np.shape(datamat)[0]
    weight = np.mat(np.eye((m)))
    for i in range(m):
        diffmat = testdata - datamat[i, :]
        weight[i,i] = np.exp(diffmat * diffmat.T / (-2 * k**2))
    xTx = datamat.T * (weight * datamat)
    if np.linalg.det(xTx) == 0.0:
        return
    w = xTx.I * (datamat.T * (weight * labermat)) #求出回归系数
    return testdata * w #算出预测结果

def lwlrTest(testdata, dataset, laberset, k=1.0):
    '''
    局部加权线性回归测试函数
    :param testdata: 测试数据，类型为：[[],[],[]]
    :param dataset: 原始训练集，类型为：[[],[],[]]
    :param laberset: 原始训练集对应的真实结果， 类型为[]
    :param k: 高斯核控制参数，主要控制训练集中有多少数据是对结果产生影响，该参数越小越容易过拟合，越大越容易欠拟合
    :return:
    '''
    m = np.shape(dataset)[0]
    result = np.zeros(m)
    for i in range(m):
        temp = lwlr(testdata[i], dataset, laberset, k)
        result[i] = temp
    return result

def ridgeRegress(dataset, laberset, lam=0.2):
    '''
    岭回归主要函数，计算公式为(XT*X + lam*I)-1XTy
    :param dataset: 原始训练集，类型为：[[],[],[]]
    :param laberset: 原始训练集对应的真实结果， 类型为[]
    :param lam: 控制回归系数结果参数
    :return:
    '''
    m = np.shape(dataset)[1]
    xTx = dataset.T * dataset
    temp = xTx + np.eye(m) * lam
    if np.linalg.det(temp) == 0.0:
        return
    w = temp.I * (dataset.T * laberset)
    return w

def ridgeTest(dataset, laberset):
    '''
    岭回归测试函数，根据不同lam值得出回归函数系数的，选择最好的
    :param dataset: 原始训练集，类型为：[[],[],[]]
    :param laberset: 原始训练集对应的真实结果， 类型为[]
    :return:
    '''
    datamat = np.mat(dataset)
    labermat = np.mat(laberset).T
    labermean = np.mean(labermat, 0)
    labermat = labermat - labermean
    datamean = np.mean(datamat, 0)
    datavar = np.var(datamat, 0)
    datamat = (datamat - datamean) / datavar
    testnumber = 30
    result = np.zeros((testnumber, np.shape(datamat)[1]))
    for i in range(testnumber):
        temp = ridgeRegress(datamat, labermat, np.exp(i-10))
        result[i, :] = temp.T
    return result
