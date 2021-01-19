import pickle
import csv
import pandas as pd


def reading_encodings(path):
    # reading the data from the file
    with open(f'encodings/{path}.txt', 'rb') as handle:
        data = handle.read()
    # reconstructing the data as dictionary
    d = pickle.loads(data)
    return d


def csv_writter(q, classname):
    with open(f'Attendance/sheet_{classname}.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(q)


def excel_writer(classname):
    # Reading the csv file
    read_file = pd.read_csv(f'Attendance/sheet_{classname}.csv')

    # saving xlsx file
    read_file.to_excel(f'Attendance/sheet_{classname}.xlsx', index=None, header=True)
