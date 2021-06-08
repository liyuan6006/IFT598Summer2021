"""G2GProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from loginapp.views import login
from homeapp.views import home
from registerapp.views import register
from newsapp.views import news
from galleriesapp.views import galleries
from signupapp.views import signup
from eventapp.views import event
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login/',login,name='login'),
    path('home/', home,name='home'),
    path('register/', register,name='register'),
    path('news/', news,name='news'),
    path('galleries/', galleries,name='galleries'),
    path('signup/', signup,name='signup'),
    path('event/', event,name='event'),
]
