import datetime
#from .models import Attendance
from encode.models import ClassSet


def attendance_day(day, class_id):
    attendees = ClassSet.objects.get(pk=class_id).attendees.all()
    day = datetime.date(day[0], day[1], day[2])
    return attendees.filter(time__gt=day)


def attendance_month(month, class_id):
    attendees = ClassSet.objects.get(pk=class_id).attendees.all()
    return attendees.filter(time__month=month)
