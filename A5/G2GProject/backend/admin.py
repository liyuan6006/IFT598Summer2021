from django.contrib import admin

from .models import Address,Officer,Event,Office,Jobtitle,Volunteer,Volunteerevent,RegisterInfo
# Register your models here.
admin.site.register(Address)
admin.site.register(Officer)
admin.site.register(Event)
admin.site.register(Office)
admin.site.register(Jobtitle)
admin.site.register(Volunteer)
admin.site.register(Volunteerevent)
admin.site.register(RegisterInfo)
