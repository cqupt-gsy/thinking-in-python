__author__ = 'Mentu'

'''
该文件的图片仅仅作为测试使用
实际画图将数据导出后用谷歌地球展示
'''
import matplotlib
import random
matplotlib.use('Agg')
import gc


from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from pre_read_file import combileFileName


#PIL模块没有python3.4版本的，等有了以后安装再来尝试自己画图
# 115.7°E-117.4°E,39.4°N-41.6°N
#ax=None, lllat=39.98, urlat=39.99, lllon=116.29, urlon=116.31
# plt.axes([39.4, 41.2, 115.7, 117.4])

simbol = ['.', 'o', 'v', '^', '<', '>', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd']

def basicMap(ax=None, lllat=39.98, urlat=39.99, lllon=116.29, urlon=116.31):#finalversion
    m = Basemap(width=120000,height=9000,projection='stere', resolution='f',
                lat_0=(urlat+lllat)/2,lon_0=(lllon+urlon)/2,
                llcrnrlon=lllon, llcrnrlat=lllat, urcrnrlon=urlon, urcrnrlat=urlat)
    m.drawcoastlines()
    m.drawstates()
    m.drawcounties()
    m.fillcontinents()
    #m.etopo()
    return m

def drawingResultTest(inputdata):#finalversion
    map = basicMap()
    for item in inputdata:
        x, y = map(item.centerlon,item.centerlat)
        map.plot(x,y,'k.',alpha=0.9)
        nerborhood = item.nerborhoods
        for content in nerborhood:
             x, y = map(content.longti, content.lat)
             map.plot(x,y,'k.',alpha=0.2)
    plt.title('cluster result')
    plt.show()

def drawingStayArea(data, fname, dir='imgresults',
                  title_1='Result for All StayArea Center(a)', title_2='Leftup Part(b)',
                  title_3='Rightdown Part(c_1)', title_4='Rightdown Part(c_2)',
                  minlat_1=31, maxlat_1=32, minlon_1=121, maxlon_1=122,
                  minlat_2=39, maxlat_2=41, minlon_2=116, maxlon_2=117,
                  minlat_3=39.8, maxlat_3=40.4, minlon_3=116.25, maxlon_3=116.45):
    '''
    画用户停留区域结果图，将中心点，详细点全部画于一张图上-v1.1
    :param data: list[type,lat,longti,time]类型
    :param fname: 保存结果文件名
    :param dir: 保存结果目录名
    :param title_1: 标题1
    :param title_2: 标题2
    :param title_3: 标题3
    :param title_4: 标题4
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
    gc.collect()
    fig = plt.figure()
    xlable = 'Latitude'
    ylable = 'Lontitude'
    skip_3 = 0
    skip_4 = 0
    ax_1 = fig.add_subplot(221, title=title_1, xlabel=xlable, ylabel=ylable, autoscale_on=True)
    ax_2 = fig.add_subplot(222, title=title_2, xlabel=xlable, ylabel=ylable, autoscale_on=True)
    ax_3 = fig.add_subplot(223, title=title_3, xlabel=xlable, ylabel=ylable, autoscale_on=True)
    ax_4 = fig.add_subplot(224, title=title_4, xlabel=xlable, ylabel=ylable, autoscale_on=True)
    loop = 1
    color_index = 0
    ret_color = []
    all_num = len(data)
    if all_num >= 300000:
        skip_num = 6
    elif 300000 > all_num >= 200000:
        skip_num = 5
    elif 200000 > all_num >= 100000:
        skip_num = 4
    elif 100000 > all_num >= 70000:
        skip_num = 2
    else:
        skip_num = 1
    for line in data:
        print('Drawing detail point [%d], left [%d]'  % (loop, len(data)-loop))
        content = line.rstrip().split(',')
        lat = float(content[1])
        lon = float(content[2])
        if content[0] == 'Center':
            color_r = random.uniform(0,1)
            color_b = random.uniform(0,1)
            color_g = random.uniform(0,1)
            ret_color.append([color_r, color_g, color_b])
            color_index += 1
            ax_1.plot(lat,lon, 'o', color=(color_r, color_g, color_b))
            if (maxlat_1 >= lat >= minlat_1) and (maxlon_1 >= lon >= minlon_1):
                ax_2.plot(lat,lon, '.', color=(color_r, color_g, color_b))
                ax_2.text(lat,lon, 'C'+str(color_index))
            elif (maxlat_2 >= lat >= minlat_2) and (maxlon_2 >= lon >= minlon_2):
                skip_3 = 0
                ax_3.plot(lat,lon, '.', color=(color_r, color_g, color_b))
                ax_3.text(lat,lon, 'C'+str(color_index))
            if (maxlat_3 >= lat >= minlat_3) and (maxlon_3 >= lon >= minlon_3):
                skip_4 = 0
                ax_4.plot(lat,lon, '.', color=(color_r, color_g, color_b))
                ax_4.text(lat,lon, 'C'+str(color_index))
        else:
            if (maxlat_1 >= lat >= minlat_1) and (maxlon_1 >= lon >= minlon_1):
                ax_2.plot(lat,lon, '.',
                          color=(ret_color[color_index-1][0], ret_color[color_index-1][1], ret_color[color_index-1][2]))
            elif (maxlat_2 >= lat >= minlat_2) and (maxlon_2 >= lon >= minlon_2) and skip_3 % skip_num ==0:
                #and skip_3 % 2 ==0
                ax_3.plot(lat,lon, '.',
                          color=(ret_color[color_index-1][0], ret_color[color_index-1][1], ret_color[color_index-1][2]))

            if (maxlat_3 >= lat >= minlat_3) and (maxlon_3 >= lon >= minlon_3) and skip_4 % skip_num ==0:
                #and skip_4 % 2 ==0
                ax_4.plot(lat,lon, '.',
                          color=(ret_color[color_index-1][0], ret_color[color_index-1][1], ret_color[color_index-1][2]))
            skip_3 += 1
            skip_4 += 1
        loop += 1
    ax_1.grid(True)
    ax_2.grid(True)
    ax_3.grid(True)
    ax_4.grid(True)
    fname = combileFileName(dirs=dir, filename=fname)
    fig.tight_layout(pad=1.1)
    fig.set_figheight(6.5)
    fig.set_figwidth(12)
    fig.savefig(fname)
    fig.clf()
    print('Drawing end')

def drawingStayAreaCenter(data, fname, dir='imgresults', title='Result for Finding StayArea'):
    '''
    画用户停留区域结果图，只画出停留区域中心点-v1.1
    :param data: 结果数据集 list[type, lat,longti,time]类型
    :param fname: 保存图片文件名
    :param dir: 文件保存目录名
    :param title: 图的标题
    :return:
    '''
    loop = 1
    for line in data:
        print('Drawing center point [%d], left [%d]' % (loop, len(data)-loop))
        content = line.rstrip().split(',')
        if content[0] == 'Center':
            color_r = random.uniform(0,1)
            color_b = random.uniform(0,1)
            color_g = random.uniform(0,1)
            plt.plot(float(content[1]),float(content[2]), '.', color=(color_r, color_g, color_b), linewidth=0.5)
        loop += 1
    plt.xlabel('Latitude')
    plt.ylabel('Lontitude')
    plt.title(title)
    plt.grid(True)
    fname = combileFileName(dirs=dir, filename=fname)
    plt.savefig(fname)
    plt.clf()
    print('Drawing end')

def drawingStayAreaDetail(data, fname, dir='imgresults', minlat=31, maxlat=32, minlon=121, maxlon=122,
                        title='StayArea Result for Finding Staypoint'):
    '''
    画用户停留区域结果图，画出某范围内的停留区域中心点以及其邻居节点的详细画图-v1.1
    :param data: 结果数据集 list[type, lat,longti,time]类型
    :param fname: 保存图片文件名
    :param dir: 文件保存目录名
    :param minlat: 最小纬度
    :param maxlat: 最大纬度
    :param minlon: 最小经度
    :param maxlon: 最大经度
    :param title: 图的标题
    :return:
    '''
    loop = 1
    color_index = 0
    ret_color = []
    skip = 0
    for line in data:
        print('Drawing detail point [%d], left [%d], minlat [%d]'  % (loop, len(data)-loop, minlat))
        content = line.rstrip().split(',')
        lat = float(content[1])
        lon = float(content[2])
        if (maxlat >= lat >=minlat) and (maxlon >= lon >= minlon):
            if content[0] == 'Center':
                color_r = random.uniform(0,1)
                color_b = random.uniform(0,1)
                color_g = random.uniform(0,1)
                ret_color.append([color_r, color_g, color_b])
                color_index += 1
                plt.plot(lat,lon, '.', color=(color_r, color_g, color_b))
                plt.text(lat,lon, 'C'+str(color_index))
            else:
                if skip % 2 == 0:
                    plt.plot(lat,lon, '.',
                         color=(ret_color[color_index-1][0], ret_color[color_index-1][1], ret_color[color_index-1][2]))
        loop += 1
        skip += 1
    plt.xlabel('Latitude/°')
    plt.ylabel('Lontitude/°')
    plt.title(title)
    plt.grid(True)
    fname = combileFileName(dirs=dir, filename=fname)
    plt.savefig(fname)
    plt.clf()
    print('Drawing end')

'''
第一阶段，DBSCAN聚类算法、Cluster组合聚类算法在以上部分
'''

def drawingTrajectory(trajectorys, fname, type, dir='imgresults',
                  title_1='All normal trajectory(a)', title_2='Leftup Part(b)',
                  title_3='Rightdown Part(c_1)', title_4='Rightdown Part(c_2)',
                  minlat_1=31, maxlat_1=32, minlon_1=121, maxlon_1=122,
                  minlat_2=39, maxlat_2=41, minlon_2=116, maxlon_2=117,
                  minlat_3=39.8, maxlat_3=40.4, minlon_3=116.25, maxlon_3=116.45):
    '''
    画用户停留区域结果图，将中心点，详细点全部画于一张图上-v1.1
    :param trajectorys: list[type,lat,longti,time]类型
    :param fname: 保存结果文件名
    :param type: 轨迹类型，正常和异常
    :param dir: 保存结果目录名
    :param title_1: 标题1
    :param title_2: 标题2
    :param title_3: 标题3
    :param title_4: 标题4
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
    gc.collect()
    fig = plt.figure()
    xlable = 'Latitude'
    ylable = 'Lontitude'
    ax_1 = fig.add_subplot(111, title=title_1, xlabel=xlable, ylabel=ylable, autoscale_on=True)
    loop = 1
    for trajectory in trajectorys:
        # if loop == 1:
        minlat_1 = trajectory.beginlocation.lat
        minlon_1 = trajectory.beginlocation.longti
        maxlat_1 = trajectory.endlocation.lat
        maxlon_1 = trajectory.endlocation.longti

        print('Drawing %s trajectory [%d], left [%d]'  % (type, loop, len(trajectorys)-loop))
        for point in trajectory.points:
            ax_1.plot(point.lat, point.longti, 'r.', alpha=0.2)
            # ax_1.text(point.lat, point.longti, str(trajectory.tid))
        nerbors = trajectory.nerbors.copy()
        for nerbors_trajectory in nerbors:
            for point in nerbors_trajectory.points:
                if (maxlat_1 >= point.lat >= minlat_1) and (maxlon_1 >= point.longti >= minlon_1 ):
                    ax_1.plot(point.lat, point.longti, 'k.')
        loop += 1
    ax_1.grid(True)
    fname = combileFileName(dirs=dir, filename=fname)
    # fig.tight_layout(pad=1.1)
    # fig.set_figheight(6.5)
    # fig.set_figwidth(12)
    fig.savefig(fname)
    fig.clf()
    print('Drawing end')