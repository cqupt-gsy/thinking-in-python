__author__ = 'Mentu'

from Apriori import loadDataset
from Apriori import apriori
from Apriori import generateRules

dataset = loadDataset()
L, supportdata = apriori(dataset)

rules = generateRules(L, supportdata)
print(rules)