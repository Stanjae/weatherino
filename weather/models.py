from django.db import models

# Create your models here.

class History(models.Model):
    #measure = (('Fahrenheit','Fahrenheit'), ('Celsius','Celsius'), ('Kelvin','Kelvin'))
    name = models.CharField(max_length=30)
    #metrics = models.CharField(max_length=100, choices=measure, default="Fahrenheit")
    
    
    def __str__(self):
        return self.name