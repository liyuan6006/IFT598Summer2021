from django.shortcuts import render
from django.http import HttpResponse
from eventapp.models import Event,Address
# Create your views here.
def event(request):
     event_list = Event.objects.order_by('eventname')
     event_dict ={'event_list_key':event_list}
     return render(request,'event/event.html',context=event_dict)