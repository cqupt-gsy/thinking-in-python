__author__ = 'Mentu'

def loadDataset():
    return [[1,3,4], [2,3,5], [1,2,3,5], [2,5]]

def createC1(dataset):
    C1 = []
    for transaction in dataset:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return list(map(frozenset, C1))

def scanD(D, Ck, minsupport):
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if can not in ssCnt.keys():
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1
    numItems = float(len(D))
    retlist = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key]/numItems
        if support >= minsupport:
            retlist.insert(0, key)
        supportData[key] = support
    return retlist, supportData

def aprioriGen(Lk, k):
    retlist = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i+1, lenLk):
            L1 = list(Lk[i])[: k-2]
            L2 = list(Lk[j])[: k-2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retlist.append(Lk[i] | Lk[j])
    return retlist

def apriori(dataset, minsupport=0.5):
    C1 = createC1(dataset)
    D = list(map(set, dataset))
    L1, supportdata = scanD(D, C1, minsupport)
    L = [L1]
    k = 2
    while len(L[k-2]) > 0:
        Ck = aprioriGen(L[k-2], k)
        Lk, supK = scanD(D, Ck, minsupport)
        supportdata.update(supK)
        L.append(Lk)
        k += 1
    return L, supportdata

def calcConf(freqset, H, supportdata, brl, minconf=0.7):
    prunedH = []
    for conseq in H:
        conf = supportdata[freqset] / supportdata[freqset - conseq]
        if conf >= minconf:
            brl.append((freqset - conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH

def rulesfromcnseq(freqset, H, supportdata, brl, minconf=0.7):
    m = len(H[0])
    if (len(freqset) > (m + 1)):
        Hmp1 = aprioriGen(H, m+1)
        Hmp1 = calcConf(freqset, Hmp1, supportdata, brl, minconf)
        if (len(Hmp1) > 1):
            rulesfromcnseq(freqset, Hmp1, supportdata, brl, minconf)

def generateRules(L, supportdata, minConf=0.7):
    bigrulelist = []
    for i in range(1, len(L)):
        for freqset in L[i]:
            H1 = [frozenset([item]) for item in freqset]
            if i > 1:
                rulesfromcnseq(freqset, H1, supportdata, bigrulelist, minConf)
            else:
                calcConf(freqset, H1, supportdata, bigrulelist, minConf)
    return bigrulelist