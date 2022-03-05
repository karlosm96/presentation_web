from pyexpat import model
from django.db import models

# Create your models here.
class contacto_in(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=300)

    def __str__(self):
        return self.email