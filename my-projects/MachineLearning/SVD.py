__author__ = 'Mentu'

import numpy as np
from numpy import linalg as la


def locdexdata():
    return [[4,4,0,2,2],
            [4,0,0,3,3],
            [4,0,0,1,1],
            [1,1,1,2,0],
            [2,2,2,0,0],
            [1,1,1,0,0],
            [5,5,5,0,0]]

def ecludsim(ina, inb):
    '''
    欧式距离
    :param ina:
    :param inb:
    :return:
    '''
    return 1.0/(1.0 +la.norm(ina - inb))

def pearssim(ina, inb):
    '''
    皮尔逊相关系数
    :param ina:
    :param inb:
    :return:
    '''
    if len(ina) < 3:
        return 1.0
    return 0.5 + 0.5 * np.corrcoef(ina, inb, rowvar=0)[0][1]

def cossim(ina, inb):
    '''
    余弦相似度
    :param ina:
    :param inb:
    :return:
    '''
    num = float(ina.T * inb)
    denom = la.norm(ina) * la.norm(inb)
    return 0.5 + 0.5 * (num / denom)

def standEst(datamat, user, simmeas, item):
    '''
    主要是通过物品相似度预测用户对没有评分的物品的评分来进行物品推荐，要选择用户对其他物品已经评过分的物品来计算未评分物品的分值
    :param datamat:
    :param user:
    :param simmeas:
    :param item:
    :return:
    '''
    n = np.shape(datamat)[1]
    simtotal = 0.0
    ratsimtotal = 0.0
    for j in range(n):
        userrating = datamat[user,j]
        if userrating == 0:
            continue
        overlap = np.nonzero(np.logical_and(datamat[:, item].A>0, datamat[:, j].A>0))[0]
        print(overlap)
        if len(overlap) == 0:
            similarity = 0
        else:
            similarity = simmeas(datamat[overlap, item], datamat[overlap, j])
        simtotal += similarity
        ratsimtotal += similarity * userrating
    if simtotal == 0:
        return 0
    else:
        return ratsimtotal/simtotal

def svdest(datamat, user, simmeas, item):
    '''
    利用奇异值分解后做基于物品的推荐引擎，要选择用户对其他物品已经评过分的物品来计算未评分物品的分值
    :param datamat:
    :param user:
    :param simmeas:
    :param item:
    :return:
    '''
    n = np.shape(datamat)[1]
    simtotal = 0.0
    ratsimtotal = 0.0
    U, sigma, VT = la.svd(datamat)
    sig4 = np.mat(np.eye(4) * sigma[:4])
    xformeditems = datamat.T * U[:, :4] * sig4.I
    for j in range(n):
        userrating = datamat[user, j]
        if userrating == 0 or j == item:
            continue
        similarity = simmeas(xformeditems[item, :].T, xformeditems[j, :].T)
        simtotal += similarity
        ratsimtotal += similarity * userrating
    if simtotal == 0:
        return 0
    else:
        return ratsimtotal/simtotal

def recommend(datamat, user, N=3, simmeas=cossim, estmethod=standEst):
    unrateditems = np.nonzero(datamat[user, :].A == 0)[1]
    print(unrateditems)
    if len(unrateditems) == 0:
        return 'you rated everything'
    itemscores = []
    for item in unrateditems:
        estimatedscore = estmethod(datamat, user, simmeas, item)
        itemscores.append((item, estimatedscore))
    return sorted(itemscores, key=lambda jj:jj[1], reverse=True)[:N]