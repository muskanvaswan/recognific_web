from django.contrib import admin

from django.contrib.auth.models import Group
from .models import Teacher
# Register your models here.
admin.site.register(Teacher)
admin.site.unregister(Group)
