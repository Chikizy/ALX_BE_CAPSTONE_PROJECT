from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (('owner', 'Owner'),
                    ('tenant', 'Tenant'),
                    ('admin', 'Admin'),
                    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='tenant')
    contact_info = models.CharField(max_length=100, null=True)

class Rental(models.Model):
    STATUS_CHOICES = (('available', 'Available'),
                      ('booked', 'Booked'),
                      ('unavailable', 'Unavailable'),)
    TYPE_CHOICES = (('apartment', 'Apartment'),
                    ('house', 'house'),
                    ('self-con', 'self_con'),)
    
