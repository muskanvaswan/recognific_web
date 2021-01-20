import datetime

from .query import attendance_day, attendance_month
from .reader import csv_writter, excel_writer


def attendance_sheet_day(date, classname):
    if date == 0 or date == "0":
        date = datetime.datetime.now().timetuple()
    qs = attendance_day(date, classname)
    file = open(f"media/Attendance/sheet_{classname}.csv", 'w+')
    file.write(f'{date[0]}/{date[1]}/{date[2]}, {classname}\n')
    file.write('Name, Date and Time \n')
    file.close()
    for q in qs:
        ls = [q.student.get_full_name(), q.time]
        csv_writter(ls, classname)
    excel_writer(classname)


def attendance_sheet_month(month, classname):
    if month == 0:
        month = datetime.datetime.now().timetuple().tm_mon
    qs = attendance_month(month, classname)
    file = open(f"media/Attendance/sheet_{classname}.csv", 'w+')
    file.write(f'for month {month}, {classname}\n')
    file.write('Name, Date and Time \n')
    file.close()
    for q in qs:
        ls = [q.student.get_full_name(), q.time]
        csv_writter(ls, classname)
    excel_writer(classname)
