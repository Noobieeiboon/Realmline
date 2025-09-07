from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MinLengthValidator

class User(AbstractUser):
    user_age = models.IntegerField(
        validators=[MinValueValidator(18)],
        default=18
    )
    user_bio = models.TextField(max_length=150)
    

    REQUIRED_FIELDS = ['email']
