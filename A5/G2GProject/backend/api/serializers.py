from rest_framework import routers, serializers, viewsets
from ..models import Event, Officer
from django.contrib.auth.models import User

class OfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officer
        fields = ['officerid', 'name', 'age', 'addressid','respdesc']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['eventcode', 'officerid', 'missiondesc', 'dateofvolunteer','attendingneed','addressid','phonenumber','numberattended','objectivedesc']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']