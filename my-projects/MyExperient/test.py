__author__ = 'Mentu'


import matplotlib
import random
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from pre_read_file import combileFileName


#画原始数据的分布
def drawingStayAreaCenter(data, fname, dir='imgresults', title='MSUserA Rawdata Distribute',
                          minlat_2=39, maxlat_2=41, minlon_2=116, maxlon_2=117):
    '''
    minlat_2=6.6, maxlat_2=7, minlon_2=46, maxlon_2=48
    minlat_2=39, maxlat_2=41, minlon_2=116, maxlon_2=117
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
        lat = float(content[0])
        lon = float(content[1])
        if (maxlat_2 >= lat >= minlat_2) and (maxlon_2 >= lon >= minlon_2):
            color_r = random.uniform(0,1)
            color_b = random.uniform(0,1)
            color_g = random.uniform(0,1)
            plt.plot(lat, lon, '.', color=(color_r, color_g, color_b), linewidth=0.5)
        loop += 1
    plt.xlabel('Latitude/°')
    plt.ylabel('Lontitude/°')
    plt.title(title)
    plt.grid(True)
    fname = combileFileName(dirs=dir, filename=fname)
    plt.savefig(fname)
    plt.clf()
    print('Drawing end')


def outputRawdataforShowing():
    skipnum = 0
    content = []
    # outfile = r'rawsdata\out.txt'
    # file = open(outfile, 'w')
    for line in open(r'rawsdata\0user.txt'):
        if skipnum % 2 == 0:
            content.append(line)
            # file.write(line)
            # skipnum = 1
        skipnum += 1
    # file.close()
    return content

# data = outputRawdataforShowing()
# drawingStayAreaCenter(data, r'MSUserA.png')

# first = []
# second = []
# for line in open('112user&14.txt'):
#     content = line.rstrip().split(',')
#     first.append(content[1]+ ',' + content[2])
# for line in open('52user&45.txt'):
#     content = line.rstrip().split(',')
#     second.append(content[1]+ ',' + content[2])
#
# for compare in first:
#     real = compare.split(',')
#     for compared in second:
#         sreal = compared.split(',')
#         if real[0]==sreal[0] and real[1] == sreal[1]:
#             print('hello')







# def emergency():
#     '''
#     紧急救援函数，将dbscanresult.txt转换成dbscanresult.pkl
#     :return:
#     '''
#     for (thisDir, dirsHere, filesHere) in os.walk(r'showresults'):
#         for files in filesHere:
#             print('Begin %s' % files)
#             content = files.split('&')
#             infile = 'showresults\\' +files
#             list_stayarea = []
#             list_content = []
#             begin = end = count = 0
#             for line in open(infile):
#                 list_content.append(line)
#                 line_content = line.rstrip().split(',')
#                 if line_content[0] == 'Center':
#                     end = count
#                     count += 1
#                 else:
#                     count += 1
#                 if begin != end:
#                     stayarea = StayArea()
#                     nerborhoods = []
#                     temp_end = len(list_content)-1
#                     for index in range(temp_end):
#                         list_temp = list_content[index].rstrip().split(',')
#                         if index == 0:
#                             stayarea.centerlat = float(list_temp[1])
#                             stayarea.centerlon = float(list_temp[2])
#                         else:
#                             location = Location()
#                             location.lat = float(list_temp[1])
#                             location.longti = float(list_temp[2])
#                             location.timer = datetime.strptime(list_temp[3], str_formate)
#                             nerborhoods.append(location)
#                     stayarea.nerborhoods = nerborhoods.copy()
#                     list_stayarea.append(stayarea)
#                     for remove_index in range(temp_end):
#                         list_content.remove(list_content[0])
#                     begin = end
#             if len(list_content) > 1:
#                 stayarea = StayArea()
#                 nerborhoods = []
#                 temp_end = len(list_content)
#                 for index in range(temp_end):
#                     list_temp = list_content[index].rstrip().split(',')
#                     if index == 0:
#                         stayarea.centerlat = float(list_temp[1])
#                         stayarea.centerlon = float(list_temp[2])
#                     else:
#                         location = Location()
#                         location.lat = float(list_temp[1])
#                         location.longti = float(list_temp[2])
#                         location.timer = datetime.strptime(list_temp[3], str_formate)
#                         nerborhoods.append(location)
#                 stayarea.nerborhoods = nerborhoods.copy()
#                 list_stayarea.append(stayarea)
#             number = 0
#             for i in range(len(list_stayarea)):
#                 number += len(list_stayarea[i].nerborhoods)
#                 number += 1
#             outfile = 'saveresults\\'+ content[0] + '&' + str(len(list_stayarea)) + '&' + content[2] + '&' + '100dbscanresult.pkl'
#             print('%s has %f points', (infile, number))
#             out_pkl = open(outfile, 'wb')
#             pickle.dump(list_stayarea, out_pkl)
#             out_pkl.close()
# emergency()

