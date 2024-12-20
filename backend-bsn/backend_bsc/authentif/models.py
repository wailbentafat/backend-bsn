from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, identity_card_number, password=None):
        if not email:
            raise ValueError("The Email field must be set")
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            identity_card_number=identity_card_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, identity_card_number, password=None):
        user = self.create_user(
            email,
            first_name,
            last_name,
            identity_card_number,
            password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    identity_card_number = models.CharField(max_length=50, unique=True)
    iscamp = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['first_name', 'last_name', 'identity_card_number']

    def __str__(self):
        return self.email
