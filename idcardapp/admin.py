from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Department, Employee

admin.site.register(User)
admin.site.register(Department)
admin.site.register(Employee)
