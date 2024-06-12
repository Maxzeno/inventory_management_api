from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(_("email address"), blank=True, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
        
    def save(self, *args, **kwargs):
        # Ensure that the password is set correctly
        if not self.pk:  # Check if the user instance is being created
            self.set_password(self.password)
        else:  # Check if the user instance is being updated
            old_user = self.__class__.objects.get(pk=self.pk)
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
