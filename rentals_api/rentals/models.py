from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (('owner', 'Owner'),
                    ('renter', 'Renter'),
#                    ('admin', 'Admin'),
                    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='renter')
    profile_picture = models.URLField(blank=True, null=True)
    contact_info = models.CharField(max_length=100, blank=True,null=True)

    def __str__(self):
        return f'{self.username} - Role: {self.role}'

class Rental(models.Model):
    STATUS_CHOICES = (('available', 'Available'),
                      ('booked', 'Booked'),
                      ('unavailable', 'Unavailable'),)
    TYPE_CHOICES = (('apartment', 'Apartment')
                    ('house', 'house')
                    ('self-con', 'self_con'))
    
