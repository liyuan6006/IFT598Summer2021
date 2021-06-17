from django.shortcuts import render,redirect
from backend.models import Event, Address, Officer
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth
import string
import random
# Create your views here.
def home(request):
     return render(request,'backend/home.html')

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            return redirect('home')
        else:
            return render(request,'backend/login.html',{'error':'Wrong email or password'})
    else:
        return render(request,'backend/login.html')

def officers(request):
     officer_list = Officer.objects.order_by('name')
     officer_dict ={'officer_list_key':officer_list}
     return render(request,'backend/officers.html',context=officer_dict)

def news(request):
     return render(request,'backend/news.html')

def event(request):
     event_list = Event.objects.order_by('eventname')
     event_dict = {'event_list_key': event_list}
     return render(request, 'backend/event.html', context=event_dict)

def signup(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        verifypassword=request.POST['verifyPassword']
        if password==verifypassword:
            try:
                user = User.objects.get(username=request.POST['email'])
                return render(request, 'backend/signup.html', {'error': 'email already exists'})
            except User.DoesNotExist: 
                user = User.objects.create_user(username= email,email=email, password=password)
                return redirect('home')
        else:
            return render(request, 'backend/signup.html', {'error': 'password does not match'})
    else:
        return render(request,'backend/signup.html')


def createnewevent(request):
     if request.method == 'POST':
          street = request.POST['street']
          city = request.POST['city']
          state = request.POST['state']
          zipcode = request.POST['zipcode']
          #create address on-the-fly and return the newly created address
          address = Address.objects.get_or_create(street=street,city=city,state=state,zipcode=zipcode)[0]
          officer_name= request.POST['officer_name']
          officer = Officer.objects.get(name=officer_name)
          #create event entity
          event_name = request.POST['event_name']
          mission_desc = request.POST['mission_desc']
          objective_desc = request.POST['objective_desc']
          num_events = Event.objects.filter(eventname=event_name).exists()
          if num_events:
               return render(request, 'backend/createnewevent.html', {'error': 'event name already exists'})
          else:
                print(event_name)
                print(officer.officerid)
                print(address.addressid)
                print(mission_desc)
                print(objective_desc)
                #event = Event.objects.get_or_create(eventname=event_name, officerid=officer, addressid=address, missiondesc=mission_desc,objectivedesc=objective_desc)
                return redirect('event')
     else:
          return render(request, 'backend/createnewevent.html')   
def contactus(request):
     return render(request,'backend/contactus.html')