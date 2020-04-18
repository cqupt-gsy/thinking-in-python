__author__ = 'Mentu'

from cluster_algorithm import readAllData
from cluster_algorithm import dbscanFindStayArea
from cluster_algorithm import adjustStayArea
from cluster_algorithm import clusterFindStayPoint
from cluster_algorithm import outputTxtResults
from cluster_algorithm import outputPklResults


from cluster_algorithm import buildLocationVector
from cluster_algorithm import buildUserLocationVector
from cluster_algorithm import calAllUsersTFIDF
from cluster_algorithm import buildAllUserTFIDFVector
from cluster_algorithm import calAllUserCosDistance
from cluster_algorithm import printClassifyResult
from cluster_algorithm import outputClassifyPklResults
from cluster_algorithm import outputClassifyTxtResults


from detect_algorithm import loadTxtSimilarityUser
from detect_algorithm import loadUserData
from detect_algorithm import bulidUserTrajectory
from detect_algorithm import seperateUserTrajectory
from detect_algorithm import calDetectParameters
from detect_algorithm import detectTrajectorys
from detect_algorithm import printDectectResults
from detect_algorithm import seperateResult


from pre_read_file import loadStayAreaTxtResults
from pre_read_file import loadStayAreaPklResults
from pre_read_file import loadClassifyData
from pre_read_file import preWalkFileCVS


from draw_figure import drawingStayAreaCenter
from draw_figure import drawingStayAreaDetail
from draw_figure import drawingStayArea
from draw_figure import drawingTrajectory


from time import clock
import os
import re
import gpxpy
import gpxpy.gpx



'''
所有论文还需要做的事情有：
1、写论文两篇（目前重点集中在这阶段）
2、所有算法的结果需要专门学校可视化后，画出更好的结果图（写论文后期可视化的时候考虑）
3、后期需要自己采集数据，然后验证算法的一般性（采集数据应用已经做好，51后开始要人采集数据，后期再进行验证）
4、跑一遍诺基亚的数据集，并且展示结果
以上5月中旬之前完成除采集数据部分的所有
'''

def runDBScanFindStayArea(rundir=r'rawsdata', runfilename=r'0user.txt', dbscanmindist=2700, dbscanminpointper=100,
            dbscanoutdir=r'showresults', dbscanoutfile=r'dbscanresult.txt',
            dbscansavedir=r'saveresults', dbscansavefile='dbscanresult.pkl'):
    '''
    单次运行DBScan算法挖掘用户停留区域-v1.1
    :param rundir: 目录名
    :param runfilename: 用户原始数据文件名
    :param dbscanmindist: dbscan算法的最小距离
    :param dbscanminpointper: dbscan算法的最小邻居节点
    :param dbscanoutdir: 目录名
    :param dbscanoutfile: dbscan算法结果展示输出文件
    :param dbscansavedir: 目录名
    :param dbscansavefile: dbscan算法结果保存输出文件
    :return: 一次算法的运行时间
    '''
    begin = clock()
    result = dbscanFindStayArea(dir=rundir, filename=runfilename, mindist=dbscanmindist, minpointper=dbscanminpointper)
    end_1 = clock()
    stayarea_result = adjustStayArea(result)
    user = runfilename.split('.')[0]
    pres_out = str(dbscanmindist) + '&' + str(dbscanminpointper)
    dbscanoutfile = pres_out + dbscanoutfile
    outputTxtResults(stayarea_result, user=user, dir=dbscanoutdir, filename=dbscanoutfile)
    dbscansavefile = pres_out + dbscansavefile
    outputPklResults(stayarea_result, user=user, dir=dbscansavedir, filename=dbscansavefile)
    end_2 = clock()
    time_consumer_1 = (end_1-begin)/60
    time_consumer_2 = (end_2-begin)/60
    print('algorithm running time: %f' % time_consumer_1)
    print('total running time: %f' % time_consumer_2)
    return [time_consumer_1, time_consumer_2]

