__author__ = 'Mentu'

from AdaBoost import loadDataset
from AdaBoost import adaBoostTrainDB
from AdaBoost import adaClassifyUT


dataset, classlabel, D = loadDataset()
classarr = adaBoostTrainDB(dataset, classlabel)
print(adaClassifyUT([[0,0],[5,5]], classarr))
