__author__ = 'Mentu'

import numpy as np
from math import log

#还差独立完成垃圾邮件分类器

def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    class_lable = [0,1,0,1,0,1]
    return  postingList, class_lable

def createVocabList(dataset):
    '''
    建立词汇表
    :param dataset: 原始文本数据集，类型为：[[],[],[]]
    :return: 词汇表，类型为：[]
    '''
    vocabset = set([])
    for document in dataset:
        vocabset = vocabset | set(document)#set集合可以用|求或预算,会将set中重复的元素去除
        #print(vocabset)
    return list(vocabset)

def setofWords2Vec(vocalist, inputset):
    '''
    将词汇表转化成0,1向量表，此函数是词集模型建立法，意思每个出现的词只对其计数为1
    :param vocalist: 词汇表，类型为：[]
    :param inputset: 每个文本的单词，类型为：[]
    :return:
    '''
    returnVec = [0] * len(vocalist)
    for word in inputset:
        if word in vocalist:
            returnVec[vocalist.index(word)] = 1#巧妙之处
    return returnVec

def bagofWords2Vec(vocalist, inputset):
    '''
    将词汇表转化成0,1向量表，此函数是词袋模型建立法，意思统计每个出现的词的次数
    :param vocalist: 词汇表，类型为：[]
    :param inputset: 每个文本的单词，类型为：[]
    :return:
    '''
    returnVec = [0] * len(vocalist)
    for word in inputset:
        if word in vocalist:
            returnVec[vocalist.index(word)] += 1#巧妙之处
    return returnVec

def calcConditionProp(trainmat, traincategory):
    '''
    计算训练集中文档中每个词属于某类型文档的条件概率
    :param trainmat: 训练集，原始数据集，并且已经转换成0,1向量表的数据集，类型为：[[],[],[]]
    :param traincategory: 训练集中文档的类型标号，类型为：[]
    :return: 属于类型0的所有词的条件概率，属于类型1的所有词的条件概率，以及类型1文档的概率
    '''
    numtraindocs = len(trainmat)
    numwords = len(trainmat[0])
    pClass_1 = sum(traincategory)/float(numtraindocs)#该式子是计算p(ci)本例子中只有两个类别，并用0和1进行标注，所以对所有类别求和就能求出一个类别的数量
    p0num = np.ones(numwords)
    p1num = np.ones(numwords)
    p0denom = 2.0
    p1denom = 2.0
    for i in range(numtraindocs):#计算p(w|ci)的概率，就是某个词在某类中出现的次数除以该类中总词数
        if traincategory[i] == 1:
            p1num += trainmat[i]#某些词在类型为1的文档中出现的次数，这种方法只适合统计词次数的算法，如果换成词的权值就不行了
            p1denom += sum(trainmat[i])#类型为1的文档中所有的词的数量
        else:
            p0num += trainmat[i]#原理同类型1的文档一致
            p0denom += sum(trainmat[i])
    p1result = p1num/p1denom
    p0result = p0num/p0denom
    return p0result, p1result, pClass_1

def naiveBayse(needclassify, p0vec, p1vec, pclass1):
    p1 = sum(needclassify*p1vec) * pclass1
    p0 = sum(needclassify*p0vec) * (1-pclass1)
    if p1 > p0:
        return 1
    else:
        return 0

def naiveBayseUT():
    dataset, lables = loadDataSet()
    vocablist = createVocabList(dataset)
    trainmat = []
    for line in dataset:
        trainmat.append(setofWords2Vec(vocablist, line))
    p0, p1, cp1 = calcConditionProp(trainmat, lables)
    testEntry = ['love', 'my', 'dalmation']
    testvec = setofWords2Vec(vocablist, testEntry)
    result = naiveBayse(testvec, p0, p1, cp1)
    print(result)


