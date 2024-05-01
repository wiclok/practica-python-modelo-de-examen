import pandas as pd
import csv
import datetime

fecha_actual = datetime.datetime.now().year

def import_data_over_25_years(archivo):
    with open(archivo, 'r', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile, delimiter=';', doublequote='"')
        cabecera = next(lector)
        age_and_fullname = []
        for fila in lector:
            age_and_fullname.append(fila)
        print(age_and_fullname)
        print(cabecera)

def ejecutar_programa():
    archivo = 'D:\Practica\Practica-Modelo-Examen-Python\edades.csv'
    import_data_over_25_years(archivo)


if __name__ == '__main__':
    ejecutar_programa()