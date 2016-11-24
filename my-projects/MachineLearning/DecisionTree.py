__author__ = 'Mentu'

from math import log2
import operator

def createDataset():
    dataset = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    labels = ['no surfacing', 'flippers']
    return dataset, labels

def calcShannonEnt(dataset):
    '''
    计算香农熵
    :param dataset: 原始数据集，类型为：[[],[],[]]
    :return:
    '''
    total_lengh = len(dataset)
    lable_count = {}
    for line in dataset:
        current_lable = line[-1]
        if current_lable not in lable_count.keys():
            lable_count[current_lable] = 0
        lable_count[current_lable] += 1
    shannon = 0.0
    for key in lable_count.keys():
        value = float(lable_count.get(key))/total_lengh
        shannon -= value * log2(value)
    return shannon

def splitDataset(dataset, axis, value):
    '''
    计算信息增益值之前，先必须把数据集按属性列划分，也就是按源数据集中的列属性将数据集划分成N个新的列表
    :param dataset: 原始数据集，类型为：[[],[],[]]
    :param axis: 列标号,如果是0表示按第0列划分，保留后两列；也就是说按哪列划分需要保留的是其他列，待划分列是要删除的
    :param value: 列表号所属的元素的值
    :return:
    '''
    returnMat = []
    for line in dataset:
        if line[axis] == value:
            tempMat = line[:axis]#将列表按列标号划分的核心
            tempMat.extend(line[axis+1:])
            returnMat.append(tempMat)
    return returnMat

def calcGainInfo(dataset):
    '''
    ID3算法的核心，计算列属性的信息增益值，并选出信息增益值最大的列，作为划分列
    :param dataset: 原始数据集，类型为：[[],[],[]]
    :return:
    '''
    colnumber = len(dataset[0]) - 1
    baseShannonEnt = calcShannonEnt(dataset)
    bestGainInfo = 0.0
    bestFeature = -1
    for i in range(colnumber):
        allvalue = [value[i] for value in dataset]
        unique_value = set(allvalue)
        colShannonEnt = 0.0#保留数据集按列值划分后，每列的香农熵
        for values in unique_value:#特别注意这里，这是计算信息增益最复杂的一块
            new_mat = splitDataset(dataset, i, values)
            prop_weight = len(new_mat)/float(len(dataset))
            colShannonEnt += prop_weight * calcShannonEnt(new_mat)
        gainInfo = baseShannonEnt - colShannonEnt
        if gainInfo > bestGainInfo:
            bestGainInfo = gainInfo
            bestFeature = i
    return bestFeature

def topClassLabel(classlabels):
    '''
    对不确定属性分类排序，选择排序最高的为最终分类
    :param classlabels: 原始类标签，类型为：[]
    :return:
    '''
    class_count = {}
    for classlabel in classlabels:
        if classlabel not in class_count.keys():
            class_count[classlabel] = 0
        class_count[classlabel] += 1
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]

def createTree(dataset, labels):
    '''
    创建决策树，递归创建
    :param dataset:  原始数据集，类型为：[[],[],[]]
    :param labels: 原始类标签，类型为：[]
    :return:
    '''
    # print('#######################################################')
    class_list = [example[-1] for example in dataset]
    # print(class_list)
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]
    if len(dataset[0]) == 1:
        return topClassLabel(class_list)
    bestFeature = calcGainInfo(dataset)#计算最好的划分属性
    # print('before del of bestFeature: %d' % bestFeature)
    # print(labels)
    bestFeatureLable = labels[bestFeature]
    # print('bestFeatureLable: %s' % bestFeatureLable)
    mytree = {bestFeatureLable:{}}#建立划分属性的树节点
    # print(mytree)
    del labels[bestFeature]
    # print('after del of bestFeature: %d' % bestFeature)
    # print(labels)
    featureValues = [example[bestFeature] for example in dataset]
    # print(featureValues)
    uniqueValues = set(featureValues)#set可以去除列表中重复的元素
    # print(uniqueValues)
    for unique_value in uniqueValues:
        sub_labels = labels[:]
        mytree[bestFeatureLable][unique_value] = createTree(splitDataset(dataset,bestFeature,unique_value), sub_labels)
        # print(mytree)
    return mytree

def decisionTreeUT(inputtree, featurelable, testvec):
    '''
    决策树单元测试函数，也是递归遍历
    :param inputtree: 决策树，是由dict类型复合组成的树结构
    :param featurelable: 原始分类标签，类型为：[]
    :param testvec: 测试向量，类型为：[]
    :return:
    '''
    firstvec = list(inputtree.keys())[0]
    secondvec = inputtree[firstvec]
    featureindex = featurelable.index(firstvec)#获得列属性名称的索引
    for key in secondvec.keys():
        if testvec[featureindex] == key:#获得列属性名称下对应的测试值
            if type(secondvec[key]).__name__ == 'dict':
                classlable = decisionTreeUT(secondvec[key], featurelable, testvec)
            else:
                classlable = secondvec[key]
        else:
            classlable = 'unknow'
    return classlable

