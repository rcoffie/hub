from django.contrib import admin
from .models import *



class AdAdmin(admin.ModelAdmin):
  list_display = ('id','title','seller','location','region','price','negotiable','used','published')
  list_display_links = ('title','seller')
  list_filter = ('title','seller','price','location','region')
  list_editable = ('id','negotiable','published','used')
  search_fields = ('title','seller','price','city','region')
  list_per_page = 12 

# Register your models here.
admin.site.register(Ad,AdAdmin)