def runMutilDBScanFindStayArea(fname=r'0user.txt', dbscandist=800,  dbscanpointper=100,
                  diststep=400, pointstepper=0, loops=8):
    '''
    多次运行DBScan算法挖掘用户停留区域-v1.1
    :param fname: 进行计算的用户数据文件名
    :param dbscandist: dbscan最小距离
    :param dbscanpointper: dbscan最小邻居点数
    :param diststep: dbcsan算法最小距离的自增长步长
    :param pointstepper: dbcsan算法最小邻居节点的自增长步长
    :param loops: 循环次数
    :return: 每次算法运行的时间
    '''
    comsumer = []
    for index in range(loops):
        print('[%d] Begins' % index )
        time_comsumer = runDBScanFindStayArea(runfilename=fname, dbscanmindist=dbscandist, dbscanminpointper=dbscanpointper,)
        dbscandist += diststep
        dbscanpointper += pointstepper
        comsumer.append(time_comsumer)
        print('[%d] Ends' % index )
    return comsumer

def drawingStayAreaFig(user='0user', number=50, dbscanfname=r'dbscanresult.txt',
                   dbscandist=2700,  dbscanpointper=100,
                   minlat_1=31, maxlat_1=32, minlon_1=121, maxlon_1=122,
                   minlat_2=39.0, maxlat_2=41.0, minlon_2=116.0, maxlon_2=117.0,
                    minlat_3=39.8, maxlat_3=40.4, minlon_3=116.25, maxlon_3=116.45):
    '''
    画用户停留区域结果图-v1.1
    :param user: 用户编号
    :param number: 中心点数量
    :param dbscanfname: dbscan结果文件名
    :param dbscandist: dbscan最小距离
    :param dbscanpointper: dbscan最小邻居点数
    :param minlat_1: 最小纬度1
    :param maxlat_1: 最大纬度1
    :param minlon_1: 最小经度1
    :param maxlon_1: 最大经度1
    :param minlat_2: 最小纬度2
    :param maxlat_2: 最大纬度2
    :param minlon_2: 最小经度2
    :param maxlon_2: 最大经度2
    :param minlat_3: 最小纬度3
    :param maxlat_3: 最大纬度3
    :param minlon_3: 最小经度3
    :param maxlon_3: 最大经度3
    :return:
    '''
    pres = user + '&' + str(number) + '&' + str(dbscandist) + '&' + str(dbscanpointper)
    fname = pres + dbscanfname
    resultdata = loadStayAreaTxtResults(fname=fname)
    outfilename = pres + 'stayarea.png'
    drawingStayArea(resultdata, outfilename,
                        minlat_1=minlat_1, maxlat_1=maxlat_1, minlon_1=minlon_1, maxlon_1=maxlon_1,
                        minlat_2=minlat_2, maxlat_2=maxlat_2, minlon_2=minlon_2, maxlon_2=maxlon_2,
                        minlat_3=minlat_3, maxlat_3=maxlat_3, minlon_3=minlon_3, maxlon_3=maxlon_3)

def drawingStayAreaFigCenter(user='0user', number=50, dbscanfname=r'dbscanresult.txt',
                   dbscandist=2700,  dbscanpointper=100):
    '''
    画用户停留区域结果图，只画出聚类中心-v1.1
    :param user: 用户编号
    :param number: 中心点数量
    :param dbscanfname: dbscan结果文件名
    :param dbscandist: dbscan最小距离
    :param dbscanpointper: dbscan最小邻居点数
    :return:
    '''
    pres = user + '&' + str(number) + '&' + str(dbscandist) + '&' + str(dbscanpointper)
    fname = pres + dbscanfname
    resultdata = loadStayAreaTxtResults(fname=fname)
    outfilename = pres + 'stayareacenter.png'
    drawingStayAreaCenter(resultdata, outfilename)

