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
            age = fecha_actual - int(fila[0].split(',')[0].split('/')[2])
            name = fila[0].split(',')[1]
            age_of_birthday = fila[0].split(',')[0]
            age_and_fullname.append([age, name, age_of_birthday])
        
        over_of_25_years = []
        for person in age_and_fullname:
            if person[0] >= 25:
                over_of_25_years.append(person)
        
        return over_of_25_years

def order_by_age(over_of_25_years):
    sorted_by_age = sorted(over_of_25_years, key=lambda x: x[0])
    return sorted_by_age

def age_different(sorted_by_age):
    different_age = set()

    for persona in sorted_by_age:
        different_age.add(persona[0])  # Agrega la edad al conjunto de edades únicas

    count_age_different = len(different_age)
    
    return count_age_different

def ejecutar_programa():
    archivo = 'D:\\Practica\\Practica-Modelo-Examen-Python\\edades.csv'
    over_of_25_years = import_data_over_25_years(archivo)
    
    sorted_by_age = order_by_age(over_of_25_years)

    age_different(sorted_by_age)
if __name__ == '__main__':
    ejecutar_programa()