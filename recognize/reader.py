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

def csv_writter(ls):
    with open('Attendance/sample.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(ls)
        excel_writer()

def excel_writer():
    # Reading the csv file
    read_file = pd.read_csv('Attendance/sample.csv')

    # saving xlsx file
    read_file.to_excel('Attendance/sample.xlsx', index = None,header=True)
