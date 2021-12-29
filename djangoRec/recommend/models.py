# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AllGzdata(models.Model):
    realip = models.BigIntegerField(db_column='realIP', blank=True, null=True)  # Field name made lowercase.
    realareacode = models.IntegerField(db_column='realAreacode', blank=True, null=True)  # Field name made lowercase.
    useragent = models.CharField(db_column='userAgent', max_length=500, blank=True, null=True)  # Field name made lowercase.
    useros = models.CharField(db_column='userOS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='userID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    clientid = models.CharField(db_column='clientID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.BigIntegerField(blank=True, null=True)
    timestamp_format = models.CharField(max_length=20, blank=True, null=True)
    pagepath = models.CharField(db_column='pagePath', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    ymd = models.IntegerField(blank=True, null=True)
    fullurl = models.CharField(db_column='fullURL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    fullurlid = models.CharField(db_column='fullURLId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hostname = models.CharField(max_length=500, blank=True, null=True)
    pagetitle = models.CharField(db_column='pageTitle', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    pagetitlecategoryid = models.IntegerField(db_column='pageTitleCategoryId', blank=True, null=True)  # Field name made lowercase.
    pagetitlecategoryname = models.CharField(db_column='pageTitleCategoryName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pagetitlekw = models.CharField(db_column='pageTitleKw', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    fullreferrer = models.CharField(db_column='fullReferrer', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    fullreferrerurl = models.CharField(db_column='fullReferrerURL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    organickeyword = models.CharField(db_column='organicKeyword', max_length=500, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all_gzdata'


class Areacode(models.Model):
    area = models.BigIntegerField(primary_key=True)
    num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areacode'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CleanedData(models.Model):
    realip = models.BigIntegerField(db_column='realIP', blank=True, null=True)  # Field name made lowercase.
    realareacode = models.BigIntegerField(db_column='realAreacode', blank=True, null=True)  # Field name made lowercase.
    useragent = models.TextField(db_column='userAgent', blank=True, null=True)  # Field name made lowercase.
    useros = models.TextField(db_column='userOS', blank=True, null=True)  # Field name made lowercase.
    userid = models.TextField(db_column='userID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.TextField(db_column='clientID', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.BigIntegerField(blank=True, null=True)
    timestamp_format = models.TextField(blank=True, null=True)
    pagepath = models.TextField(db_column='pagePath', blank=True, null=True)  # Field name made lowercase.
    ymd = models.BigIntegerField(blank=True, null=True)
    fullurl = models.TextField(db_column='fullURL', blank=True, null=True)  # Field name made lowercase.
    fullurlid = models.TextField(db_column='fullURLId', blank=True, null=True)  # Field name made lowercase.
    hostname = models.TextField(blank=True, null=True)
    pagetitle = models.TextField(db_column='pageTitle', blank=True, null=True)  # Field name made lowercase.
    pagetitlecategoryid = models.BigIntegerField(db_column='pageTitleCategoryId', blank=True, null=True)  # Field name made lowercase.
    pagetitlecategoryname = models.TextField(db_column='pageTitleCategoryName', blank=True, null=True)  # Field name made lowercase.
    pagetitlekw = models.TextField(db_column='pageTitleKw', blank=True, null=True)  # Field name made lowercase.
    fullreferrer = models.TextField(db_column='fullReferrer', blank=True, null=True)  # Field name made lowercase.
    fullreferrerurl = models.TextField(db_column='fullReferrerURL', blank=True, null=True)  # Field name made lowercase.
    organickeyword = models.TextField(db_column='organicKeyword', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(blank=True, null=True)
    type_1 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cleaned_data'


class CleanedGzdata(models.Model):
    realip = models.BigIntegerField(db_column='realIP', blank=True, null=True)  # Field name made lowercase.
    fullurl = models.TextField(db_column='fullURL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cleaned_gzdata'


class Count101Web(models.Model):
    type = models.CharField(primary_key=True, max_length=50)
    num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'count101web'


class Count107Web(models.Model):
    index = models.CharField(primary_key=True, max_length=50)
    num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'count107web'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


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


class Fullurl(models.Model):
    fullurl = models.CharField(db_column='fullURL', primary_key=True, max_length=200)  # Field name made lowercase.
    num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fullurl'


class OnesWeb(models.Model):
    realip = models.BigIntegerField(db_column='realIP', primary_key=True)  # Field name made lowercase.
    num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ones_web'


class Pagetitlecategoryname(models.Model):
    page = models.CharField(primary_key=True, max_length=50)
    num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pagetitlecategoryname'


class Pagetitlekw(models.Model):
    page = models.CharField(primary_key=True, max_length=50)
    num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pagetitlekw'


class Realip(models.Model):
    count = models.CharField(primary_key=True, max_length=50)
    num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'realip'


class RecommendStudentinfo(models.Model):
    stu_id = models.CharField(primary_key=True, max_length=20)
    stu_name = models.CharField(max_length=20)
    stu_pwd = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'recommend_studentinfo'


class Source(models.Model):
    source = models.CharField(primary_key=True, max_length=50)
    num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'source'


class Test(models.Model):
    mytest = models.CharField(max_length=50, blank=True, null=True)
    seconds = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'


class Timestamp(models.Model):
    timestamp = models.BigIntegerField(primary_key=True)
    num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timestamp'


class Useragent(models.Model):
    useragent = models.CharField(db_column='userAgent', primary_key=True, max_length=200)  # Field name made lowercase.
    num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'useragent'


class Useros(models.Model):
    useros = models.CharField(db_column='userOS', primary_key=True, max_length=50)  # Field name made lowercase.
    num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'useros'


class WebInfoCount(models.Model):
    index = models.CharField(primary_key=True, max_length=50)
    num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_info_count'


class Ymd(models.Model):
    ymd = models.BigIntegerField(primary_key=True)
    num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ymd'
