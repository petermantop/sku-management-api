from django.db import models

class Sku(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    medication_name = models.CharField(max_length=500)
    dose = models.CharField(max_length=500)
    presentation = models.CharField(max_length=500)
    unit = models.CharField(max_length=50)
    countries = models.CharField(max_length=500)
    
    class Meta:
        ordering = ['created']