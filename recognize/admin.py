from django.contrib import admin

from .models import Attendance

# Register your models here.


class AttendanceAdmin(admin.ModelAdmin):
    fields = [
        'classname',
        'time',
        'student',
    ]

    readonly_fields = ['time', ]

    class Meta:
        model = Attendance


admin.site.register(Attendance, AttendanceAdmin)
