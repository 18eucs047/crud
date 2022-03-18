from django.db import models
import datetime
import os


# Create your models here.
class Quality(models.Model):
             title = models.CharField(max_length=50)

             def __str__(self):
                         return self.title

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class Vehicles(models.Model):
             username = models.CharField(max_length=50,default='NULL')
             company = models.CharField(max_length=30,default='NULL')
             name = models.CharField(max_length=50)
             vehicle_code = models.CharField(max_length=5)
             vehicle_price = models.CharField(max_length=15)
             quality = models.ForeignKey(Quality,on_delete=models.CASCADE)
             image = models.ImageField(upload_to=filepath, null=True, blank=True)

             def __str__(self):
                         return self.name
