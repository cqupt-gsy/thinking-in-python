__author__ = 'Mentu'

import numpy as np

def loadDataset(filename, delim='\t'):
    fr = open(filename)
    stringarr = [line.rstrip().split(delim) for line in fr.readlines()]
    datarr = [map(float, line) for line in stringarr]
    return np.mat(datarr)

def pca(datamat, topNfeat=9999999):
    meanvals = np.mean(datamat, axis=0)
    meanremoved = datamat - meanvals
    covmat = np.cov(meanremoved, rowvar=0)
    eigvals, eigvects = np.linalg.eig(np.mat(covmat))
    eigvalind = np.argsort(eigvals)
    eigvalind = eigvalind[:-(topNfeat+1):-1]
    redeigvects = eigvects[:, eigvalind]
    lowddatamat = meanremoved * redeigvects
    reconmat = (lowddatamat * redeigvects.T) + meanvals
    return lowddatamat, reconmat
