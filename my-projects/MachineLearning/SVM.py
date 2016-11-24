__author__ = 'Mentu'

import numpy as np
from random import uniform

def loadDataset(filename):
    datamat = []
    labelmat = []
    fr = open(filename)
    for line in fr.readlines():
        linearr = line.rstrip().split('\t')
        datamat.append([float(linearr[0]), float(linearr[1])])
        labelmat.append(float(linearr[2]))
    return datamat, labelmat

def selectJrand(i, m):
    j = i
    while j==i:
        j = int(uniform(0, m))
    return j

def clipAlpha(aj, H, L):
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj

def smoSimple(dataset, classlabel, C, toler, maxloop):
    '''
    暂时没搞懂
    :param dataset:
    :param classlabel:
    :param C:
    :param toler:
    :param maxloop:
    :return:
    '''
    datamat = np.mat(dataset)
    labelmat = np.mat(classlabel).T
    b = 0
    m, n = np.shape(datamat)
    alpha = np.mat(np.zeros((m,1)))
    iterer = 0
    while iterer < maxloop:
        alphaPairsChanged = 0
        for i in range(m):
            fXi = float(np.multiply(alpha, labelmat).T * (datamat * datamat[i, :].T)) + b#将每行训练集的数据集进行分类
            Ei = fXi - float(labelmat[i])#判断分类的误差
            if ((labelmat[i]*Ei < -toler) and (alpha[i] < C)) or ((labelmat[i]*Ei > toler) and (alpha[i] > 0)):#判断alpha和分类结果是否满足特定条件
                j = selectJrand(i, m)#随机选择另行数据进行分类
                fXj = float(np.multiply(alpha, labelmat).T * (datamat*datamat[j, :].T)) + b
                Ej = fXj - float(labelmat[j])
                alphaIold = alpha[i].copy()
                alphaJold = alpha[j].copy()
                if labelmat[i] != labelmat[j]:
                    L = max(0, alpha[j]-alpha[i])
                    H = min(C, C + alpha[j] - alpha[i])
                else:
                    L = max(0, alpha[j] + alpha[i] - C)
                    H = min(C, alpha[j] + alpha[i])
                if L == H:
                    continue
                eta = 2.0 * datamat[i, :] * datamat[j, :].T - datamat[i, :] * datamat[i, :].T - datamat[j, :] * datamat[j, :].T
                if eta >= 0:
                    continue
                alpha[j] -= labelmat[j]*(Ei - Ej)/eta
                alpha[j] = clipAlpha(alpha[j], H, L)
                if abs(alpha[j] - alphaJold < 0.00001):
                    continue
                alpha[i] += labelmat[j] * labelmat[i] * (labelmat[j] - labelmat[i])
                b1 = b - Ei - labelmat[i] * (alpha[i] - alphaIold) * datamat[i, :] * datamat[i, :].T -\
                    labelmat[j] * (alpha[j] - alphaJold) * datamat[i, :] * datamat[j, :].T
                b2 =  b - Ej - labelmat[i] * (alpha[i] - alphaIold) * datamat[i, :] * datamat[j, :].T -\
                    labelmat[j] * (alpha[j] - alphaJold) * datamat[j, :] * datamat[j, :].T
                if 0 < alpha[i] and C > alpha[i]:
                    b = b1
                elif 0 < alpha[j] and C > alpha[j]:
                    b = b2
                else:
                    b = (b1 + b2)/2
                alphaPairsChanged += 1
        if alphaPairsChanged == 0:
            iterer += 1
        else:
            iterer = 0
    return b, alpha
