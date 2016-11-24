__author__ = 'Mentu'

from SVD import locdexdata
from SVD import recommend
from SVD import svdest
import  numpy as np

mattest = np.mat(locdexdata())
print(recommend(mattest,2,estmethod=svdest))