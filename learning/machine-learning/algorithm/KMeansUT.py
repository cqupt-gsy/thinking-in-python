__author__ = 'Mentu'

from KMeans import loadDataset
from KMeans import biKmeans

dataset = loadDataset(r'dataset\testSet2.txt')
mycenter, clustassign = biKmeans(dataset,4)
print(mycenter)