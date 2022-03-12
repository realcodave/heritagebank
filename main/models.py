from django.db import models

# Create your models here.

class Statement(models.Model):
    CHOICES = (
        ('SU', 'SuccessFul'),
        ('US', 'Unsuccessful'),
        
    )
    TYPE = (
        ('Transfer', 'Transfer'),
        ('Withdraw', 'Withdraw'),
    )
    description = models.CharField(max_length=30000)
    amount = models.IntegerField()
    date_created = models.DateTimeField()
    successful = models.CharField(blank=True, null=True, max_length=300, choices = CHOICES)
    alert = models.CharField(blank=True, null=True, max_length=300, choices = TYPE)

class Amount(models.Model):
    amount = models.CharField(max_length=30000)

