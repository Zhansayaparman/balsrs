from django.db import models

# Create your models here.
from django.urls import reverse

class tauar(models.Model):
    tauar_name = models.CharField(max_length=200, help_text=" ")
   tauar_address = models.CharField(max_length=200, help_text=" ")
   
    phone_number = models.CharField(max_length=200, help_text=" ")

    class Meta:
        ordering = ["tauar_name", "tauar_address"]


    def get_absolute_url(self):
        return reverse('tauar-detail', args=[str(self.id)])

    def __str__(self):
        return '{0},{1}'.format(self.tauar_name, self.tauar_address)


class Client(models.Model):
    name = models.CharField(max_length=200, help_text=" ")
    tauar= models.CharField(max_length=200, help_text=" ")


    class Meta:
        ordering = ["name","tauar"]

    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])

    def __str__(self):
        return '{0},{1}'.format(self.name,self.tauar)


