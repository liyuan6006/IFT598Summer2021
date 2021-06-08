from django.shortcuts import render,redirect
from django.contrib.auth.models import User

def signup(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        verifypassword=request.POST['verifyPassword']
        if password==verifypassword:
            try:
                user = User.objects.get(username=request.POST['email'])
                return render(request, 'signup/signup.html', {'error': 'email already exists'})
            except User.DoesNotExist: 
                user = User.objects.create_user(username= email,email=email, password=password)
                return redirect('home')
        else:
            return render(request, 'signup/signup.html', {'error': 'password does not match'})
    else:
        return render(request,'signup/signup.html')
