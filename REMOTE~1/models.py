from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    gender= models.CharField(max_length=30)
    address= models.CharField(max_length=30)


class content_detection_type(models.Model):


    video_id= models.CharField(max_length=3000)
    title= models.CharField(max_length=3000)
    channel_title= models.CharField(max_length=3000)
    category= models.CharField(max_length=3000)
    publish_time= models.CharField(max_length=3000)
    content= models.CharField(max_length=30000)
    views= models.CharField(max_length=3000)
    likes= models.CharField(max_length=3000)
    dislikes= models.CharField(max_length=3000)
    comment_count= models.CharField(max_length=3000)
    Video_link= models.CharField(max_length=3000)
    publish_date= models.CharField(max_length=3000)
    views_per_day= models.CharField(max_length=3000)
    Prediction= models.CharField(max_length=3000)


class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



