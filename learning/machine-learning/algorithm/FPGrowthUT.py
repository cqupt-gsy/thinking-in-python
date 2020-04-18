__author__ = 'Mentu'

from FPGrowth import loadDataset
from FPGrowth import createInitset
from FPGrowth import createTree
from FPGrowth import mineTree

dataset = loadDataset()
initset = createInitset(dataset)

mytree, myheadtable = createTree(initset, 3)
freqitems = []
mineTree(mytree, myheadtable, 3, set([]), freqitems)

# mytree.disp()
