from django.shortcuts import render

# Create your views here.

def login(request):
  return render(request,'account/login.html')



def registration(request):
  return render(request,'account/register.html')



def dashboard(request):
  return render(request,'account/dashboard.html')