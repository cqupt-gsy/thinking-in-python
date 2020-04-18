__author__ = 'Mentu'
from datetime import datetime
from entity import Location


import os
import re
import pickle


str_formate='%Y-%m-%d %H:%M:%S'


def combileFileName(dirs, filename):
    '''
    合成文件路径-v1.1
    :param dirs: 目录名
    :param filename: 文件名
    :return: 完整的文件名，包含文件目录
    '''
    complete_name = os.path.join(dirs, filename)
    return complete_name

def preWalkFile(basepath=r'D:\MicrosoftDB\Geolife Trajectories 1.3\Data', regulars=r'(.*)\\(\d{3})\\Trajectory',
                skip_line=6, line_num=1, cur_users=0, read_users=1):
    '''
    处理原始数据文件，提取用户的地理位置数据，只取纬度、经度、记录时间-v1.1
    :param basepath:待扫描的路径
    :param regulars:正则表达式
    :param skip_line:读取文件时选择跳过的行数
    :param line_num:当前读的是第几行
    :param cur_users:当前读取的是第几个用户
    :param read_users:选择读取的用户数
    :return:
    '''
    for(thisDir, dirsHere, filesHere) in os.walk(basepath):#thisDir表示当前目录，dirsHere表示当前目录中存在的目录循环下次将以此进入此目录中进行运算，filesHere表示当前目录中的所有文件
        if cur_users <= read_users:
            if re.match(regulars,thisDir):#寻找匹配的目录
                match = re.match(regulars,thisDir)
                number = int(match.group(2))
                print('[%d] User begin' % number)
                output_dir = 'rawsdata'
                output_filename = str(number) + 'user.txt'
                output_name = combileFileName(output_dir,output_filename)
                result = []
                for fname in filesHere:#需找目录中所有文件
                    read_filename = os.path.join(thisDir, fname)
                    line_num = 1
                    # skip = 1
                    for line in open(read_filename):#一行一行的将文件读出来
                        if line_num > skip_line:
                            # if skip % 2 !=0:
                            content = line.rstrip().split(',')#将原始数据分割
                            date = content[5]
                            time = content[6]
                            content_time = datetime.strptime(date + ' ' + time, str_formate)#字符串转日期类型
                            result.append(content[0] + ',' + content[1] + ',' + content_time.strftime(str_formate))#日期类型转字符串
                            # skip += 1
                        line_num += 1
                output = open(output_name, 'w')
                for file_line in result:
                    output.write(file_line)
                    output.write('\n')
                output.close()
                cur_users += 1

def preWalkFileCVS(basepath=r'rawsdata', skip_line=1):
    '''
    处理原始数据文件，提取用户的地理位置数据，只取纬度、经度、记录时间-v1.1
    :param basepath:待扫描的路径
    :param regulars:正则表达式
    :param skip_line:读取文件时选择跳过的行数
    :param line_num:当前读的是第几行
    :param cur_users:当前读取的是第几个用户
    :param read_users:选择读取的用户数
    :return:
    '''
    for(thisDir, dirsHere, filesHere) in os.walk(basepath):#thisDir表示当前目录，dirsHere表示当前目录中存在的目录循环下次将以此进入此目录中进行运算，filesHere表示当前目录中的所有文件
        output_dir = 'rawsdata'
        output_filename = 'user.txt'
        output_name = combileFileName(output_dir,output_filename)
        result = []
        for fname in filesHere:#需找目录中所有文件
            read_filename = os.path.join(thisDir, fname)
            line_num = 1
            # skip = 1
            for line in open(read_filename):#一行一行的将文件读出来
                if line_num > skip_line:
                    # if skip % 2 !=0:
                    content = line.rstrip().split(',')#将原始数据分割
                    content_time = datetime.strptime(content[0], str_formate)#字符串转日期类型
                    result.append(content[1] + ',' + content[2] + ',' + content_time.strftime(str_formate))#日期类型转字符串
                    # skip += 1
                line_num += 1
        output = open(output_name, 'a')
        for file_line in result:
            output.write(file_line)
            output.write('\n')
        output.close()

