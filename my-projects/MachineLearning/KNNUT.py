__author__ = 'Mentu'

from KNN import creatDataset
from KNN import kNNLearningFromBooks
from KNN import file2matrix
from KNN import autoNorm
from KNN import datingClassTest


# group, lables = creatDataset()
# print(kNNLearningFromBooks([0,0], group, lables, 3))

dataset, classlable = file2matrix(r'dataset/datingTestSet2.txt')
normalData = autoNorm(dataset)
datingClassTest(normalData, classlable)