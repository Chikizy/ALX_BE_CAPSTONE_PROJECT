from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (('landlord', 'Landlord'),
                    ('tenant', 'Tenant'),
                    ('admin', 'Admin'),
                    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='tenant')

class Rental(models.Model):
    STATUS_CHOICES = (('available', 'Available'),
                      ('booked', 'Booked'),
                      ('unavailable', 'Unavailable'),)
    TYPE_CHOICES = (('apartment', 'Apartment')
                    ('house', 'house')
                    ('self-con', 'self_con'))
    