def drawingStayAreaFigDetail(user='0user', number=50, dbscanfname=r'dbscanresult.txt',
                   dbscandist=2700,  dbscanpointper=100, minlat=6.6, maxlat=7.2, minlon=46.5, maxlon=46.6):
    '''
    minlat=6.6, maxlat=7, minlon=46, maxlon=48
    minlat=39.8, maxlat=40.4, minlon=116.25, maxlon=116.45
    画用户停留区域结果图，画出停留区域中心以及其邻居节点-v1.1
    :param user: 用户编号
    :param number: 中心点数量
    :param dbscanfname: dbscan结果文件名
    :param dbscandist: dbscan最小距离
    :param dbscanpointper: dbscan最小邻居点数
    :param minlat: 最小纬度
    :param maxlat: 最大纬度
    :param minlon: 最小经度
    :param maxlon: 最大经度
    :return:
    '''
    pres = user + '&' + str(number) + '&' + str(dbscandist) + '&' + str(dbscanpointper)
    fname = pres + dbscanfname
    resultdata = loadStayAreaTxtResults(fname=fname)
    outfilename = pres + 'stayareadetail.png'
    drawingStayAreaDetail(resultdata, outfilename, minlat=minlat, maxlat=maxlat, minlon=minlon, maxlon=maxlon,
                          title="NUserA's StayArea")


def printTimeConsumer(comsumer):
    '''
    打印程序所有运行时间-v1.1
    :param comsumer: 消耗的时间是个二维数组
    :return:
    '''
    total_time_dbscan = 0.0
    total_time_all = 0.0
    all_number = len(comsumer) + 1
    for content in comsumer:
        total_time_dbscan += content[0]
        total_time_all += content[1]
    avg_time_dbscan = total_time_dbscan/all_number
    avg_time_all = total_time_all/all_number
    print('Total time consumer for dbscan is [%f], avg time is [%f]' % (total_time_dbscan, avg_time_dbscan))
    print('Total time consumer for all is [%f], avg time is [%f]' % (total_time_all, avg_time_all))

def runClusterFindStayPoint(user='0user', number=50, dbscandist=2700, dbscanpointper=100,
               rundir=r'saveresults', runfilename=r'dbscanresult.pkl',
                clusterdist=100, clustertime=1800,
                clusteroutdir=r'showresults', clusteroutfile=r'clusterresult.txt',
                clustersavedir=r'saveresults', clustersavefile='clusterresult.pkl',):
    '''
    单次运行Cluster算法挖掘用户停留位置-v1.1
    :param user: 用户ID
    :param number: DBScan聚类数目
    :param dbscandist: DBScan聚类最短距离参数
    :param dbscanpointper: DBScan聚类最小密度参数
    :param rundir: 源数据目录名
    :param runfilename: 用户原始数据文件名
    :param clusterdist: cluster算法最小聚类
    :param clustertime: cluster算法最小时间间隔
    :param clusteroutdir: cluster结果输出目录名
    :param clusteroutfile: cluster算法结果展示输出文件名
    :param clustersavedir: 结果保存目录名
    :param clustersavefile: cluster算法结果保存输出文件名
    :return: 一次算法的运行时间
    '''
    pres = user + '&' + str(number) + '&' + str(dbscandist) + '&' + str(dbscanpointper)
    runfilename = pres + runfilename
    data = loadStayAreaPklResults(dirs=rundir, fname=runfilename)
    begin = clock()
    staypoint_result = clusterFindStayPoint(data, mindist=clusterdist, mintime=clustertime)
    end_1 = clock()
    pres_out = str(clusterdist) + '&' + str(clustertime)
    clusteroutfile = pres_out + clusteroutfile
    outputTxtResults(staypoint_result, user=user, dir=clusteroutdir, filename=clusteroutfile)
    clustersavefile = pres_out + clustersavefile
    outputPklResults(staypoint_result, user=user, dir=clustersavedir, filename=clustersavefile)
    end_2 = clock()
    time_consumer_1 = (end_1-begin)/60
    time_consumer_2 = (end_2-begin)/60
    print('algorithm running time: %f' % time_consumer_1)
    print('total running time: %f' % time_consumer_2)
    return [time_consumer_1, time_consumer_2]

