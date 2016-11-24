__author__ = 'Mentu'

from DecisionTree import createDataset
from DecisionTree import createTree
from DecisionTree import decisionTreeUT

dataset, labels = createDataset()
mytree = createTree(dataset, labels[:])#如果函数内改变了列表的值一定要记得这样传参
print(decisionTreeUT(mytree,labels,[1,1]))

