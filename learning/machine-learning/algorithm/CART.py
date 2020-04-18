__author__ = 'Mentu'

import numpy as np

def loadDataSet(filename):
    datamat = []
    fr = open(filename)
    for line in fr.readlines():
        curline = line.rstrip().split('\t')
        fltline = map(float, curline)
        datamat.append(fltline)
    return datamat

def binSplitDataset(dataset, feature, value):
    mat0 = dataset[np.nonzero(dataset[:, feature] > value)[0], :][0]
    mat1 = dataset[np.nonzero(dataset[:, feature] <= value)[0], :][0]
    return mat0, mat1

def regLeaf(dataset):
    return np.mean(dataset[:, -1])

def regErr(dataset):
    return np.var(dataset[:, -1]) * np.shape(dataset)[0]

def chooseBestSplit(dataset, leafType, errType, ops):
    tolS = ops[0]
    tolN = ops[1]
    if len(set(dataset[:, -1].T.tolist()[0])) == 1:
        return None, leafType(dataset)
    m, n = np.shape(dataset)
    S = errType(dataset)
    bestS = np.inf
    bestindex = 0
    bestvalue = 0
    for featindex in range(n-1):
        for splitval in set(dataset[:, featindex]):
            mat0, mat1 = binSplitDataset(dataset, featindex, splitval)
            if (np.shape(mat0)[0] < tolN) or (np.shape(mat1)[0] < tolN):
                continue
            newS = errType(mat0) + errType(mat1)
            if newS < bestS:
                bestindex = featindex
                bestvalue = splitval
                bestS = newS
    if S - bestS < tolS:
        return None, leafType(dataset)
    mat0, mat1 = binSplitDataset(dataset, bestindex, bestvalue)
    if (np.shape(mat0)[0] < tolN) or (np.shape(mat1)[0] < tolN):
        return None, leafType(dataset)
    return bestindex, bestvalue


def createTree(dataset, leafType=regLeaf, errType=regErr, ops=(1,4)):
    '''
    分类回归树主函数，后续继续学习其构造树的思路以及树减枝代码
    :param dataset:
    :param leafType:
    :param errType:
    :param ops:
    :return:
    '''
    feat, val = chooseBestSplit(dataset, leafType, errType, ops)
    if feat == None:
        return val
    retTree = {}
    retTree['spInd'] = feat
    retTree['spVal'] = val
    lSet, rSet = binSplitDataset(dataset, feat, val)
    retTree['left'] = createTree(lSet, leafType, errType, ops)
    retTree['right'] = createTree(rSet, leafType, errType, ops)
    return retTree