def runMutilClusterFindStayPoint(user='0user', number=50, dbscandist=2700, dbscanpointper=100,
                    clusterdist=160,  clustertime=1800,
                    diststep=0, timestep=300, loops=13):
    '''
    多次运行Cluster算法挖掘用户停留位置-v1.1
    :param user: 用户ID
    :param number: DBScan聚类数目
    :param dbscandist: DBScan聚类最短距离参数
    :param dbscanpointper: DBScan聚类最小密度参数
    :param clusterdist: cluster算法最小距离
    :param clustertime: cluster算法最小时间间隔
    :param diststep: cluster算法最小距离的自增长步长
    :param timestep: cluster算法最小时间间隔的自增长步长
    :param loops: 循环次数
    :return: 每次算法运行的时间
    '''
    comsumer = []
    for index in range(loops):
        print('[%d] Begins' % index )
        time_comsumer = runClusterFindStayPoint(user=user,number=number, dbscandist=dbscandist, dbscanpointper=dbscanpointper,
                                   clusterdist=clusterdist, clustertime=clustertime)
        clusterdist += diststep
        clustertime += timestep
        comsumer.append(time_comsumer)
        print('[%d] Ends' % index )
    return comsumer

def outputstdlocations(all_user_location_vector, user):
    locations = all_user_location_vector.get(user)
    filename =  user + '&' + str(len(locations)) + '.txt'
    file = open(filename, 'w')
    for location in locations:
        file.write('Center')
        file.write(',')
        file.write(str(location.lat))
        file.write(',')
        file.write(str(location.longti))
        file.write('\n')

def classifyUser():
    #1、加载需要分类的数据，就是所有用户的停留位置中心
    print('begining loadClassifyData......')
    raws_user_staypoint_center = loadClassifyData()#所有用户的位置，没有排除重复的数据
    #2、建立所有用户唯一的中心位置向量列表
    print('begining buildLocationVector......')
    user_final_location_vector = buildLocationVector(raws_user_staypoint_center)#所有用户的位置向量表
    #3、分别建立每个用户的唯一中心位置向量列表
    print('begining buildUserLocationVector......')
    all_user_location_vector = buildUserLocationVector(raws_user_staypoint_center)#删除用户重复后的数据
    outputstdlocations(all_user_location_vector, '0user')#输出删除用户重复后的数据
    outputstdlocations(all_user_location_vector, '12user')#输出删除用户重复后的数据
    outputstdlocations(all_user_location_vector, '4user')#输出删除用户重复后的数据
    outputstdlocations(all_user_location_vector, '52user')#输出删除用户重复后的数据
    outputstdlocations(all_user_location_vector, '5user')#输出删除用户重复后的数据
    outputstdlocations(all_user_location_vector, '112user')#输出删除用户重复后的数据
    outputstdlocations(all_user_location_vector, '78user')#输出删除用户重复后的数据
    # #4、根据每个用户的唯一中心位置向量列表与原始用户停留位置中心计算TF-IDF值
    # print('begining calAllUsersTFIDF......')
    # calAllUsersTFIDF(all_user_location_vector, raws_user_staypoint_center, allusers=82)#计算所有用户的TFIDF值
    # #5、根据每个用户的唯一中心位置向量列表所得的TF-IDF值与所有用户唯一的中心位置向量列表建立每个用户的TF-IDF向量列表
    # print('begining buildAllUserTFIDFVector......')
    # all_user_tfidf_vector = buildAllUserTFIDFVector(all_user_location_vector, user_final_location_vector)#构建所有用的位置向量表
    # #6、根据所有用户的TF-IDF值，计算用户的相似性
    # print('begining calAllUserCosDistance......')
    # resutls = calAllUserCosDistance(all_user_tfidf_vector)#计算所有用户的相似性
    # print('endclassifying......')
    # #7、输出所有用户相似性结果到二进制文件，将结果序列化
    # outputClassifyPklResults(resutls)
    # # 8、输出所有用户相似性结果到文本文件，为异常轨迹检测算法提供用户相似性结果
    # outputClassifyTxtResults(resutls)
    # # 9、打印所有用户相似性结果
    # printClassifyResult(resutls)


