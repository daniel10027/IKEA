from django.db import models
from django.contrib.auth.models import User


# models.py

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.user.username


# Create your models here.
class Customer(models.Model):
    """Model definition for Customer."""
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=254 , null=True)
    contact = models.CharField(max_length=50, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Customer."""

        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        """Unicode representation of Customer."""
        try:
            return self.name 
        except:
            return ""


    def get_absolute_url(self):
        """Return absolute url for Customer."""
        return ('')

    # TODO: Define custom methods here
