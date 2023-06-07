from django.contrib.auth.models import AbstractUser
from django.db import models
from generator.models import Variant


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    favorites = models.ManyToManyField(Variant)

    def __str__(self):
        return self.username
