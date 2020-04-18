__author__ = 'Mentu'

import numpy as np
import random

def loadDataset(filename):
    datamat = []
    fr = open(filename)
    for line in fr.readlines():
        curline = line.rstrip().split('\t')
        fitline = map(float, curline)#map函数是将参数2中的元素内容按参数1指定的函数进行转换，然后返回列表，这里是把curline中的原始全部转换成float类型,然后需要转回list类型才能使用
        datamat.append(list(fitline))
    return np.mat(datamat)

def distEclud(vecA, vecB):
    '''
    计算两个向量的欧式距离，一定要记住如果是处理的numpy中的数据和矩阵，一定要用numpy的函数
    :param vecA:
    :param vecB:
    :return:
    '''
    return np.sqrt(np.sum(np.power(vecA - vecB, 2)))

def randCent(dataset, k):
    '''
    生成随机的簇中心
    :param dataset: 数据集，类型为：[[],[],[]]
    :param k: 簇心的个数
    :return: 随机簇中心, 类型为[[], [], []]
    '''
    colnumber = np.shape(dataset)[1]
    centeroids = np.mat(np.zeros((k,colnumber)))
    for j in range(colnumber):
        minj = min(dataset[:, j])
        rangej = float(max(dataset[:, j]) - minj)
        centeroids[:, j] = minj + rangej * np.random.rand(k,1)#产生一个k行1列的随机数矩阵
    return centeroids

def kMeans(dataset, k, distmeas=distEclud, createcent=randCent):
    '''
    k-means核心函数
    :param dataset: 数据集，类型为：[[],[],[]]
    :param k: 簇中心个数
    :param distmeas: 欧式距离计算函数
    :param createcent: 产生随机簇中心函数
    :return:
    '''
    rownumber = np.shape(dataset)[0]
    clusterAssment = np.mat(np.zeros((rownumber , 2)))#存储每条数据是属于哪个簇中心，以及它与中心的距离
    centeroirds = createcent(dataset, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(rownumber):
            mindist = np.inf
            minindex = -1
            for j in range(k):
                distji = distmeas(centeroirds[j, :], dataset[i, :])
                if distji < mindist:
                    mindist = distji
                    minindex = j
            if clusterAssment[i, 0] != minindex:
                clusterChanged = True
                clusterAssment[i, :] = minindex, mindist ** 2
        for cent in range(k):
            ptsincluster = dataset[np.nonzero(clusterAssment[:,0].A == cent)[0]]
            centeroirds[cent, :] = np.mean(ptsincluster, axis=0)
    return centeroirds, clusterAssment

def biKmeans(dataset, k, distmeas=distEclud):
    '''
    二分kmeans算法核心函数
    :param dataset: 数据集，类型为：[[],[],[]]
    :param k: 簇中心个数
    :param distmeas:  欧式距离计算函数
    :return:
    '''
    rownumber = np.shape(dataset)[0]
    clusterAssment = np.mat(np.zeros((rownumber, 2)))
    centeroid_0 = np.mean(dataset, axis=0).tolist()[0]#通过原始训练集产生初始的簇中心
    centlist = [centeroid_0]
    for j in range(rownumber):
        clusterAssment[j,1] = distmeas(np.mat(centeroid_0), dataset[j, :]) ** 2 #计算每个训练集与簇中心的距离，也就是误差
    while len(centlist) < k:
        lowestSSE = np.inf
        for i in range(len(centlist)):
            ptsincluster = dataset[np.nonzero(clusterAssment[:,0].A == i)[0], :] #选取下标为i的簇中心的所有元素
            centeroidmat, splitclusterass = kMeans(ptsincluster, 2, distmeas)
            sseSplit = np.sum(splitclusterass[:, 1])
            ssenotsplit = np.sum(clusterAssment[np.nonzero(clusterAssment[:, 0].A != i)[0], 1])
            if sseSplit + ssenotsplit < lowestSSE:
                bestcenttosplit = i
                bestnewcent = centeroidmat
                bestclustass = splitclusterass.copy()
                lowestSSE = sseSplit + ssenotsplit
        bestclustass[np.nonzero(bestclustass[:, 0].A == 1)[0], 0] = len(centlist)
        bestclustass[np.nonzero(bestclustass[:, 0].A == 0)[0], 0] = bestcenttosplit
        centlist[bestcenttosplit] = bestnewcent[0, :]
        centlist.append(bestnewcent[1, :])
        clusterAssment[np.nonzero(clusterAssment[:, 0].A == bestcenttosplit)[0], :] = bestclustass
    return centlist, clusterAssment



