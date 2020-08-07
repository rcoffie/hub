from django.shortcuts import render,redirect 
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import logout


# Create your views here.

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password  = request.POST['password']
    user = auth.authenticate(username=username,password=password)
    if user is not None:
      auth.login(request, user)
      messages.success(request,'you have successfuly login ')
      return redirect('dashboard')
    else:
      messages.error(request,'credentials error')
      return redirect('login')
  else:
   
   return render(request,'account/login.html')



def registration(request):
  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name  = request.POST['last_name']
    username   = request.POST['username']
    email      = request.POST['email']
    username   = request.POST['username']
    password   = request.POST['password']
    password2  = request.POST['password2']

    if password == password2:
      if User.objects.filter(username=username).exists():
        messages.error(request, 'username already exists') 
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'email already eixists')
          return redirect('register')
        else:
          user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
          user.save()
          messages.success(request, 'accounts created succesfuly you can login now')
          return redirect('login')
    else:
      messages.error(request, 'password dont match')
      return redirect('register')

  return render(request, 'account/register.html')


  



def dashboard(request):
  return render(request,'account/dashboard.html')




def logoutUser(request):
  logout(request)
  return redirect('home')