def outAbnormalTrajectoryResultsToJs(abnormal_trajectorys):
    for abnormal_trajectory in abnormal_trajectorys:
        out_index = 0
        print("beginning abnormal: %d" %(out_index))
        if len(abnormal_trajectory.nerbors) < 8:
            out_index += 1
            continue
        abnormal = r"abnormal/points-sample-data"
        abnormal = abnormal + str(abnormal_trajectory.tid) + ".js"
        abnormalfile = open(abnormal, 'w')
        abnormalfile.write('var data = { "data": [')
        points = abnormal_trajectory.points.copy()
        for point in points:
            if point == points[0] or point == points[35] or point == points[-1]:
                if point == points[0]:
                    abnormalfile.write('[[')
                else:
                    abnormalfile.write('[')
                abnormalfile.write(str(point.longti))
                abnormalfile.write(',')
                abnormalfile.write(str(point.lat))
                abnormalfile.write(',1')
                if point == points[-1]:
                    abnormalfile.write(']],')
                else:
                    abnormalfile.write('],')
        abnormalfile.write(']};')
        abnormalfile.write('\n')
        abnormalfile.write('var data1 = { "data1": [')
        #输出轨迹邻居点
        nerbors = abnormal_trajectory.nerbors.copy()
        for nerbor in nerbors:
            nerbor_points = nerbor.points.copy()
            for nerbor_point in nerbor_points:
                if nerbor_point == nerbor_points[0] or nerbor_point == nerbor_points[35] or nerbor_point == nerbor_points[-1]:
                    if nerbor_point == nerbor_points[0]:
                        abnormalfile.write('[[')
                    else:
                        abnormalfile.write('[')
                    abnormalfile.write(str(nerbor_point.longti))
                    abnormalfile.write(',')
                    abnormalfile.write(str(nerbor_point.lat))
                    abnormalfile.write(',1')
                    if nerbor_point == nerbor_points[-1]:
                        abnormalfile.write(']],')
                    else:
                        abnormalfile.write('],')
        abnormalfile.write(']}')
        abnormalfile.close()
        out_index += 1

def outNormalTrajectoryResultsToJs(normal_trajectorys):
    out_index = 0
    for normal_trajectory in normal_trajectorys:
        print("beginning normal: %d" %(out_index))
        if len(normal_trajectory.nerbors) < 30:
            out_index += 1
            continue
        normal = r"normal/points-sample-data"
        normal = normal + str(normal_trajectory.tid) + ".js"
        normalfile = open(normal, 'w')
        normalfile.write('var data = { "data": [')
        points = normal_trajectory.points.copy()
        for point in points:
            if point == points[0] or point == points[35] or point == points[-1]:
                if point == points[0]:
                    normalfile.write('[[')
                else:
                    normalfile.write('[')
                normalfile.write(str(point.longti))
                normalfile.write(',')
                normalfile.write(str(point.lat))
                normalfile.write(',1')
                if point == points[-1]:
                    normalfile.write(']],')
                else:
                    normalfile.write('],')
        normalfile.write(']};')
        normalfile.write('\n')
        normalfile.write('var data1 = { "data1": [')
        #输出轨迹邻居点
        nerbors = normal_trajectory.nerbors.copy()
        for nerbor in nerbors:
            nerbor_points = nerbor.points.copy()
            for nerbor_point in nerbor_points:
                if nerbor_point == nerbor_points[0] or nerbor_point == nerbor_points[35] or nerbor_point == nerbor_points[-1]:
                    if nerbor_point == nerbor_points[0]:
                        normalfile.write('[[')
                    else:
                        normalfile.write('[')
                    normalfile.write(str(nerbor_point.longti))
                    normalfile.write(',')
                    normalfile.write(str(nerbor_point.lat))
                    normalfile.write(',1')
                    if nerbor_point == nerbor_points[-1]:
                        normalfile.write(']],')
                    else:
                        normalfile.write('],')
        normalfile.write(']}')
        normalfile.close()
        out_index += 1

