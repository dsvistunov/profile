from django.core.validators import RegexValidator
from django.db import models


class Profile(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_birth = models.DateField(
        null=True, blank=True
    )
    email = models.EmailField(max_length=30)
    skype = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15, blank=True)
    bio = models.TextField()
