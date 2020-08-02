
from django.urls import path,include
from . import views 

urlpatterns = [
  path('register/',views.registration,name='register'),
  path('login/',views.login,name='login'),
  path('dashboard',views.dashboard,name='dashboard')
]
