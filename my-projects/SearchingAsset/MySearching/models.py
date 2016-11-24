from __future__ import unicode_literals

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.


from django.db import models


class Abandonrecord(models.Model):
    aid = models.BigIntegerField(db_column='aId', primary_key=True)  # Field name made lowercase.
    relatenum = models.CharField(db_column='relateNum', max_length=60)  # Field name made lowercase.
    atime = models.CharField(db_column='aTime', max_length=20)  # Field name made lowercase.
    areason = models.CharField(db_column='aReason', max_length=500)  # Field name made lowercase.
    aaction = models.CharField(db_column='aAction', max_length=200)  # Field name made lowercase.
    apeo = models.CharField(db_column='aPeo', max_length=60)  # Field name made lowercase.
    aapeo = models.CharField(db_column='aaPeo', max_length=20)  # Field name made lowercase.
    aother = models.CharField(db_column='aOther', max_length=500, blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'AbandonRecord'

    class Admin:
        pass


class Borrowrecord(models.Model):
    bid = models.BigIntegerField(db_column='bId', primary_key=True)  # Field name made lowercase.
    relatenum = models.CharField(db_column='relateNum', max_length=60)  # Field name made lowercase.
    bpeo = models.CharField(db_column='bPeo', max_length=20)  # Field name made lowercase.
    bedpeo = models.CharField(db_column='bedPeo', max_length=20)  # Field name made lowercase.
    bapeo = models.CharField(db_column='baPeo', max_length=20)  # Field name made lowercase.
    bposition = models.CharField(db_column='bPosition', max_length=200)  # Field name made lowercase.
    btime = models.CharField(db_column='bTime', max_length=20)  # Field name made lowercase.
    bbtime = models.CharField(db_column='bbTime', max_length=20)  # Field name made lowercase.
    bother = models.CharField(db_column='bOther', max_length=500, blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'BorrowRecord'

    class Admin:
        pass

class Classify(models.Model):
    cid = models.BigIntegerField(db_column='cId', primary_key=True)  # Field name made lowercase.
    cname = models.CharField(db_column='cName', max_length=101)  # Field name made lowercase.
    ctype = models.CharField(db_column='cType', max_length=50)  # Field name made lowercase.
    cnname = models.CharField(db_column='cnName', max_length=50)  # Field name made lowercase.
    cmodule = models.CharField(db_column='cModule', max_length=20)  # Field name made lowercase.

    class Meta:
        db_table = 'Classify'

    class Admin:
        pass

class Fixrecord(models.Model):
    fid = models.BigIntegerField(db_column='fId', primary_key=True)  # Field name made lowercase.
    relatenum = models.CharField(db_column='relateNum', max_length=60)  # Field name made lowercase.
    ftime = models.CharField(db_column='fTime', max_length=20)  # Field name made lowercase.
    fposition = models.CharField(db_column='fPosition', max_length=200)  # Field name made lowercase.
    fpeo = models.CharField(db_column='fPeo', max_length=20)  # Field name made lowercase.
    fpeijian = models.CharField(db_column='fPeijian', max_length=500, blank=True)  # Field name made lowercase.
    fedtime = models.CharField(db_column='fedTime', max_length=20, blank=True)  # Field name made lowercase.
    freason = models.CharField(db_column='fReason', max_length=500, blank=True)  # Field name made lowercase.
    fprice = models.FloatField(db_column='fPrice', blank=True, null=True)  # Field name made lowercase.
    fcondition = models.CharField(db_column='fCondition', max_length=500, blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'FixRecord'

    class Admin:
        pass

class Fromer(models.Model):
    fid =models.BigIntegerField(db_column='fId', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_column='fName', max_length=50)  # Field name made lowercase.

    class Meta:
        db_table = 'Fromer'

    class Admin:
        pass

class Keeper(models.Model):
    kid = models.BigIntegerField(db_column='kId', primary_key=True)  # Field name made lowercase.
    kname = models.CharField(db_column='kName', max_length=20)  # Field name made lowercase.

    class Meta:
        db_table = 'Keeper'

    class Admin:
        pass

class Logininfo(models.Model):
    lid = models.BigIntegerField(db_column='LID', primary_key=True)  # Field name made lowercase.
    login = models.CharField(db_column='Login', max_length=4)  # Field name made lowercase.
    psw = models.CharField(db_column='Psw', max_length=50)  # Field name made lowercase.
    logintime = models.DateTimeField(db_column='LoginTime')  # Field name made lowercase.
    macip = models.CharField(db_column='MacIP', max_length=50)  # Field name made lowercase.

    class Meta:
        db_table = 'LoginInfo'

    class Admin:
        pass

class Medical(models.Model):
    mid = models.BigIntegerField(db_column='mId', primary_key=True)  # Field name made lowercase.
    mnum = models.CharField(db_column='mNum', max_length=60)  # Field name made lowercase.
    mtype = models.CharField(db_column='mType', max_length=50)  # Field name made lowercase.
    mname = models.CharField(db_column='mName', max_length=50)  # Field name made lowercase.
    muse = models.CharField(db_column='mUse', max_length=50, blank=True)  # Field name made lowercase.
    mclass = models.CharField(db_column='mClass', max_length=50, blank=True)  # Field name made lowercase.
    msetting = models.CharField(db_column='mSetting', max_length=500, blank=True)  # Field name made lowercase.
    mposition = models.CharField(db_column='mPosition', max_length=50, blank=True)  # Field name made lowercase.
    mkeeper = models.CharField(db_column='mKeeper', max_length=20, blank=True)  # Field name made lowercase.
    mfrom = models.CharField(db_column='mFrom', max_length=50, blank=True)  # Field name made lowercase.
    mprice = models.FloatField(db_column='mPrice')  # Field name made lowercase.
    mnumber = models.IntegerField(db_column='mNumber')  # Field name made lowercase.
    mbuytime = models.CharField(db_column='mBuyTime', max_length=20)  # Field name made lowercase.
    musetime = models.CharField(db_column='mUseTime', max_length=20, blank=True)  # Field name made lowercase.
    mproducer = models.CharField(db_column='mProducer', max_length=200, blank=True)  # Field name made lowercase.
    maddress = models.CharField(db_column='mAddress', max_length=200, blank=True)  # Field name made lowercase.
    mproducenum = models.CharField(db_column='mProduceNum', max_length=50, blank=True)  # Field name made lowercase.
    mproducephone = models.CharField(db_column='mProducePhone', max_length=20, blank=True)  # Field name made lowercase.
    mfixphone = models.CharField(db_column='mFixPhone', max_length=20, blank=True)  # Field name made lowercase.
    mother = models.CharField(db_column='mOther', max_length=500, blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Medical'

    class Admin:
        pass

class Name(models.Model):
    nid = models.BigIntegerField(db_column='nId', primary_key=True)  # Field name made lowercase.
    nname = models.CharField(db_column='nName', max_length=50)  # Field name made lowercase.
    ntype = models.CharField(db_column='nType', max_length=50)  # Field name made lowercase.
    nmodule = models.CharField(db_column='nModule', max_length=20)  # Field name made lowercase.

    class Meta:
        db_table = 'Name'

    class Admin:
        pass

class Position(models.Model):
    pid = models.BigIntegerField(db_column='pId', primary_key=True)  # Field name made lowercase.
    pname = models.CharField(db_column='pName', max_length=50)  # Field name made lowercase.

    class Meta:
        db_table = 'Position'

    class Admin:
        pass

class Printchoies(models.Model):
    pid = models.BigIntegerField(db_column='pId', primary_key=True)  # Field name made lowercase.
    pname = models.CharField(db_column='pName', max_length=10)  # Field name made lowercase.
    num = models.NullBooleanField()
    ptype = models.NullBooleanField()
    name = models.NullBooleanField()
    puse = models.NullBooleanField()
    pclass = models.NullBooleanField()
    setting = models.NullBooleanField()
    position = models.NullBooleanField()
    keeper = models.NullBooleanField()
    pfrom = models.NullBooleanField()
    price = models.NullBooleanField()
    number = models.NullBooleanField()
    buytime = models.NullBooleanField(db_column='buyTime')  # Field name made lowercase.
    usetime = models.NullBooleanField(db_column='useTime')  # Field name made lowercase.
    discount = models.NullBooleanField()
    pricenow = models.NullBooleanField(db_column='priceNow')  # Field name made lowercase.
    producer = models.NullBooleanField()
    paddress = models.NullBooleanField()
    producenum = models.NullBooleanField(db_column='produceNum')  # Field name made lowercase.
    producephone = models.NullBooleanField(db_column='producePhone')  # Field name made lowercase.
    fixphone = models.NullBooleanField(db_column='fixPhone')  # Field name made lowercase.
    other = models.NullBooleanField()
    fix = models.NullBooleanField()
    borrow = models.NullBooleanField()
    psend = models.NullBooleanField()
    abandon = models.NullBooleanField()

    class Meta:
        db_table = 'PrintChoies'

    class Admin:
        pass

class Sendrecord(models.Model):
    sid = models.BigIntegerField(db_column='sId', primary_key=True)  # Field name made lowercase.
    relatenum = models.CharField(db_column='relateNum', max_length=60)  # Field name made lowercase.
    stime = models.CharField(db_column='sTime', max_length=20)  # Field name made lowercase.
    snposition = models.CharField(db_column='snPosition', max_length=50)  # Field name made lowercase.
    snpeo = models.CharField(db_column='snPeo', max_length=20)  # Field name made lowercase.
    soposition = models.CharField(db_column='soPosition', max_length=50)  # Field name made lowercase.
    sopeo = models.CharField(db_column='soPeo', max_length=20)  # Field name made lowercase.
    sapeo = models.CharField(db_column='saPeo', max_length=20)  # Field name made lowercase.
    sother = models.CharField(db_column='sOther', max_length=500, blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'SendRecord'

    class Admin:
        pass

class Solid(models.Model):
    sid = models.BigIntegerField(db_column='sId', primary_key=True)  # Field name made lowercase.
    snum = models.CharField(db_column='sNum', max_length=60)  # Field name made lowercase.
    stype = models.CharField(db_column='sType', max_length=50)  # Field name made lowercase.
    sname = models.CharField(db_column='sName', max_length=50)  # Field name made lowercase.
    suse = models.CharField(db_column='sUse', max_length=50, blank=True)  # Field name made lowercase.
    sclass = models.CharField(db_column='sClass', max_length=50, blank=True)  # Field name made lowercase.
    ssetting = models.CharField(db_column='sSetting', max_length=500, blank=True)  # Field name made lowercase.
    sposition = models.CharField(db_column='sPosition', max_length=50, blank=True)  # Field name made lowercase.
    skeeper = models.CharField(db_column='sKeeper', max_length=20, blank=True)  # Field name made lowercase.
    sfrom = models.CharField(db_column='sFrom', max_length=50, blank=True)  # Field name made lowercase.
    sprice = models.FloatField(db_column='sPrice')  # Field name made lowercase.
    snumber = models.IntegerField(db_column='sNumber')  # Field name made lowercase.
    sbuytime = models.CharField(db_column='sBuyTime', max_length=20)  # Field name made lowercase.
    susetime = models.CharField(db_column='sUseTime', max_length=10, blank=True)  # Field name made lowercase.
    sproducer = models.CharField(db_column='sProducer', max_length=200, blank=True)  # Field name made lowercase.
    saddress = models.CharField(db_column='sAddress', max_length=200, blank=True)  # Field name made lowercase.
    sproducenum = models.CharField(db_column='sProduceNum', max_length=50, blank=True)  # Field name made lowercase.
    sproducephone = models.CharField(db_column='sProducePhone', max_length=20, blank=True)  # Field name made lowercase.
    sfixphone = models.CharField(db_column='sFixPhone', max_length=20, blank=True)  # Field name made lowercase.
    sother = models.CharField(db_column='sOther', max_length=500, blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Solid'

    class Admin:
        pass

class Thing(models.Model):
    tid = models.BigIntegerField(db_column='tId', primary_key=True)  # Field name made lowercase.
    tnum = models.CharField(db_column='tNum', max_length=60)  # Field name made lowercase.
    ttype = models.CharField(db_column='tType', max_length=50)  # Field name made lowercase.
    tname = models.CharField(db_column='tName', max_length=50)  # Field name made lowercase.
    tuse = models.CharField(db_column='tUse', max_length=50, blank=True)  # Field name made lowercase.
    tclass = models.CharField(db_column='tClass', max_length=50, blank=True)  # Field name made lowercase.
    tsetting = models.CharField(db_column='tSetting', max_length=500, blank=True)  # Field name made lowercase.
    tposition = models.CharField(db_column='tPosition', max_length=50, blank=True)  # Field name made lowercase.
    tkeeper = models.CharField(db_column='tKeeper', max_length=20, blank=True)  # Field name made lowercase.
    tfrom = models.CharField(db_column='tFrom', max_length=50, blank=True)  # Field name made lowercase.
    tprice = models.FloatField(db_column='tPrice')  # Field name made lowercase.
    tnumber = models.IntegerField(db_column='tNumber')  # Field name made lowercase.
    tbuytime = models.CharField(db_column='tBuyTime', max_length=20)  # Field name made lowercase.
    tusetime = models.CharField(db_column='tUseTime', max_length=10, blank=True)  # Field name made lowercase.
    tproducer = models.CharField(db_column='tProducer', max_length=200, blank=True)  # Field name made lowercase.
    taddress = models.CharField(db_column='tAddress', max_length=200, blank=True)  # Field name made lowercase.
    tproducenum = models.CharField(db_column='tProduceNum', max_length=50, blank=True)  # Field name made lowercase.
    tproducephone = models.CharField(db_column='tProducePhone', max_length=20, blank=True)  # Field name made lowercase.
    tfixphone = models.CharField(db_column='tFixPhone', max_length=20, blank=True)  # Field name made lowercase.
    tother = models.CharField(db_column='tOther', max_length=500, blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Thing'

    class Admin:
        pass

class Time(models.Model):
    tid = models.BigIntegerField(db_column='tId', primary_key=True)  # Field name made lowercase.
    tname = models.CharField(db_column='tName', max_length=10)  # Field name made lowercase.

    class Meta:
        db_table = 'Time'

    class Admin:
        pass

class Type(models.Model):
    tid = models.BigIntegerField(db_column='tId', primary_key=True)  # Field name made lowercase.
    tname = models.CharField(db_column='tName', max_length=50)  # Field name made lowercase.
    tmodule = models.CharField(db_column='tModule', max_length=20)  # Field name made lowercase.

    class Meta:
        db_table = 'Type'

    class Admin:
        pass

class Userinfo(models.Model):
    uid = models.BigIntegerField(db_column='uId', primary_key=True)  # Field name made lowercase.
    unum = models.CharField(db_column='uNum', max_length=4)  # Field name made lowercase.
    upass = models.CharField(db_column='uPass', max_length=50)  # Field name made lowercase.
    uname = models.CharField(db_column='uName', max_length=20)  # Field name made lowercase.
    uofficial = models.CharField(db_column='uOfficial', max_length=30, blank=True)  # Field name made lowercase.
    uposition = models.CharField(db_column='uPosition', max_length=50, blank=True)  # Field name made lowercase.
    uqueryright = models.NullBooleanField(db_column='uQueryRight')  # Field name made lowercase.
    usolidright = models.NullBooleanField(db_column='uSolidRight')  # Field name made lowercase.
    uthingright = models.NullBooleanField(db_column='uThingRight')  # Field name made lowercase.
    umedicalright = models.NullBooleanField(db_column='uMedicalRight')  # Field name made lowercase.
    usystemright = models.NullBooleanField(db_column='uSystemRight')  # Field name made lowercase.
    uquestion = models.CharField(db_column='uQuestion', max_length=50, blank=True)  # Field name made lowercase.
    uanswer = models.CharField(db_column='uAnswer', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'UserInfo'

    class Admin:
        pass

class Using(models.Model):
    uid = models.BigIntegerField(db_column='uId', primary_key=True)  # Field name made lowercase.
    uname = models.CharField(db_column='uName', max_length=101)  # Field name made lowercase.
    utype = models.CharField(db_column='uType', max_length=50)  # Field name made lowercase.
    unname = models.CharField(db_column='unName', max_length=50)  # Field name made lowercase.
    umodule = models.CharField(db_column='uModule', max_length=20)  # Field name made lowercase.

    class Meta:
        db_table = 'Using'

    class Admin:
        pass

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.NullBooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.NullBooleanField()
    is_active = models.NullBooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

