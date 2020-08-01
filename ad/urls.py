
from django.urls import path,include
from . import views 

urlpatterns = [
   path('',views.ads,name='ads'),
   path('<int:ad_id>',views.ad,name='ad'),
   path('search/',views.search,name='search')
]
