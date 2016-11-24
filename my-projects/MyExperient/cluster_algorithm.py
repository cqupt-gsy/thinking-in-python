__author__ = 'Mentu'

import math
import pickle

from pre_read_file import preWalkFile
from pre_read_file import loadRawsData
from pre_read_file import combileFileName

from entity import StayArea
from entity import StayPoint
from entity import Location
from entity import UserClassify


def readAllData(number=1):
    '''
    预处理原始数据，将用户原始地理位置数据按用户ID整理成文件，只提取纬度、经度以及采集时间三个属性-v1.1
    :param number:所需要读取原始用户数据的数量
    :return:
    '''
    preWalkFile(read_users=number)


def loadProcessData(dir=r'rawsdata', name=r'0user.txt'):
    '''
    从用户地理位置数据文件中加载用户原始地理位置数据-v1.1
    :param dir: 目录名
    :param name:是处理好的数据存放文件名
    :return: list[Location]，该用户所有的地理位置数量number
    '''
    rawsdata_result, number = loadRawsData(dirs=dir, fname=name)
    return rawsdata_result, number


def minusDate(date_1, date_2):
    '''
    计算两个日期差-v1.1
    :param date_1:日期一
    :param date_2:日期二
    :return:timedelta对象，保存两个日期的时间差
    '''
    if date_1 < date_2:
        dateminu_result = date_2 - date_1
    else:
        dateminu_result = date_1 - date_2
    return dateminu_result  # 返回timedelta对象，通过实例属性seconds,days获得两个日期差距的天数和秒数


def calDistance(location_1, location_2):
    '''
    通过经纬度计算两个位置的实际距离单位是米-v1.1
    :param location_1:位置一
    :param location_2:位置二
    :return:实际距离结果，保留两位小数
    '''
    pi_num = 0.01745329
    radlat1 = location_1.lat * pi_num  # math.pi/180=0.01745329
    radlat2 = location_2.lat * pi_num
    a = radlat1 - radlat2
    radlongti1 = location_1.longti * pi_num
    radlongti2 = location_2.longti * pi_num
    b = radlongti1 - radlongti2
    temp_a = math.sin(a / 2) ** 2
    temp_b_sin = math.sin(b / 2) ** 2
    temp_b = math.cos(radlat1) * math.cos(radlat2) * temp_b_sin
    temp_asin = (temp_a + temp_b) ** 0.5
    s = 2 * math.asin(temp_asin)
    # m = 2 * math.asin(math.sqrt(math.pow(math.sin(a/2),2)+math.cos(radlat1)*math.cos(radlat2)*math.pow(math.sin(b/2),2)))
    earth_radius = 6378137  # 地球半径，单位为米，求出的结果单位为米；单位为千米，求出的结果单位为千米
    distance_result = math.fabs(s * earth_radius)
    distance_result = round(distance_result, 2)
    return distance_result


def calAvgPoint(all_nerborhoo_points):
    '''
    计算邻居节点的平局值-v1.1
    :param all_nerborhoo_points: list[Location] 该停留区域或停留位置所有的邻居节点
    :return: [avglat, avglon] 该聚类的平均经纬度
    '''
    totallat = 0.0
    totallon = 0.0
    totalpoints = len(all_nerborhoo_points)
    for item in all_nerborhoo_points:
        totallat += item.lat
        totallon += item.longti
    avglat = totallat / totalpoints
    avglon = totallon / totalpoints
    avgvalue_result = [avglat, avglon]
    return avgvalue_result


def adjustStayArea(user_stayareas):
    '''
    整理DBScan聚类算法结果，将聚类结果保存到StayArea类中-v1.0
    :param user_stayareas: dict{key:Location, value:list[Location]} 聚类算法的结果，是一个字典类型，key是聚类的首个Loction节点，value是该聚类的所有邻居Loction节点是个列表
    :return: list[StayArea] 一个StayArea类的列表
    '''
    print('Adjustment beginlocation')
    user_stayarea = []
    for key in user_stayareas.keys():
        stayarea = StayArea()
        stayarea.nerborhoods = user_stayareas.get(key)
        stayarea.nerborhoods.append(key)
        stayarea.centerlat, stayarea.centerlon = calAvgPoint(stayarea.nerborhoods)
        user_stayarea.append(stayarea)
    print('Adjustment Ends')
    return user_stayarea


