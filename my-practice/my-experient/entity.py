__author__ = 'Mentu'

class Location:
    '''
    地理位置类
    '''
    def __init__(self, lat=0, longti=0, timer=0, tfidf=0):
        """
        :param lat: 纬度 float
        :param longti: 经度 float
        :param timer: 记录时刻 datetime
        :param tfidf: 位置的TF-IDF值
        :return:
        """
        self._lat=lat
        self._longti=longti
        self._timer=timer
        self._tfidf=tfidf

    @property
    def lat(self):
        return self._lat

    @lat.setter
    def lat(self, value):
        self._lat=value

    @property
    def longti(self):
        return self._longti

    @longti.setter
    def longti(self, value):
        self._longti=value

    @property
    def timer(self):
        return self._timer

    @timer.setter
    def timer(self, value):
        self._timer=value

    @property
    def tfidf(self):
        return self._tfidf

    @tfidf.setter
    def tfidf(self, value):
        self._tfidf=value


class StayArea:
    '''
    停留区域类
    '''
    def __init__(self, centerlat=0, centerlon=0, nerberhoods=None):
        """
        :param centerlat: 停留区域中心纬度 float
        :param centerlon: 停留区域中心经度 float
        :param nerberhoods: list[Location] 停留区域邻居节点
        :return:
        """
        self._centerlat=centerlat
        self._centerlon=centerlon
        self._nerborhoods=nerberhoods


    @property
    def centerlat(self):
        return self._centerlat

    @centerlat.setter
    def centerlat(self, value):
        self._centerlat = value

    @property
    def centerlon(self):
        return self._centerlon

    @centerlon.setter
    def centerlon(self, value):
        self._centerlon = value

    @property
    def nerborhoods(self):
        return self._nerborhoods

    @nerborhoods.setter
    def nerborhoods(self, value):
        self._nerborhoods = value


class StayPoint:
    '''
    停留位置类
    '''
    def __init__(self, centerlat=0, centerlon=0, nerborhoods=None):
        """
        :param centerlat: 停留位置中心纬度
        :param centerlon: 停留位置中心经度
        :param nerborhoods: list[Location] 停留位置邻居节点
        :return:
        """
        self._centerlat = centerlat
        self._centerlon = centerlon
        self._nerborhoods = nerborhoods

    @property
    def centerlat(self):
        return self._centerlat

    @centerlat.setter
    def centerlat(self, value):
        self._centerlat=value

    @property
    def centerlon(self):
        return self._centerlon

    @centerlon.setter
    def centerlon(self, value):
        self._centerlon=value

    @property
    def nerborhoods(self):
        return self._nerborhoods

    @nerborhoods.setter
    def nerborhoods(self, value):
        self._nerborhoods=value


class UserClassify:
    '''
    用户分类结果类-v1.0
    '''
    def __init__(self):
        '''
        similarityuser类型是dict{'user':similaritynumber}
        '''
        self._user = None
        self._similarityuser = None

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    @property
    def similarityuser(self):
        return self._similarityuser

    @similarityuser.setter
    def similarityuser(self, value):
        self._similarityuser = value

class TLocation(Location):
    '''
    轨迹中的地理位置点类-v1.0
    '''
    def __init__(self, lat=0, longti=0, timer=0, tfidf=0, nerbortrajectory=[], nerbornumbers=0, status=0):
        """
        :param lat: 纬度 float
        :param longti: 经度 float
        :param timer: 记录时刻 datetime
        :param tfidf: 位置的TF-IDF值
        :param nerbortrajectory: 有邻居节点的轨迹编号以及用户ID类型为list['belongs+tid']
        :param nerbornumbers: 邻居节点数量
        :param status: 位置点的状态，0为正常，1为异常
        :return:
        """
        self._nerbortrajectory = nerbortrajectory
        self._nerbornumbers = nerbornumbers
        self._status = status
        Location.__init__(self, lat=lat, longti=longti, timer=timer, tfidf=tfidf)
        #super(ComputerPlayer, self).__init__(name, is_big_blind , is_small_blind)

    @property
    def nerbortrajectory(self):
        return self._nerbortrajectory

    @nerbortrajectory.setter
    def nerbortrajectory(self,value):
        self._nerbortrajectory = value

    @property
    def nerbornumbers(self):
        return self._nerbornumbers

    @nerbornumbers.setter
    def nerbornumbers(self, value):
        self._nerbornumbers = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


class Trajectory:
    '''
    轨迹类-v1.0
    '''
    def __init__(self, tid=0, belongs=None, normalpoint=0, beginlocation=None, endlocation=None, points=None, nerbors=[],  status=0):
        '''
        :param tid: 轨迹ID
        :param belongs: 属于哪个用户
        :param normalpoint: 该轨迹中正常点的数量
        :param beginlocation: 开始位置点
        :param endlocation: 结束位置点
        :param points: 该轨迹的所有点
        :param nerbors: 该轨迹的所有相关的轨迹
        :param status: 轨迹状态，0为正常，1为异常
        :return:
        '''
        self._tid = tid
        self._belongs = belongs
        self._normalpoint = normalpoint
        self._beginlocation = beginlocation
        self._endlocation = endlocation
        self._points = points
        self._nerbors = []
        self._status = status

    @property
    def tid(self):
        return self._tid

    @tid.setter
    def tid(self, value):
        self._tid = value

    @property
    def belongs(self):
        return self._belongs

    @belongs.setter
    def belongs(self, value):
        self._belongs = value

    @property
    def normalpoint(self):
        return self._normalpoint

    @normalpoint.setter
    def normalpoint(self, value):
        self._normalpoint = value

    @property
    def beginlocation(self):
        return self._beginlocation

    @beginlocation.setter
    def beginlocation(self, value):
        self._beginlocation = value

    @property
    def endlocation(self):
        return self._endlocation

    @endlocation.setter
    def endlocation(self, value):
        self._endlocation = value

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        self._points = value

    @property
    def nerbors(self):
        return self._nerbors

    @nerbors.setter
    def nerbors(self, value):
        self._nerbors = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value