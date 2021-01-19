import datetime

from .query import attendance_day
from .reader import csv_writter, excel_writer


def attendance_sheet_day(date, classname):
    date = datetime.datetime(2021, 1, 15).timetuple()
    qs = attendance_day(date, classname)
    print("qs", qs)
    file = open(f"Attendance/sheet_{classname}.csv", 'w+')
    file.write(f'{date[0]}/{date[1]}/{date[2]}, {classname}\n')
    file.write('Name, Date and Time \n')
    file.close()
    for q in qs:
        ls = [q.student.get_full_name(), q.time]
        csv_writter(ls, classname)
    excel_writer(classname)
