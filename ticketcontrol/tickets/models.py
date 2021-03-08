from django.db import models

# Create your models here.
class Ticket(models.Model):
    creation_date = models.DateTimeField(auto_now=True)
    customer_name = models.CharField(max_length=100)
    performance_title = models.CharField(max_length=100)
    performance_time = models.DateTimeField()
    price = models.PositiveIntegerField()

class User(models.Model):
    pass