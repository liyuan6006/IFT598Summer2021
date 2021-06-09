from django.shortcuts import render

from django.http import HttpResponse
from eventapp.models import Officer
# Create your views here.
def officers(request):
     officer_list = Officer.objects.order_by('name')
     officer_dict ={'officer_list_key':officer_list}
     return render(request,'officers/officers.html',context=officer_dict)