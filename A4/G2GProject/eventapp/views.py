from django.shortcuts import redirect, render
from django.http import HttpResponse
from eventapp.models import Event, Address, Officer
# Create your views here.


def event(request):
     event_list = Event.objects.order_by('eventname')
     event_dict = {'event_list_key': event_list}
     return render(request, 'event/event.html', context=event_dict)


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
               return render(request, 'event/createnewevent.html', {'error': 'event name already exists'})
          else:
                print(event_name)
                print(officer.officerid)
                print(address.addressid)
                print(mission_desc)
                print(objective_desc)
                event = Event.objects.get_or_create(eventname=event_name, officerid=officer, addressid=address, missiondesc=mission_desc,objectivedesc=objective_desc)
                return redirect('event')
     else:
          return render(request, 'event/createnewevent.html')   
   