def dbscanFindStayArea(dir=r'rawsdata', filename=r'0user.txt', mindist=600, minpointper=100):
    '''
    DBScan方法挖掘用户停留点区域-v1.1
    :param dir: 目录名
    :param filename:读取原始数据的文件
    :param mindist:最小距离间隔
    :param minpointper:最小点数
    :return: dict{key:Location, value:list[Location]}，某用户所有的停留区域的字典,
    '''
    result = {}
    rawdata, number = loadProcessData(dir=dir, name=filename)  # rawdata类型为list[Location]
    minpoint = number / minpointper
    for first_item in rawdata:
        first_loop = rawdata.index(first_item)
        print('Begins Location [%d], left [%d]' % (first_loop, len(rawdata) - first_loop))
        nerborhood = []  # 保存所有邻居节点
        for second_item in rawdata:
            if first_item == second_item:
                continue
            dist = calDistance(first_item, second_item)  # 计算点与点之间的距离
            if dist <= mindist:
                nerborhood.append(second_item)
        if len(nerborhood) >= minpoint:  # 当邻居节点满足一定数量时，获得一个聚类中心
            result[first_item] = nerborhood.copy()
            for remove_item in nerborhood:
                rawdata.remove(remove_item)
        rawdata.remove(first_item)
    return result


def clusterFindStayPoint(data, mindist=100, maxdist=240, mintime=1800, maxtime=86400):
    '''
    通过在mindist距离内，停留超过mintime间隔的思想，挖掘停留位置-v1.1
    :param data: 某用户的停留区域数据，类型为list[StayArea]
    :param mindist: 最小距离间距
    :param maxdist: 最大距离
    :param mintime: 最小停留时间间隔
    :param maxtime: 最大停留时间间隔
    :return: list[StayPoint]
    '''
    result = []
    nerborhood = []
    first_loop = 0
    for index in range(len(data)):  # data的类型为list[StayArea]
        rawdata = data[index].nerborhoods  #nerborhoods为list[location]类型
        print('Begins StayArea [%d]' % (index))
        while first_loop < len(rawdata):  #第一次循环开始
            print('Begins location [%d], left [%d]' % (first_loop, len(rawdata) - first_loop))
            for second_loop in range(first_loop + 1, len(rawdata)):  #第二次循环开始
                dist = calDistance(rawdata[first_loop], rawdata[second_loop])
                if maxdist >= dist >= mindist:  #当找到满足与第一个点的距离条件时这时记录第二个点
                    diftime = minusDate(rawdata[first_loop].timer, rawdata[second_loop].timer)
                    # diftime = rawdata[second_loop].timer - rawdata[first_loop].timer
                    if diftime.seconds >= mintime and diftime.days == 0:  #计算两点之间的时间间隔是否满足需求
                    # if maxtime >= diftime >= mintime:
                        for nerbor_index in range(first_loop, second_loop + 1):
                            nerborhood.append(rawdata[nerbor_index])
                        staypoint = StayPoint()
                        staypoint.nerborhoods = nerborhood.copy()
                        staypoint.centerlat, staypoint.centerlon = calAvgPoint(nerborhood)
                        result.append(staypoint)  #保存停留点
                    nerborhood = []
                    first_loop = second_loop  #从计算完的剩下的点中继续
                    break
            first_loop += 1
        print('Ends StayArea [%d]' % (index))
    return result


def outputTxtResults(data, user='0user', dir=r'showresults', filename=r'dbscanresult.txt'):
    '''
    将挖掘停留区域结果数据导出为文本文件，给画图程序提供源数据-v1.1
    :param data: 挖掘停留区域或停留位置的结果集，类型为list[StayArea]或list[StayPoint]
    :param dir: 目录名
    :param filename: 输出数据文件名
    :return:
    '''
    filename = user + '&' + str(len(data)) + '&' + filename
    filename = combileFileName(dir, filename)
    print('Output beginlocation')
    outfile = open(filename, 'w')
    print('Total StayArea|StayPoint center: %d ' % (len(data)))
    for item in data:
        print('StayArea|StayPoint [%d] has [%d] nerborhoods' % (data.index(item), len(item.nerborhoods)))
        outfile.write('Center')
        outfile.write(',')
        outfile.write(str(item.centerlat))
        outfile.write(',')
        outfile.write(str(item.centerlon))
        outfile.write('\n')
        for nerbor in item.nerborhoods:
            outfile.write('Nerborhood')
            outfile.write(',')
            outfile.write(str(nerbor.lat))
            outfile.write(',')
            outfile.write(str(nerbor.longti))
            outfile.write(',')
            outfile.write(str(nerbor.timer))
            outfile.write('\n')
    outfile.close()
    print('Output endlocation')


