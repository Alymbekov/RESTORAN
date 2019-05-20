from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Administrator'),
        (2, 'Chef'),
        (3, 'Waiter'),
    )
    email = models.CharField(max_length=50)

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=3)