def outRawTrajectoryToJs(detected_trajectorys, other_trajectorys):
    detectedfile = open(r'rawtra/points-sample-detected.js', 'w')
    otherfile = open(r'rawtra/points-sample-other.js', 'w')
    print(len(detected_trajectorys))
    print(len(other_trajectorys))
    detectedfile.write('var data = { "data": [')
    otherfile.write('var data1 = { "data1": [')
    for detected_trajectory in detected_trajectorys:
        points = detected_trajectory.points.copy()
        for point in points:
            if point == points[0] or point == points[35] or point == points[-1]:
                if point == points[0]:
                    detectedfile.write('[[')
                else:
                    detectedfile.write('[')
                detectedfile.write(str(point.longti))
                detectedfile.write(',')
                detectedfile.write(str(point.lat))
                detectedfile.write(',1')
                if point == points[-1]:
                    detectedfile.write(']],')
                else:
                    detectedfile.write('],')
    for other_trajectory in other_trajectorys:
        points = other_trajectory.points.copy()
        for point in points:
            if point == points[0] or point == points[35] or point == points[-1]:
                if point == points[0]:
                    otherfile.write('[[')
                else:
                    otherfile.write('[')
                otherfile.write(str(point.longti))
                otherfile.write(',')
                otherfile.write(str(point.lat))
                otherfile.write(',1')
                if point == points[-1]:
                    otherfile.write(']],')
                else:
                    otherfile.write('],')
    detectedfile.write(']}')
    otherfile.write(']}')
    detectedfile.close()
    otherfile.close()

# def outTrajectoryResultsToGPX(abnormal_trajectorys, normal_trajectorys):
#     abnormalfile = open('abnormal.gpx', 'w')
#     normalfile = open('normal.gpx', 'w')
#     abnormal_gpx = gpxpy.gpx.GPX()
#     normal_gpx = gpxpy.gpx.GPX()
#     for abnormal_trajectory in abnormal_trajectorys:
#         #输出轨迹本身的点
#         points = abnormal_trajectory.points.copy()
#         gpx_track = gpxpy.gpx.GPXTrack()
#         abnormal_gpx.tracks.append(gpx_track)
#         gpx_segment = gpxpy.gpx.GPXTrackSegment()
#         gpx_track.segments.append(gpx_segment)
#         gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(points[0].lat, points[0].longti, elevation=492))
#         gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(points[35].lat, points[35].longti, elevation=492))
#         gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(points[60].lat, points[60].longti, elevation=492))
#         #输出轨迹邻居点
#         nerbors = abnormal_trajectory.nerbors.copy()
#         for nerbor in nerbors:
#             nerbor_points = nerbor.points.copy()
#             gpx_track_nerbor = gpxpy.gpx.GPXTrack()
#             abnormal_gpx.tracks.append(gpx_track_nerbor)
#             gpx_segment_nerbor = gpxpy.gpx.GPXTrackSegment()
#             gpx_track_nerbor.segments.append(gpx_segment_nerbor)
#             gpx_segment_nerbor.points.append(gpxpy.gpx.GPXTrackPoint(nerbor_points[0].lat, nerbor_points[0].longti, elevation=492))
#             gpx_segment_nerbor.points.append(gpxpy.gpx.GPXTrackPoint(nerbor_points[35].lat, nerbor_points[35].longti, elevation=492))
#             gpx_segment_nerbor.points.append(gpxpy.gpx.GPXTrackPoint(nerbor_points[60].lat, nerbor_points[60].longti, elevation=492))
#
#     # nerbor_num = 0
#     for normal_trajectory in normal_trajectorys:
#         #输出轨迹本身的点
#         # nerbor_num += 1
#         # if nerbor_num > 20:
#         #     break
#         points = normal_trajectory.points.copy()
#         gpx_track = gpxpy.gpx.GPXTrack()
#         normal_gpx.tracks.append(gpx_track)
#         gpx_segment = gpxpy.gpx.GPXTrackSegment()
#         gpx_track.segments.append(gpx_segment)
#         gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(points[0].lat, points[0].longti, elevation=492))
#         gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(points[35].lat, points[35].longti, elevation=492))
#         gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(points[60].lat, points[60].longti, elevation=492))
#         #输出轨迹邻居点
#         nerbors = normal_trajectory.nerbors.copy()
#         for nerbor in nerbors:
#             nerbor_points = nerbor.points.copy()
#             gpx_track_nerbor = gpxpy.gpx.GPXTrack()
#             normal_gpx.tracks.append(gpx_track_nerbor)
#             gpx_segment_nerbor = gpxpy.gpx.GPXTrackSegment()
#             gpx_track_nerbor.segments.append(gpx_segment_nerbor)
#             gpx_segment_nerbor.points.append(gpxpy.gpx.GPXTrackPoint(nerbor_points[0].lat, nerbor_points[0].longti, elevation=492))
#             gpx_segment_nerbor.points.append(gpxpy.gpx.GPXTrackPoint(nerbor_points[35].lat, nerbor_points[35].longti, elevation=492))
#             gpx_segment_nerbor.points.append(gpxpy.gpx.GPXTrackPoint(nerbor_points[60].lat, nerbor_points[60].longti, elevation=492))
#     abnormalfile.write(abnormal_gpx.to_xml())
#     normalfile.write(normal_gpx.to_xml())
#     abnormalfile.close()
#     normalfile.close()

