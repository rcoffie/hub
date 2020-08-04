from django.shortcuts import render,redirect 
from django.contrib import messages,auth
from django.contrib.auth.models import User

# Create your views here.

def login(request):
  if request.method == 'POST':
    username  == request.POST['username']
    password  == request.POST['password']
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
    password   = request.POST['password']
    password2  = request.POST['password2']
    email      = request.POST['email']

    if password == password2:
      if username == User.objects.filter(username=username).exists():
        messages.error(request,'username already taken')
        return redirect('register')
      else:
        if email == User.objects.filter(email=email).exists():
          messages.error(request,'this email has bee used try another one')
          return redirect('register')
        else:
          user = User.objects.create(first_name=first_name,last_name=last_name,username=username,password=password,email=email)
          user.save()
          return redirect('login')
    else:
      messages.error(request,'password dont match ')
      return redirect('register')

  else:

   return render(request,'account/register.html')


  



def dashboard(request):
  return render(request,'account/dashboard.html')