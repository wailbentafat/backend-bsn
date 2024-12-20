from django.db import models
from django.contrib.auth.models import AbstractUser


from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    identity_card_number = models.CharField(max_length=50, unique=True)
    iscamp = models.BooleanField(default=False)

    objects = CustomUserManager()

    def __str__(self):
        return self.email