def outputPklResults(data, user='0user', dir=r'saveresults', filename=r'dbscanresult.pkl'):
    '''
    保存停留区域或者停留位置挖掘结果，以二进制形式保存，将结果序列化保存-v1.1
    :param data: 需要保存的停留区域以及停留位置数据  list[StayArea]或list[StayPoint]
    :param dir: 目录名
    :param filename: 保存数据的文件名
    :return:
    '''
    print('Output beginlocation')
    filename = user + '&' + str(len(data)) + '&' + filename
    filename = combileFileName(dir, filename)
    out_file = open(filename, 'wb')
    pickle.dump(data, out_file)
    out_file.close()
    print('Output endlocation')


'''
第一阶段，DBSCAN聚类算法挖掘用户停留区域、Cluster聚类算法挖掘用户停留位置在以上部分
'''


def buildLocationVector(raws_user_staypointcenter, mindist=80):
    '''
    建立分类算法时需要用到的用户总的位置向量列表，提取用户停留位置中心，删除重复的停留位置中心-v1.1--------------算法还存在漏洞，在最后写毕设的时候再来排查
    :param raws_user_staypointcenter: dict{'user':list[Location]}，原始用户的位置数据
    :param mindist: 位置归类，最小距离为20m
    :return: 所有用户的停留位置中心向量列表final_vector类型为list[Location]
    '''
    final_vector = []
    for key_fisrt in raws_user_staypointcenter.keys():
        content = raws_user_staypointcenter.get(key_fisrt)  # 获得某个用户的所有中心位置点
        skip = False
        for item in content:  # 开始循环
            for skip_item in final_vector:  #查找某个位置是否已经添加至最终位置列表中
                if skip_item.lat == item.lat and skip_item.longti == item.longti:  #由于每次添加位置信息都是新生产一个Location类型实例，所以必须要使用数值相等判断是否相等而不能使用地址相等判断
                    # print('------skipping [%f,%f] ==> [%f,%f]------' % (skip_item.lat, skip_item.longti, item.lat, item.longti))
                    skip = True
                    break
            if skip:
                skip = False
                continue
            nerbor = []
            for key_second in raws_user_staypointcenter.keys():  #从所有用户数据中依次寻找符合条件的同类型中心点
                temp = raws_user_staypointcenter.get(key_second)
                for line in temp:
                    if item == line:
                        continue
                    dist = calDistance(item, line)
                    if dist <= mindist:  #符合条件的中心点，依次添加至临时向量中，由于这里是直接添加的中心点的地址，因此在后续修改数值时，可以直接影响原始结果
                        nerbor.append(line)
            if len(nerbor) != 0:
                nerbor.append(item)
                location = Location()
                location.lat, location.longti = calAvgPoint(nerbor)
                isnew = False  #用来判断是否产生新的中心点
                for ci in nerbor:
                    for cm in final_vector:  #判断这个新的中心点是否是从已经计算过的中心点中再次产生的
                        if cm.lat == ci.lat and cm.longti == ci.longti:  #表明新产生的中心点是从已经计算过的中心点中产生的，因此只需修改已计算过的中心点数值，然后将其他中心点的值改为最新值即可
                            isnew = True
                            cm.lat, cm.longti = location.lat, location.longti
                            break
                    # print('******changing [%f,%f] ==> [%f,%f]******' % (ci.lat, ci.longti, location.lat, location.longti))
                    ci.lat, ci.longti = location.lat, location.longti
                if not isnew:  #表明这是一个完成新产生的中心点
                    final_vector.append(location)
            else:
                final_vector.append(item)
    return final_vector


