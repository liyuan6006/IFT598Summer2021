from django.db import models

# Create your models here.


class Officer(models.Model):
    officerid = models.AutoField(db_column='OfficerID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    addressid = models.ForeignKey(Address, models.DO_NOTHING, db_column='AddressID', blank=True, null=True)  # Field name made lowercase.
    respdesc = models.CharField(db_column='RespDesc', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'officer'