def loadRawsData(dirs=r'rawsdata', fname=r'5477.txt'):
    '''
    从文本文件中加载原始地理位置数据信息，DBScan挖掘用户停留区域的数据源，包括纬度(浮点类型)、经度(浮点类型)、时间点(日期类型)-v1.1
    :param dirs: 目录名
    :param fname:是读取存储处理好的数据文件名
    :return: list[Location] 用户所有地理位置数量number
    '''
    fname = combileFileName(dirs, fname)
    result = []
    number = 0
    for line in open(fname):
        content = line.rstrip().split(',')
        location = Location()
        location.lat = float(content[0])
        location.longti = float(content[1])
        # location.timer = float(content[2])
        location.timer = datetime.strptime(content[2], str_formate)
        result.append(location)
        number += 1
    return result, number

def loadStayAreaTxtResults(dirs=r'showresults', fname=r'dbscanresult.txt'):
    '''
    从文本文件中加载停留区域数据信息，为画用户停留区域结果图提供数据源-v1.1
    :param dirs: 目录名
    :param fname: 文件名
    :return: 所有结果,类型为list[type, lat,longti,time]
    '''
    fname = combileFileName(dirs, fname)
    result = []
    for line in open(fname):
        result.append(line)
    return result

def loadStayAreaPklResults(dirs=r'saveresults',fname=r'dbscanresult.pkl'):
    '''
    从二进制文件中加载停留区数据信息，为挖掘停留位置提供数据源-v1.1
    :param dirs: 目录名
    :param fname: 文件名
    :return: 所有聚类结果，类型为list[StayArea]
    '''

    fname = combileFileName(dirs, fname)
    input_file = open(fname, 'rb')
    data = pickle.load(input_file)
    return data

def loadStayPointPklResults(dirs=r'saveresults',fname=r'clusterresult.pkl'):
    '''
    从二进制文件中加载停留位置数据信息，为挖掘用户分类提供数据源-v1.1
    :param dirs: 目录名
    :param fname: 文件名
    :return: 所有聚类结果，类型为list[StayPoint]
    '''
    fname = combileFileName(dirs, fname)
    input_file = open(fname, 'rb')
    data = pickle.load(input_file)
    return data

'''
第一阶段，DBSCAN聚类算法、Cluster组合聚类算法数据加载的代码在以上部分
'''

def loadClassifyData(dir=r'saveresults', filename=r'clusterresult.pkl'):
    '''
    从二进制文件中加载停留位置数据信息，为分类算法提供输入数据-v1.1
    :param dir: 保存结果目录名
    :param filename: 保存数据文件名
    :return: 返回所有用户的中心位置，类型为 dict{'user':list[location]}
    '''
    data = {}
    for (thisDir, dirsHere, filesHere) in os.walk(dir):
        for files in filesHere:
            user = files.split('&')[0]
            content = loadStayPointPklResults(dirs=dir, fname=files)
            locations = []
            for line in content:
                location = Location()
                location.lat, location.longti = line.centerlat, line.centerlon
                location.tfidf = 0
                locations.append(location)
            data[user] = locations
    return data

def loadClassifyPklResult(dir=r'classifypklresults', filename=r'classifyresult.pkl'):
    '''
    从二进制文件中加载用户分类结果数据信息，为轨迹检测提供数据参考-v1.0
    :param dirs: 目录名
    :param fname: 文件名
    :return: 用户分类结果，结果类型为list[UserClassify]
    '''
    fname = combileFileName(dir, filename)
    input_file = open(fname, 'rb')
    data = pickle.load(input_file)
    return data

'''
第二阶段，通过用户停留位置中心求TF-IDF值，并以此建立用户TF-IDF向量，以余弦定理计算用户相似性数据加载在以上部分
'''

# loadRawsData()