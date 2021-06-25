from django.shortcuts import render,redirect
from backend.models import Event, Address, Officer,RegisterInfo
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib import auth
import string
import random
# Create your views here.
def home(request):
     return render(request,'backend/home.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
         user_dict ={'user':user}
         return render(request,'backend/home.html',context=user_dict)
        else:
            return render(request,'backend/login.html',{'error':'Wrong user name or password'})
    else:
        return render(request,'backend/login.html')
        
def mylogout(request):
    logout(request)
    return redirect('/')

def officers(request):
     officer_list = Officer.objects.order_by('addressid')
     officer_dict ={'officer_list_key':officer_list}
     return render(request,'backend/officers.html',context=officer_dict)

def deleteofficer(request,id):
    officer = Officer.objects.get(pk=id)
    officer.delete()
    return redirect('officers')
 
#update officer
def updateofficer(request,id):
     if request.method == 'POST':
         officer = Officer.objects.get(pk=id)
         officer.name=officer_name= request.POST['officer_name']
         officer.age= officer_age = request.POST['officer_age']
         officer.respdesc=resp_desc = request.POST['resp_desc']
         officer.save()
         return redirect('officers')
     else:
         officer = Officer.objects.get(pk=id)
         officer_dict ={'officer':officer}
         return render(request, 'backend/updateofficer.html',context=officer_dict)   

def createnewofficer(request):
     if request.method == 'POST':
          street = request.POST['street']
          city = request.POST['city']
          state = request.POST['state']
          zipcode = request.POST['zipcode']
          #create address on-the-fly and return the newly created address
          address = Address.objects.get_or_create(street=street,city=city,state=state,zipcode=zipcode)[0]
          officer_name= request.POST['officer_name']
          officer_age = request.POST['officer_age']
          resp_desc = request.POST['resp_desc']
          num_officers = Officer.objects.filter(name=officer_name).exists()
          if num_officers:
               return render(request, 'backend/createnewofficer.html', {'error': 'officer name already exists'})
          else:
                print(officer_name)
                print(officer_age)
                print(address.addressid)
                print(resp_desc)
                officer = Officer.objects.get_or_create(name=officer_name, age=officer_age, addressid=address, respdesc=resp_desc)
                return redirect('officers')
     else:
          return render(request, 'backend/createnewofficer.html')   

def news(request):
     return render(request,'backend/news.html')

def event(request):
     event_list = Event.objects.order_by('eventname')
     event_dict = {'event_list_key': event_list}
     return render(request, 'backend/event.html', context=event_dict)

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        verifypassword=request.POST['verifyPassword']
        gender=request.POST['gender']
        cellphone=request.POST['cellphone']
        dateofbirth=request.POST['dateofbirth']
        street = request.POST['street']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        if password==verifypassword:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'backend/signup.html', {'error': 'username already exists'})
            except User.DoesNotExist: 
                user = User.objects.create_user(username= username,email=email, password=password, first_name=firstname, last_name=lastname)
                address = Address.objects.get_or_create(street=street,city=city,state=state,zipcode=zipcode)[0]
                RegisterInfo.objects.get_or_create(userid=user,addressid=address,gender=gender,cellphone=cellphone,dateofbirth=dateofbirth)
                user_dict ={'user':user}
                return render(request,'backend/home.html',context=user_dict)
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
          #create event entity
          event_name = request.POST['event_name']
          mission_desc = request.POST['mission_desc']
          objective_desc = request.POST['objective_desc']
          num_events = Event.objects.filter(eventname=event_name).exists()
          if num_events:
               return render(request, 'backend/createnewevent.html', {'error': 'event name already exists'})
          else:
                print(event_name)
                print(address.addressid)
                print(mission_desc)
                print(objective_desc)
                event = Event.objects.get_or_create(eventname=event_name, addressid=address, missiondesc=mission_desc,objectivedesc=objective_desc)
                return redirect('event')
     else:
          return render(request, 'backend/createnewevent.html')   
def contactus(request):
     return render(request,'backend/contactus.html')