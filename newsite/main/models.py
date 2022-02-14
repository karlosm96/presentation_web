from pyexpat import model
from django.db import models

# Create your models here.
class contacto_info(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_phone = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class item(models.Model):
    contacto_info = models.ForeignKey(contacto_info, on_delete=models.CASCADE)
    name = models.CharField(max_length = 300)
    complete = models.BooleanField()

    def __str__(self):
        return self.name