from django.db import models

# Create your models here.
class offerDeals(models.Model):
    place=models.CharField(max_length=100)
    price=models.FloatField()
    img=models.ImageField(upload_to='static/images/')

class destinationPlaces:
    place=models.CharField(max_length=100)
    price=models.FloatField()
    img=models.ImageField(upload_to='static/images/')
    description=models.TextField()