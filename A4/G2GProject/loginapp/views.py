from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import auth
# Create your views here.
def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user = auth.authenticate(username=email, password=password)
        if user is not None:
        # if email=='123@abc.com'and password=='123':
            return redirect('home')
        else:
            return render(request,'login/login.html',{'error':'Wrong email or password'})
    else:
        return render(request,'login/login.html')

        
    # Create your views here.
    
    # return HttpResponse("Hello my friend,welcome to login page")
    