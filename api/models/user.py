from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


from django.contrib.auth.models import BaseUserManager


# Create your models here.



class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, username=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, password=password, **extra_fields)
        user.save(using=self._db)
        return user

    def create_user(self, email, username=None, password=None, **extra_fields):
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(_("email address"), blank=True, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
        
    objects = UserManager()

    def save(self, *args, **kwargs):
        if not self.pk and not self._password: 
            self.set_password(self.password)
        else: 
            old_user = self.__class__.objects.filter(pk=self.pk).first()
            if self.password != old_user.password:
                self.set_password(self.password)

        # Ensure that a superuser is always staff
        if self.is_superuser and not self.is_staff:
            self.is_staff = True

        super().save(*args, **kwargs)
    

class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')
    position = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    
    def __str__(self):
        return self.user.username
