from .serializers import EventSerializer, OfficerSerializer,UserSerializer
from rest_framework import generics,viewsets
from ..models import Officer,Event
from django.contrib.auth.models import User

class OfficerListView(generics.ListAPIView):
     queryset=Officer.objects.all()
     serializer_class=OfficerSerializer

class OfficerDetailView(generics.RetrieveAPIView):
     queryset=Officer.objects.all()
     serializer_class=OfficerSerializer

class EventListView(generics.ListAPIView):
    queryset=Event.objects.all() 
    serializer_class=EventSerializer

class EventDetailView(generics.RetrieveAPIView):
     queryset=Event.objects.all()
     serializer_class=EventSerializer

# ViewSets define the view behavior.
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer