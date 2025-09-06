from django.db import models
from django.conf import settings

# Create your models here.

class RentalListing(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='listing' )
    title = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=250)
    price_per_night = models.DecimalField(max_digits=5, decimal_places=2)
    availability_dates = models.JSONField(default=dict)
    #   date of creation of listing(auto_now_add -- allows a permanent timestamp for time of creation)
    created_at = models.DateTimeField(auto_now_add=True)
    #   "auto_now" allows the update time to be updated every time an update is done
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title