__author__ = 'Mentu'

from LinerRegression import loadDataset
from LinerRegression import ridgeTest

dataset, laberset = loadDataset(r'dataset\ex0.txt')
print(ridgeTest(dataset ,laberset))