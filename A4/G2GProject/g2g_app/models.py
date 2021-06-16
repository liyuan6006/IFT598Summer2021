# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    addressid = models.AutoField(db_column='AddressID', primary_key=True)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=25, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=25, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=25, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.DecimalField(db_column='Zipcode', max_digits=9, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'address'


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
    first_name = models.CharField(max_length=30)
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


class Event(models.Model):
    eventcode = models.AutoField(db_column='EventCode', primary_key=True)  # Field name made lowercase.
    eventname = models.CharField(db_column='EventName', max_length=45)  # Field name made lowercase.
    officerid = models.ForeignKey('Officer', models.DO_NOTHING, db_column='OfficerID', blank=True, null=True)  # Field name made lowercase.
    missiondesc = models.CharField(db_column='MissionDesc', max_length=225, blank=True, null=True)  # Field name made lowercase.
    dateofvolunteer = models.DateField(db_column='DateOfVolunteer', blank=True, null=True)  # Field name made lowercase.
    attendingneed = models.DecimalField(db_column='AttendingNeed', max_digits=8, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    addressid = models.ForeignKey(Address, models.DO_NOTHING, db_column='AddressID', blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.IntegerField(db_column='PhoneNumber', blank=True, null=True)  # Field name made lowercase.
    numberattended = models.DecimalField(db_column='NumberAttended', max_digits=8, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    objectivedesc = models.CharField(db_column='ObjectiveDesc', max_length=225, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'event'


class Jobtitle(models.Model):
    jobtitleid = models.AutoField(db_column='JobTitleID', primary_key=True)  # Field name made lowercase.
    jobtitle = models.CharField(db_column='JobTitle', max_length=45)  # Field name made lowercase.
    officerid = models.ForeignKey('Officer', models.DO_NOTHING, db_column='OfficerID')  # Field name made lowercase.
    salary = models.DecimalField(db_column='Salary', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jobtitle'


class Office(models.Model):
    officeid = models.AutoField(primary_key=True)
    officename = models.CharField(db_column='OfficeName', unique=True, max_length=45)  # Field name made lowercase.
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    officerid = models.ForeignKey('Officer', models.DO_NOTHING, db_column='officerid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'office'


class Officer(models.Model):
    officerid = models.AutoField(db_column='OfficerID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    addressid = models.ForeignKey(Address, models.DO_NOTHING, db_column='AddressID', blank=True, null=True)  # Field name made lowercase.
    respdesc = models.CharField(db_column='RespDesc', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'officer'


class Volunteer(models.Model):
    volunteerid = models.AutoField(db_column='VolunteerID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    addressid = models.ForeignKey(Address, models.DO_NOTHING, db_column='AddressID', blank=True, null=True)  # Field name made lowercase.
    respdesc = models.CharField(db_column='RespDesc', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'volunteer'


class Volunteerevent(models.Model):
    volunteereventid = models.AutoField(db_column='VolunteerEventID', primary_key=True)  # Field name made lowercase.
    volunteerid = models.ForeignKey(Volunteer, models.DO_NOTHING, db_column='VolunteerID', blank=True, null=True)  # Field name made lowercase.
    eventcode = models.ForeignKey(Event, models.DO_NOTHING, db_column='EventCode', blank=True, null=True)  # Field name made lowercase.
    requestdate = models.DateField(db_column='RequestDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    signupdate = models.DateField(db_column='SignUpDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'volunteerevent'