'''
DBScan算法调试步骤
'''
#1、产生原始数据
# readAllData(number=181)
# preWalkFileCVS()

#2-1、多次运行DBScan算法，调整参数
# comsumer = runMutilDBScanFindStayArea(fname='0user.txt',loops=8, dbscandist=800, dbscanpointper=100, diststep=400, pointstepper=0)
# printTimeConsumer(comsumer)
#2-2、单独运行DBScan算法
# number = 141
# fname = '0user.txt'
# print('Begin %s' % fname)
# runDBScanFindStayArea(runfilename=fname, dbscanmindist=2400, dbscanminpointper=100)
#2-3 通过DBScan算法计算其他用户的聚类中心
# time_consumer = []
# for (thisDir, dirsHere, filesHere) in os.walk(r'rawsdata'):
#     for files in filesHere:
#         print('Begin %s' % files)
#         consumer = runDBScanFindStayArea(rundir='rawsdata', runfilename=files, dbscanmindist=2400, dbscanminpointper=100)
#         time_consumer.append(consumer)
# printTimeConsumer(time_consumer)


#3、画图程序，画出结果
# user = 'user'
# num = 1
# dbscan_dis = 2400
# dbscan_poit =100
# drawingStayAreaFig(user=user, number=num, dbscandist=dbscan_dis, dbscanpointper=dbscan_poit)
# drawingStayAreaFigCenter(number=num, dbscandist=dbscan_dis,  dbscanpointper=dbscan_poit)
# drawingStayAreaFigDetail(user=user, number=num, dbscandist=dbscan_dis,  dbscanpointper=dbscan_poit)
# for (thisDir, dirsHere, filesHere) in os.walk(r'showresults'):
#     for files in filesHere:
#         if re.match(r'(.*)dbscanresult.txt', files):
#             print('Begin %s' % files)
#             content = files.split('&')
#             drawingStayAreaFig(user=content[0], number=int(content[1]), dbscandist=dbscan_dis, dbscanpointper=dbscan_poit)


