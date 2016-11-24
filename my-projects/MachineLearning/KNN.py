__author__ = 'Mentu'

import numpy as np
import operator

def creatDataset():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return  group, labels

def kNNLearningFromBooks(inX, dataSet, labels, k):#选择距离最近的前K个
    '''
    KNN算法的实现思路
    :param inX: 待检测的元素，类型为：[]
    :param dataSet: 原始数据集，类型为：[[],[],[],[]]
    :param labels: 原始数据集所对应的标签，类型为：[]
    :param k: 选取最近的个数
    :return: 待检测原始的标签
    '''
    dataSetSize = dataSet.shape[0] #array.shape[0] means the array's row number, array.shape[1]means the array's column number
    # print('dataSetSize: %d' % dataSetSize)
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet #将inX这个元素，按(dataSetSize, 1)的内容构造多维数组，第一个元素是行，第二个是列，以此类推
    # print(diffMat)
    sqDiffMat = diffMat ** 2 #将二维数组的每个元素都平方
    # print(sqDiffMat)
    sqDistances = np.cumsum(sqDiffMat, axis=1) #axis=0 行元素相加， axis=1 列元素相加
    # print(sqDistances)
    distances = sqDistances ** 0.5 #将二维数据的每个元素都开方
    # print(distances)
    sortedDistIndicies = np.argsort(distances, axis=0)#axis=0 行元素排序， axis=1 列元素排序, 根据元素的内容大小，排序其对应的索引
    # print(sortedDistIndicies)
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i,-1]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True) #key用来指出排序的方式
    #print(sortedClassCount)
    return sortedClassCount[0][0]

def file2matrix(filename):
    files = open(filename).readlines()
    numberofLines = len(files)
    returnMat = np.zeros((numberofLines, 3))#zeros生成N行M列的多维数组，每个元素都是0
    classLabelVector = []
    index = 0
    for line in files:
        content = line.rstrip().split('\t')
        returnMat[index, : ] = content[0:3]#numpy array可以直接把数组进行赋值
        classLabelVector.append(int(content[-1]))
        index += 1
    return returnMat, classLabelVector

def autoNorm(dataset):
    '''
    归一化数据集
    :param dataset: 原始数据集，类型为：[[],[],[],[]]
    :return: 归一化处理后的数据集
    '''
    minVals = dataset.min(0)#0按行求最小值，1按列求最小值；获得每一列的最小值，有N列/行就是有N个元素的一维数组
    maxVals = dataset.max(0)#0按行求最大值，1按列求最大值；获得每一列的最大值，有N列/行就是有N个元素的一维数组
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataset))#获得数组的行和列组成的元组原始(N,M)
    m = dataset.shape[0]
    normDataSet = dataset - np.tile(minVals, (m, 1))#只有numpy的数组可以这样做
    normDataSet = normDataSet / np.tile(ranges, (m, 1))#只有numpy的数组可以这样做
    return normDataSet

def datingClassTest(dataset, lables):
    '''
    KNN分类器测试函数
    :param dataset: 原始数据集，类型为：[[],[],[],[]]
    :param lables:  原始数据集所对应的标签，类型为：[]
    :return:
    '''
    hoRatio = 0.10
    m = dataset.shape[0]
    numTestVecs = int(m * hoRatio)
    errorcount = 0.0
    for i in range(numTestVecs):
        results = kNNLearningFromBooks(dataset[i, : ], dataset[numTestVecs : m, : ], lables[numTestVecs : m], 3)
        print('the result is 【%d】, the real result is 【%d】' % (results, lables[i]))

        if results != lables[i]:
            errorcount += 1.0
    print('the error rate is %f' % (errorcount/float(numTestVecs)))

