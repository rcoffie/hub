from django.shortcuts import render,get_object_or_404
from .models import *
from ad.choices import *

# Create your views here.

def ads(request):
  ads = Ad.objects.order_by('-date_posted').filter(published=True)
  context = {'ads':ads,}
  return render(request, 'ad/ads.html',context)




def search(request):
  query_ads = Ad.objects.order_by('-date_posted')

  #keywords 
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      query_ads = query_ads.filter(description__icontains=keywords)

  context = {
    
    'query_ads':query_ads,
              
  }
  return render(request,'ad/search.html',context)




def ad(request,ad_id):
  ad = get_object_or_404(Ad,pk=ad_id)
  context = {'ad':ad,}
  return render(request,'ad/ad.html',context)