'''
Cluster组合聚类算法调试步骤
'''
#1-1、多次运行合并算法，调整参数
# comsure = runMutilClusterFindStayPoint(user=user, number=num, dbscandist=dbscan_dis,  dbscanpointper=dbscan_poit)
# printTimeConsumer(comsure)
#1-2、单次运行合并算法
# runClusterFindStayPoint(user= user, number=num, dbscandist=dbscan_dis,  dbscanpointper=dbscan_poit, clusterdist=150,  clustertime=1800)
#1-3、通过Cluster算法计算其他用户的停留点
# for (thisDir, dirsHere, filesHere) in os.walk(r'saveresults'):
#     for files in filesHere:
#         if files.endswith('dbsacnresult.pkl'):
#             print('Begin %s' % files)
#             data = loadStayAreaPklResults(fname=files)
#             begin = clock()
#             result = clusterFindStayPoint(data, mindist=160, mintime=1800)
#             end_1 = clock()
#             user = files.split('&')[0]
#             clusteroutfile = '150&1800clusterresult.txt'
#             outputTxtResults(result, user=user,  filename=clusteroutfile)
#             clustersavefile = '150&1800clusterresult.pkl'
#             outputPklResults(result, user=user, filename=clustersavefile)
#             end_2 = clock()
#             time_consumer_1 = (end_1-begin)/60
#             time_consumer_2 = (end_2-begin)/60
#             print('algorithm running time: %f' % time_consumer_1)
#             print('total running time: %f' % time_consumer_2)

'''
第一阶段，DBSCAN聚类算法、Cluster组合聚类算法在以上部分
'''

# 将提留区域中心点输出
# data = loadStayAreaPklResults(fname='112user&13&2400&100dbsacnresult.pkl')
# filename = '0user&' + str(len(data)) + '.txt'
# file = open(filename, 'w')
# for sa in data:
#     file.write('Center')
#     file.write(',')
#     file.write(str(sa.centerlat))
#     file.write(',')
#     file.write(str(sa.centerlon))
#     file.write('\n')

'''
分类算法调试步骤
'''
# classifyUser()


# '''
# 第二阶段，计算用户的相似性算法在以上部分
# '''
#
# '''
# 异常轨迹检测算法调试步骤
# '''
# #1、加载所有相似用户
# print('begin loadTxtSimilarityUser......')
# similarity_user = loadTxtSimilarityUser(filename='0&4&0user.txt')
# #2、分组加载相似用户的所有原始数据
# print('begin loadUserData......')
# one_couple_users = loadUserData(similarity_user)
# #3、挖掘一组相似用户的轨迹
# print('begin bulidUserTrajectory......')
# user_trajectory = bulidUserTrajectory(one_couple_users, minpoint=61, mintime=280, maxtime=305)
#
# #4、分离检测轨迹
# print('begin seperateUserTrajectory......')
# detected_trajectory, others_trajectory = seperateUserTrajectory(user_trajectory, filename='0&4&0user.txt')
# # outRawTrajectoryToJs(detected_trajectory, others_trajectory)
#
# #5、计算对应时间间隔内轨迹点的邻居点以及轨迹的邻居轨迹
# # begin = clock()
# print('begin calDetectParameters......')
# # detect_index=[0, 6, 11, 12, 13, 17, 35, 36, 38, 41, 43, 44, 46, 48, 60]
# calDetectParameters(detected_trajectory, others_trajectory)
# #6、检测用户的轨迹多少是异常的
# minnerbors = 10
# detectTrajectorys(detected_trajectory, minnerbors=minnerbors)
# # end = clock()
# # time_consumer = (end-begin)/60
# # print('algorithm running time: %f' % time_consumer)
#
# trajectory_number = 0
# for key in user_trajectory.keys():
#     trajectory_number += len(user_trajectory.get(key))
# print('total %d trajectorys' % trajectory_number)
# printDectectResults(detected_trajectory)
#
#
#
# #7、可视化检测结果
# normal_trajectorys , abnormal_trajectorys = seperateResult(detected_trajectory)
# outAbnormalTrajectoryResultsToJs(abnormal_trajectorys)
# outNormalTrajectoryResultsToJs(normal_trajectorys)
# outTrajectoryResultsToGPX(abnormal_trajectorys, normal_trajectorys)

# drawingTrajectory(normal_trajectorys, 'normal.png', 'normal')
# drawingTrajectory(abnormal_trajectorys, 'abnormal.png', 'abnormal')







