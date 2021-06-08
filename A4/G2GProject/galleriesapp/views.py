from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def galleries(request):
     return render(request,'galleries/galleries.html')