from django.db import models
from datetime import datetime
from seller.models import Seller


# Create your models here.
class Ad(models.Model):

  Category=(
    ('Mobile Phones','Mobile Phones'),
    ('Mobile Phone Accessories','Mobile Phone Accessories'),
    ('Computer Accessories','Computer Accessories'),
    ('TVs','TVs'),
     ('TV & Video Accessories','TV & Video Accessories'),
    ('Cameras & Camcorders','Cameras & Camcorders'),
    ('Audio & MP3','Audio & MP3'),
    ('Other Electronics','Other Electronics'),
   )

  Region=(
    ('Upper West','Upper West'),
    ('Upper East','Upper East'),
    ('North East','North East'),
    ('Northen','Northen'),
     ('Savannah','Savannah'),
    ('Bono East','Bono East'),
    ('Brong Ahafo','Brong Ahafo'),
    ('Oti','Oti'),
    ('Ahafo','Ahafo'),
    ('Ashanti','Ashanti'),
    ('Volta','Volta'),
    ('Greater Accra','Greater Accra'),
    ('Western North','Western North'),
    ('Western','Western'),
    ('Eastern','Eastern'),
    ('Central','Central'),
   )

  title = models.CharField(max_length=100)
  seller= models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
  category = models.CharField(max_length=200, null=True,choices=Category)
  location = models.CharField(max_length=100)
  region   =  models.CharField(max_length=200, null=True,choices=Region)
  brand    = models.CharField(max_length=50)
  price    = models.IntegerField()
  phone    = models.BigIntegerField()
  description = models.TextField()
  published = models.BooleanField(default=False,null=True)
  used      = models.BooleanField(default=False,null=True)
  negotiable = models.BooleanField(default=False,null=True)
  main_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo      = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1    = models.ImageField(upload_to='photos/%Y/%m/%d/')
  date_posted = models.DateField(default=datetime.now, blank=True)


  def __str__(self):
    return self.title


    

