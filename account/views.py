from django.shortcuts import render,redirect 
from django.contrib import messages

# Create your views here.

def login(request):
  if request.method == 'POST':
    messages.error(request, 'testing error message')
    return redirect ('login')
  return render(request,'account/login.html')



def registration(request):
  if request.method == 'POST':
    messages.error(request,'testingerror message ma gee')
    return redirect('register')
  return render(request,'account/register.html')



def dashboard(request):
  return render(request,'account/dashboard.html')