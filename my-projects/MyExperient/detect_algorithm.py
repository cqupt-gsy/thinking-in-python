__author__ = 'Mentu'

from pre_read_file import loadClassifyPklResult
from pre_read_file import combileFileName
from pre_read_file import str_formate

from cluster_algorithm import calDistance


from entity import TLocation
from entity import Trajectory


from datetime import datetime


def loadPklSimilarityUser(dir=r'classifypklresults', filename=r'62&classifyresult.pkl'):
    '''
    加载用户分类结果，用轨迹挖掘提供用户信息
    :param dir: 目录名
    :param filename: 文件名
    :return: 将相似用户按组划分，类型为dict{id, list[user]}
    '''
    results = loadClassifyPklResult(dir=dir, filename=filename)
    similarity_user = {}
    for index in range(len(results)):
        users = []
        users.append(results[index].user)
        for key in results[index].similarityuser.keys():
            users.append(key)
        similarity_user[index+1] = users
    return similarity_user

def loadTxtSimilarityUser(dir=r'classifytxtresults', filename=r'10&8&40user.txt'):
    '''
    加载用户分类结果，用轨迹挖掘提供用户信息
    :param dir: 目录名
    :param filename: 文件名
    :return: 将相似用户按组划分，类型为list[user]
    '''
    filename = combileFileName(dirs=dir, filename=filename)
    similarity_user = []
    for line in open(filename):
        if line != '':
            similarity_user.append(line.rstrip())
    return similarity_user

def loadUserData(similarity_user, dirs=r'rawsdata'):
    '''
    加载一组相似用户的地理位置数据
    :param similarity_user: 一组相似用户类型为：list[user]
    :param dirs: 原始文件目录名
    :return: 加载完一组相似用户地理位置数据类型为：dict{'user':list[TLocation]}
    '''
    user_location = {}
    for item in similarity_user:
        filename = item + '.txt'
        print('begins %s' % filename)
        filename = combileFileName(dirs, filename)
        locations = []
        for line in open(filename):
            content = line.rstrip().split(',')
            tlocation = TLocation()
            tlocation.lat = float(content[0])
            tlocation.longti = float(content[1])
            tlocation.timer = datetime.strptime(content[2], str_formate)
            locations.append(tlocation)
        user_location[item] = locations.copy()
    return user_location

def bulidUserTrajectory(user_location, minpoint=24, mintime=280, maxtime=305):
    '''
    挖掘一组相似用户的移动轨迹
    :param user_location: 一组相似用户的地理位置数据类型为: dict{'user', list[TLocation]}
    :param minpoint: 最小点数，由于数据是每隔5秒采集一次，因此一分钟是12个点并且要加上初始点1个
    :param mintime: 最小时间间隔，单位是秒
    :return: 一组相似用户的移动轨迹类型为: dict{'user', list[Trajectory]}
    '''
    user_trajectory = {}
    for key in user_location.keys():
        print('begins %s' % key)
        locations = user_location.get(key)
        trajectorys = []
        temp_points = []
        tid = 1
        for location in locations:
            temp_points.append(location)
            if len(temp_points) == minpoint:
                begins = temp_points[0]
                ends = temp_points[minpoint-1]
                timedel = ends.timer - begins.timer
                if maxtime>= timedel.seconds >= mintime:
                    trajectory = Trajectory()
                    trajectory.tid = tid
                    trajectory.belongs = key
                    trajectory.beginlocation = begins
                    trajectory.endlocation = ends
                    trajectory.points = temp_points.copy()
                    trajectorys.append(trajectory)
                    tid += 1
                temp_points = []
        user_trajectory[key] = trajectorys
    return user_trajectory

def seperateUserTrajectory(user_trajectory, dir=r'classifytxtresults', filename=r'10&8&40user.txt'):
    '''
    将用户轨迹分离，分为被检测用户的轨迹以及其他用户的轨迹
    :param user_trajectory: 一组相似用户的所有轨迹类型为：dict{'user', list[Trajectory]}
    :param dir: 原始相似用户保存的文件目录名
    :param filename: 原始相似用户保存的文件名，文件的第一条用户即为待检测的用户
    :return: 被检测用户的轨迹列表类型为：list[Trajectory]和其他用户的轨迹列表类型为：list[Trajectory]
    '''
    filename = combileFileName(dirs=dir, filename=filename)
    input_file = open(filename)
    detected_user = input_file.readline().rstrip()
    input_file.close()
    detected_trajectorys = []
    others_trajectorys = []
    for key in user_trajectory.keys():
        if key == detected_user:
            trajectorys = user_trajectory.get(key).copy()
            for trajectory in trajectorys:
                detected_trajectorys.append(trajectory)
        else:
            trajectorys = user_trajectory.get(key).copy()
            for trajectory in trajectorys:
                others_trajectorys.append(trajectory)
    return detected_trajectorys, others_trajectorys

