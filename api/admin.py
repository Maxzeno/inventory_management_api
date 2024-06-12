from django.contrib import admin
from api import models 

# Register your models here.

admin.site.register(models.user.User)
admin.site.register(models.user.EmployeeProfile)
admin.site.register(models.inventory.Supplier)
admin.site.register(models.inventory.Item)
