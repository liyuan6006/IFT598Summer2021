from django.shortcuts import render,redirect
from g2g_app.models import Event, Address, Officer
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth
# Create your views here.
def home(request):
     return render(request,'g2g_app/home.html')

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user = auth.authenticate(username=email, password=password)
        if user is not None:
        # if email=='123@abc.com'and password=='123':
            return redirect('home')
        else:
            return render(request,'g2g_app/login.html',{'error':'Wrong email or password'})
    else:
        return render(request,'g2g_app/login.html')

def officers(request):
    #  officer_list = Officer.objects.order_by('name')
     officer_list = []#fake data source for now
     for x in range(1, 8):
        officer = Officer(officerid=x,name='fake name',age=x*10,respdesc="fake respdesc")
        officer_list.append(officer)
     officer_dict ={'officer_list_key':officer_list}
     return render(request,'g2g_app/officers.html',context=officer_dict)

def news(request):
     return render(request,'g2g_app/news.html')

def register(request):
     return render(request,'register/register.html')

def event(request):
     #event_list = Event.objects.order_by('eventname')
     event_list = []#fake data source for now
     for x in range(1, 8):
         event = Event(eventname="fake eventname",missiondesc="fake missiondesc",objectivedesc="fake objectivedesc")
         event_list.append(event)
     event_dict = {'event_list_key': event_list}
     return render(request, 'g2g_app/event.html', context=event_dict)

def signup(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        verifypassword=request.POST['verifyPassword']
        if password==verifypassword:
            try:
                user = User.objects.get(username=request.POST['email'])
                return render(request, 'g2g_app/signup.html', {'error': 'email already exists'})
            except User.DoesNotExist: 
                user = User.objects.create_user(username= email,email=email, password=password)
                return redirect('home')
        else:
            return render(request, 'g2g_app/signup.html', {'error': 'password does not match'})
    else:
        return render(request,'g2g_app/signup.html')


def createnewevent(request):
     if request.method == 'POST':
          street = request.POST['street']
          city = request.POST['city']
          state = request.POST['state']
          zipcode = request.POST['zipcode']
          #create address on-the-fly and return the newly created address
          address = Address.objects.get_or_create(street=street,city=city,state=state,zipcode=zipcode)[0]
          #addressid = address.addressid
          #get officerid
          officer_name= request.POST['officer_name']
          officer = Officer.objects.get(name=officer_name)
          #officer_id = officer.officerid
          #create event entity
          event_name = request.POST['event_name']
          mission_desc = request.POST['mission_desc']
          objective_desc = request.POST['objective_desc']
          num_events = Event.objects.filter(eventname=event_name).exists()
          if num_events:
               return render(request, 'g2g_app/createnewevent.html', {'error': 'event name already exists'})
          else:
                print(event_name)
                print(officer.officerid)
                print(address.addressid)
                print(mission_desc)
                print(objective_desc)
                #event = Event.objects.get_or_create(eventname=event_name, officerid=officer, addressid=address, missiondesc=mission_desc,objectivedesc=objective_desc)
                return redirect('event')
     else:
          return render(request, 'g2g_app/createnewevent.html')   
def contactus(request):
     return render(request,'g2g_app/contactus.html')