def buildUserLocationVector(raws_user_staypointcenter):
    '''
    建立用户位置向量列表，将用户停留位置中心重复的删去-v1.1
    :param raws_user_staypointcenter: 原始位置数据集，但是已经完成了统一化操作，也就是说所有相同的中心点都设置成一样的了，类型为dict{'user':list[location]}
    :return: 用户向量列表，类型为dict{'user':list[location]}
    '''
    user_vector = {}
    for key in raws_user_staypointcenter.keys():
        content = raws_user_staypointcenter.get(key)
        temp_vector = []
        for item in content:
            hasadded = False
            for temp_item in temp_vector:
                if temp_item.lat == item.lat and temp_item.longti == item.longti:
                    hasadded = True
                    break
            if not hasadded:
                temp_vector.append(item)
        user_vector[key] = temp_vector.copy()
    return user_vector


def calUserTFIDF(user, user_location_vector, raws_user_staypointcenter, allusers=32):
    '''
    计算某个用户的TFIDF值-v1.1
    :param user: 用户标识
    :param user_location_vector: 某个用户的位置向量表，类型为list[location]类型
    :param raws_user_staypointcenter: 所有用户的原始数据，类型为dict{'user':list[location]}
    :param allusers: 总用户数
    :return: 一定记住，使用了类的实例变量也就是对象的话，操作的都是地址，除了new一个新对象外，其他都是会直接影响原值，因此无需重复赋值
    '''
    tf_totalnumber = len(user_location_vector)
    idf_totalnumber = allusers + 1
    for user_location in user_location_vector:  # 从某个用户的停留位置中心开始遍历
        tf_showtimes = 0
        idf_showtimes = 0
        for key in raws_user_staypointcenter.keys():  #遍历其他用户的停留位置中心
            others_locations = raws_user_staypointcenter.get(key)
            if key == user:  #如果是该用户自己的停留位置中心
                idf_showtimes += 1  #IDF出现次数加1
                for content in others_locations:  #计算该停留位置中心的TF出现次数
                    if content.lat == user_location.lat and content.longti == user_location.longti:  #统计该位置在该用户中出现的次数
                        tf_showtimes += 1  #TF出现次数加1
            else:
                for content in others_locations:  #如果是其他用户的停留位置中心
                    if content.lat == user_location.lat and content.longti == user_location.longti:  #统计该位置在所有用户中出现的次数
                        idf_showtimes += 1  #IDF出现次数加1，并停止此用户的遍历
                        break
        idf_showtimes += 1
        tf_value = tf_showtimes / tf_totalnumber
        idf_value = math.log10(idf_totalnumber / idf_showtimes)
        tfidf_value = tf_value * idf_value
        user_location.tfidf = tfidf_value


def calAllUsersTFIDF(all_user_location_vector, raws_user_staypointcenter, allusers=32):
    '''
    计算所有用户位置的TFIDF值-v1.1
    :param all_user_location_vector: 总的用户位置向量表，剔除了重复的，类型为dict{'user':list[location]}
    :param raws_user_staypointcenter: 所有用户原始的位置向量，没剔除重复的dict{'user':list[location]}
    :param allusers: 总用户数
    :return:
    '''
    for key in all_user_location_vector.keys():
        user_location_vector = all_user_location_vector.get(key)
        calUserTFIDF(key, user_location_vector, raws_user_staypointcenter, allusers)


def buildUserTFIDFVector(user_location_vector, user_final_location_vector):
    '''
    建立某个用户的TFIDF向量列表-v1.1
    :param user_location_vector: 某用户的停留位置中心向量列表，类型为list[location]
    :param user_final_location_vector: 所有用户总的停留位置向量列表，类型为list[location]
    :return: 返回值为list[location]
    '''
    result = []
    for raws_locations in user_final_location_vector:
        location = Location()
        location.lat, location.longti = raws_locations.lat, raws_locations.longti
        location.tfidf = 0
        for item in user_location_vector:
            if location.lat == item.lat and location.longti == item.longti:
                location.tfidf = item.tfidf
                break
        result.append(location)
    return result


def buildAllUserTFIDFVector(all_user_location_vector, user_final_location_vector):
    '''
    计算所有用户的TFIDF向量列表-v1.1
    :param all_user_location_vector: 所有用户的位置向量，类型为dict{'user':list[location]}
    :param user_final_location_vector: 所有用的总位置向量列表，类型为list[location]
    :return: 返回值为dict{'user':list[location]}
    '''
    final_result = {}
    for key in all_user_location_vector.keys():
        user_location_vector = all_user_location_vector.get(key).copy()
        temp_result = buildUserTFIDFVector(user_location_vector, user_final_location_vector)
        final_result[key] = temp_result.copy()
    return final_result