def calDetectParameters(detected_trajectorys, others_trajectorys, mindist=20, detect_index=[0, 11, 23, 35, 47, 60]):
    '''
    计算对应时间间隔内轨迹点的邻居点以及寻找和轨迹有关联的其他轨迹
    :param detected_trajectorys: 待检测用户的所有轨迹类型为：list[Trajectory]
    :param others_trajectorys: 其他相似用户的多有轨迹类型为：list[Trajectory]
    :param mindist: 邻居点的最小距离间隔
    :return: 由于轨迹中保存的是对象，所以无需返回结果，内容在内存中自动进行了更新
    '''
    for detected_trajectory in detected_trajectorys:
        print('%s, the %d-th trajectory begins, left %d' %(detected_trajectory.belongs, detected_trajectory.tid, len(detected_trajectorys)-detected_trajectory.tid))
        for index in detect_index:
            detect_point = detected_trajectory.points[index]
            #开始从遍历其他用户的所有轨迹
            for others_trajectory in others_trajectorys:
                other_point = others_trajectory.points[index]
                #计算相应时间间隔所有轨迹中的选中点的聚类，也就是计算邻居点
                dist = calDistance(detect_point, other_point)
                begin = False
                end = False
                middle = False
                #判断轨迹点的邻居点
                if dist <= mindist and index == 0:
                    detected_trajectory.beginlocation.nerbornumbers += 1
                    detected_trajectory.beginlocation.nerbortrajectory.append(others_trajectory.belongs + ',' + str(others_trajectory.tid))
                    begin = True
                elif dist <= mindist and index == 35:
                    detected_trajectory.points[index].nerbornumbers += 1
                    middle = True
                elif dist <= mindist and index == 60:
                    detected_trajectory.endlocation.nerbornumbers += 1
                    detected_trajectory.endlocation.nerbortrajectory.append(others_trajectory.belongs + ',' + str(others_trajectory.tid))
                    end = True
                elif dist <= mindist:
                    detected_trajectory.points[index].nerbornumbers += 1
                if begin and end or middle and others_trajectory not in detected_trajectory.nerbors:
                    print("%d has been added!" %(others_trajectory.tid))
                    detected_trajectory.nerbors.append(others_trajectory)
            print("end index %d: **************************%d********************" %(index, len(detected_trajectory.nerbors)))

def detectTrajectorys(detected_trajectorys, minnerbors=100, minnormalpoint=3, detect_index=[0, 11, 23, 35, 47, 60]):
    for detected_trajectory in detected_trajectorys:
        #检测该轨迹中正常点的数量
        for index in detect_index:
            if detected_trajectory.points[index].nerbornumbers >= minnerbors:
                detected_trajectory.normalpoint += 1
            else:
                detected_trajectory.points[index].status = 1
        #首先判断正常点的数量
        if detected_trajectory.normalpoint <= minnormalpoint:
            detected_trajectory.status = 1
        #其次判断开始结尾是否方向相同
        else:
            issamedirection = False
            hasfound = False
            beginsnerbors = detected_trajectory.beginlocation.nerbortrajectory.copy()
            endsnerbors = detected_trajectory.endlocation.nerbortrajectory.copy()
            for first_item in beginsnerbors:
                for second_item in endsnerbors:
                    if first_item == second_item:
                        issamedirection = True
                        hasfound = True
                        break
                if hasfound:
                    break
            if not issamedirection:
                detected_trajectory.status = 1
            else:
                detected_trajectory.status = 0
        # break

def printDectectResults(detected_trajectorys):
    '''
    打印轨迹检测算法的结果
    :param detected_trajectorys: 待检测用户的所有轨迹类型为：list[Trajectory]
    :return:
    '''
    abnormal_number = 0
    normal_number = 0
    print('There are %d trajectorys in this user' % len(detected_trajectorys))
    for detected_trajectory in detected_trajectorys:
        if detected_trajectory.status == 0:
            normal_number += 1
        else:
            abnormal_number += 1
            # print('%s has the %d-th trajectory is abnormal.' %(detected_trajectory.belongs, detected_trajectory.tid))
    print('The normal trajectorys are %d' % normal_number)
    print('The abnormal trajectorys are %d' % abnormal_number)

def seperateResult(detected_trajectorys):
    '''
    分离待检测用户的正常轨迹与异常轨迹
    :param detected_trajectorys: 待检测用户的所有轨迹类型为：list[Trajectory]
    :return: 正常轨迹类型为：list[Trajectory]，异常轨迹类型为：list[Trajectory]
    '''
    normal_trajectorys = []
    abnormal_trajecotys = []
    for detected_trajectory in detected_trajectorys:
        if detected_trajectory.status == 0:
            normal_trajectorys.append(detected_trajectory)
        else:
            abnormal_trajecotys.append(detected_trajectory)
    return normal_trajectorys, abnormal_trajecotys








