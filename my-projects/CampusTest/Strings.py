__author__ = 'Mentu'

#alibaba test
def backSentence(wordlist, rawstring):
    '''
    还原字符串
    :param wordlist: 字典列表
    :param rawstring: 原始字符串
    :return: 加入空格后的字符串
    '''
    #从单词字典中选取单词
    wordlist.sort(key=str.__len__, reverse=True)
    # print(wordlist)
    for word in wordlist:
        if len(word) == 1:
            continue
        index = 0
        index = rawstring.find(word, index)
        stringlength = len(rawstring)
        wordlength = len(word)
        #从字符串中查找该单词出现的所有索引，按该索引以及对应的单词长度将该字符串截断
        while index != -1:
            firstpart = rawstring[0:index]
            middlepart = rawstring[index:(index+wordlength)]
            lastpart = rawstring[(index+wordlength) : stringlength]
            #用新的字符串将截断的字符串加入空格后复制给原来的字符串，直到单词字典中的单词全部查询完毕
            rawstring = firstpart[:] + ' ' + middlepart[:] + ' ' + lastpart[:]
            index = (index+wordlength+1)
            index = rawstring.find(word, index)
            stringlength = len(rawstring)
    #由于上述步骤会加入多的空格，需要去除多余的空格
    templist = rawstring.split(' ')
    finalresult = []
    for word in templist:
        if word != '':
            finalresult.append(word)
    print(finalresult)
    finalstring = ' '.join(finalresult)
    return finalstring

def adjustBackSentence(wordlist, finalstring):
    '''
    将过分分类的单词进行合并
    :param wordlist: 单词列表
    :param finalstring: 第一步分类的字符串
    :return:
    '''
    finallist = finalstring.split(' ')
    firstindex = []
    middleindex = []
    finalresult = ''
    #查找能够组成更长单词的字符串
    for index in range(len(finallist)):
        if index+1 < len(finallist):
            firststring = finallist[index-1] + finallist[index]
            middlestring =finallist[index-1] + finallist[index] + finallist[index+1]
            if wordlist.count(firststring) != 0:
                firstindex.append(index)
                continue
            if wordlist.count(middlestring) != 0:
                middleindex.append(index)
                continue
        else:
            tempstring =finallist[index-1] + finallist[index]
            if wordlist.count(tempstring) != 0:
                firstindex.append(index)
    skipnum = 0
    #进行合并
    for index in range(len(finallist)):
        if skipnum != 0 :
            skipnum = skipnum - 1
            continue
        if middleindex.count(index+1) != 0:
            if index+2 < len(finallist):
                finalresult += finallist[index] + finallist[index+1] + finallist[index+2] + ' '
                skipnum = 2
            else:
                finalresult += finallist[index] + finallist[index+1] + ' '
                skipnum = 1
        elif firstindex.count(index+1) != 0:
            finalresult += finallist[index] + finallist[index+1] + ' '
            skipnum = 1
        else:
            finalresult += finallist[index] + ' '
            skipnum = 0
    return finalresult

def backSentenceUT():
    #要求字典顺序中单词出现的顺序基本与原句相似
    wordlist = ['i', 'love', 'him', 'or', 'it', 'is', 'the', 'best', 'man', 'combine', 'beautiful', 'girl']
    rawstring = 'ilovehimoritisthebestmancombinebeautifulgirl'
    finalstring = backSentence(wordlist,rawstring)
    finalresult = adjustBackSentence(wordlist, finalstring)
    print(finalresult)
#alibaba test

#meituan test
def removeRepeatBlank(rawstr):
    list_a = rawstr.split(' ')
    list_b = [item for item in list_a if item != '']

    results = ' '.join(list_b)
    return results

def removeRepeatBlankUT():
    str = '  hello   world again   hello world     '
    print(removeRepeatBlank(str))

#removeRepeatBlankUT()
#meituan test

list_test = ['a', 'a', 'b']
print(list_test[0:3])