def calCosDistance(first_user_location_vector, second_user_location_vector):
    '''
    计算两个用户的TFIDF向量的余弦cos值-v1.1
    :param first_user_location_vector: 第一个用户的位置向量
    :param second_user_location_vector: 第二个用户的位置向量
    :return: 两个用户的cos值
    '''
    total_distance = 0
    temp_first_user_distance = 0
    temp_second_user_distance = 0
    for index in range(len(first_user_location_vector)):
        temp_first_user_distance += (first_user_location_vector[index].tfidf ** 2)  # 计算第一个用户的位置向量聚类
        temp_second_user_distance += (second_user_location_vector[index].tfidf ** 2)  # 计算第二个用户的位置向量聚类
        total_distance += (
            first_user_location_vector[index].tfidf * second_user_location_vector[index].tfidf)  # 计算两个用户位置向量的乘积
    first_user_distance = math.sqrt(temp_first_user_distance)
    second_user_distance = math.sqrt(temp_second_user_distance)
    if first_user_distance == 0 or second_user_distance == 0 :
        return 0
    result_distance = total_distance / (first_user_distance * second_user_distance)

    return result_distance


def calAllUserCosDistance(all_user_tfidf_vector):
    '''
    计算所有用户的TFIDF向量的余弦cos值-v1.1
    :param all_user_tfidf_vector: 所有用户的位置向量表
    :return: 最终用户的相似性，类型为list[UserClassify]
    '''
    final_result = []
    users = []
    for first_user in all_user_tfidf_vector.keys():
        # if users.count(first_user) != 0:
        # continue
        userclassify = UserClassify()
        userclassify.user = first_user
        similarity = {}
        first_user_location_vector = all_user_tfidf_vector.get(first_user)
        for second_user in all_user_tfidf_vector.keys():
            if first_user == second_user:
                continue
            second_user_location_vector = all_user_tfidf_vector.get(second_user)
            result = calCosDistance(first_user_location_vector, second_user_location_vector)
            if result > 0.2:
                similarity[second_user] = result
                # users.append(second_user)
                # print('%s and %s has similarity for %f' %(first_user, second_user, result))
        userclassify.similarityuser = similarity.copy()
        if len(similarity) > 0:
            final_result.append(userclassify)
            # users.append(first_user)
    return final_result


def printClassifyResult(classifyresult):
    for item in classifyresult:
        print('%s has [%d] similarity user, details are below: ' % (item.user, len(item.similarityuser)))
        for key in item.similarityuser.keys():
            print('similarity with %s are %f' % (key, item.similarityuser.get(key)))


def outputClassifyPklResults(data, dir=r'classifypklresults', filename=r'classifyresult.pkl'):
    '''
    保存用户分类结果数据信息，以二进制形式保存，将结果序列化保存-v1.0
    :param data: 用户分类结果数据信息  list[UserClassify]
    :param dir: 目录名
    :param filename: 保存数据的文件名
    :return:
    '''
    print('Output beginlocation')
    filename = str(len(data)) + '&' + filename
    filename = combileFileName(dir, filename)
    out_file = open(filename, 'wb')
    pickle.dump(data, out_file)
    out_file.close()
    print('Output endlocation')


def outputClassifyTxtResults(data, dir=r'classifytxtresults'):
    '''
    保存用户分类结果数据信息，以文本文件形式保存-v1.0
    :param data: 用户分类结果数据信息  list[UserClassify]
    :param dir: 目录名
    :return:
    '''
    index = 1
    for item in data:
        print('Output begin user similarity %d group' % index)
        filename = str(index) + '&' + str(len(item.similarityuser)) + '&' + item.user + '.txt'
        filename = combileFileName(dir, filename)
        outfile = open(filename, 'w')
        outfile.write(item.user)
        outfile.write('\n')
        for key in item.similarityuser.keys():
            outfile.write(key)
            outfile.write('\n')
        outfile.close()
        index += 1


'''
第二阶段，通过用户停留位置中心求TF-IDF值，并以此建立用户TF-IDF向量，以余弦定理计算用户相似性在以上部分
'''















