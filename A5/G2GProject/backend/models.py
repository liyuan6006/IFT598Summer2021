from django.contrib.auth.models import User
from django.db import models

class Address(models.Model):
    
    addressid = models.AutoField( primary_key=True)  
    street = models.CharField(max_length=25, blank=True, null=True)  
    city = models.CharField(max_length=25, blank=True, null=True)  
    state = models.CharField(max_length=25, blank=True, null=True)  
    zipcode = models.DecimalField(max_digits=9, decimal_places=0, blank=True, null=True)  
    def __str__(self):
        return str(self.city+self.street+self.state)

class Officer(models.Model):
    officerid = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=45,blank=True, null=True)  
    age = models.IntegerField(blank=True, null=True)  
    addressid = models.ForeignKey(Address, on_delete=models.DO_NOTHING, blank=True, null=True)  
    respdesc = models.CharField(max_length=45, blank=True, null=True)  

    def __str__(self):
        return str(self.name)

class Event(models.Model):
    eventcode = models.AutoField(primary_key=True)  
    eventname = models.CharField(max_length=45)  
    officerid = models.ForeignKey(Officer, on_delete=models.DO_NOTHING, blank=True, null=True)  #1:M
    missiondesc = models.CharField(max_length=225, blank=True, null=True)  
    dateofvolunteer = models.DateField(blank=True, null=True)  
    attendingneed = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)  
    addressid = models.ForeignKey(Address, on_delete=models.DO_NOTHING, blank=True, null=True)  
    phonenumber = models.IntegerField(blank=True, null=True)  
    numberattended = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)  
    objectivedesc = models.CharField(max_length=225, blank=True, null=True)  

    def __str__(self):
        return str(self.eventname)

class Jobtitle(models.Model):
    jobtitleid = models.AutoField(primary_key=True)  
    jobtitle = models.CharField(max_length=45,blank=True, null=True)  
    officerid = models.ForeignKey(Officer, on_delete=models.DO_NOTHING,blank=True, null=True)  
    salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)  

    def __str__(self):
        return str(self.jobtitleid)



class Office(models.Model):
    officeid = models.AutoField(primary_key=True)
    officename = models.CharField(unique=True, max_length=45)  
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    officerid = models.ForeignKey(Officer, on_delete=models.DO_NOTHING, db_column='officerid', blank=True, null=True)
    
    def __str__(self):
        return str(self.officeid)


class Volunteer(models.Model):
    volunteerid = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=45,blank=True, null=True)  
    age = models.IntegerField(blank=True, null=True)  
    addressid = models.ForeignKey(Address, on_delete=models.DO_NOTHING, blank=True, null=True)  
    respdesc = models.CharField(max_length=45, blank=True, null=True)  

    def __str__(self):
        return str(self.volunteerid)



class Volunteerevent(models.Model):
    volunteereventid = models.AutoField(primary_key=True)  
    volunteerid = models.ForeignKey(Volunteer, on_delete=models.DO_NOTHING, blank=True, null=True)  
    eventcode = models.ForeignKey(Event, on_delete=models.DO_NOTHING, blank=True, null=True)  
    requestdate = models.DateField(blank=True, null=True)  
    enddate = models.DateField(blank=True, null=True)  
    signupdate = models.DateField(blank=True, null=True)  

    def __str__(self):
        return str(self.volunteereventid)

class RegisterInfo(models.Model):
    registerid = models.AutoField(primary_key=True)  
    userid = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)  
    cellphone = models.IntegerField(blank=True, null=True)  
    gender = models.IntegerField(blank=True, null=True)  
    addressid = models.ForeignKey(Address, on_delete=models.DO_NOTHING, blank=True, null=True)  
    dateofbirth=models.DateField(blank=True, null=True)  
    def __str__(self):
        return str(self.registerid)