from django.db import models
from datetime import datetime
class cars(models.Model):
    cars_name = models.CharField(max_length=255)
    cars_image = models.ImageField(upload_to='pic')
    price = models.FloatField()
    des = models.TextField()
    opt = models.CharField(max_length=200)
    year = models.IntegerField()


class parts(models.Model):
    model_name = models.CharField(max_length=255)
    parts_image =  models.ImageField(upload_to='pic')


    def __str__(self):
        return self.model_name


class detail(models.Model):
    part = models.ForeignKey(parts,on_delete=models.CASCADE)
    p_name = models.CharField(max_length=200)
    p_image = models.ImageField(upload_to='pic')
    p_des = models.TextField()
    p_price = models.IntegerField()


class s_services(models.Model):
    s_name = models.CharField(max_length=200)
    s_address = models.CharField(max_length=200)
    s_loc = models.CharField(max_length=200)
    s_phone = models.CharField(max_length=200)
    s_time = models.CharField(max_length=200)
    s_image = models.ImageField(upload_to='pic',default='servicelogo')





