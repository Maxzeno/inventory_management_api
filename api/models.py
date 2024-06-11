from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(_("email address"), blank=True, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    

class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.user.username
