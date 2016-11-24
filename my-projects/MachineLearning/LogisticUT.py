__author__ = 'Mentu'

from Logistic import loadDataset
from Logistic import stocGradAscent
from Logistic import improveStocGradAscent

dataset, labelset = loadDataset()
print(improveStocGradAscent(dataset, labelset))