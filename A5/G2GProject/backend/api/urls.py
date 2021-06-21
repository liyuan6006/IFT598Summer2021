from django import urls
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('officerlist/',views.OfficerListView.as_view(),name='officer_list'),
    path('officerlist/<pk>/',views.OfficerDetailView.as_view(),name='officer_detail'),
    path('eventlist/',views.EventListView.as_view(),name='event_list'),
    path('eventlist/<pk>/',views.EventDetailView.as_view(),name='event_detail'),
    path('userlist/',views.UserListView.as_view(),name='user_list')
    ]