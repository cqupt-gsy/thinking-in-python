__author__ = 'Mentu'


class TreeNode:
    def __init__(self, namevalue, numoccur, parentnode):
        self.name = namevalue
        self.count = numoccur
        self.nodelink = None
        self.parent = parentnode
        self.children = {}

    def inc(self, numoccur):
        self.count += numoccur

    def disp(self, ind=1):
        print('  ' * ind, self.name, ' ', self.count)
        for child in self.children.values():
            child.disp(ind+1)

def loadDataset():
    dataset = [['r', 'z', 'h', 'j', 'p'],
               ['z', 'y', 'x', 'v', 'u', 't', 's'],
               ['z'],
               ['r', 'x', 'n', 'o', 's'],
               ['y', 'r', 'x', 'z', 'q', 't', 'p'],
               ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
    return dataset

def createInitset(dataset):
    retdic = {}
    for trans in dataset:
        retdic[frozenset(trans)] = 1
    return retdic

def updateTree(items, inTree, headertable, count):
    if items[0] in inTree.children:
        inTree.children[items[0]].inc(count)
    else:
        inTree.children[items[0]] = TreeNode(items[0], count, inTree)
        if headertable[items[0]][1] == None:
            headertable[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(headertable[items[0]][1], inTree.children[items[0]])
    if len(items) > 1:
        updateTree(items[1::], inTree.children[items[0]], headertable, count)

def updateHeader(nodetotest, targetnode):
    while  nodetotest.nodelink != None:
        nodetotest = nodetotest.nodelink
    nodetotest.nodelink = targetnode


def createTree(dataset, minsup=1):
    headertable = {}
    for trans in dataset:
        for item in trans:
            headertable[item] = headertable.get(item, 0) + dataset[trans]
    temp = {}
    for k in headertable.keys():
        if headertable[k] >= minsup:
            temp[k] = headertable[k]
    headertable.clear()
    headertable = temp.copy()
    temp.clear()
    freqItemset = set(headertable.keys())
    if len(freqItemset) == 0:
        return None, None
    for k in headertable:
        headertable[k] = [headertable[k], None]
    retTree = TreeNode('Null Set', 1, None)
    for transet, count in dataset.items():
        localD = {}
        for item in transet:
            if item in freqItemset:
                localD[item] = headertable[item][0]
        if len(localD) > 0:
            orderedItem = [v[0] for v in sorted(localD.items(), key=lambda p: p[1], reverse=True)]
            updateTree(orderedItem, retTree, headertable, count)
    return retTree, headertable

def ascendTree(leafnode, prefixpath):
    if leafnode.parent != None:
        prefixpath.append(leafnode.name)
        ascendTree(leafnode.parent, prefixpath)

def findPrefixPath(basepath, treenode):
    condpats = {}
    while treenode != None:
        prefixpath = []
        ascendTree(treenode, prefixpath)
        if len(prefixpath) > 1:
            condpats[frozenset(prefixpath[:])] = treenode.count
        treenode = treenode.nodelink
    return condpats

def mineTree(inTree, headertable, minsup, prefix, freqitemlist):

    bigL = [v[0] for v in sorted(headertable.items(), key=lambda p: p[1])]
    for basepat in bigL:
        newfreqset = prefix.copy()
        newfreqset.add(basepat)
        freqitemlist.append(newfreqset)
        condpattbases = findPrefixPath(basepat, headertable[basepat][1])
        mycondtree, myhead = createTree(condpattbases, minsup)
        if myhead != None:
            mineTree(mycondtree, myhead, minsup, newfreqset, freqitemlist)