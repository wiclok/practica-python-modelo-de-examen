import pandas as pd
import matplotlib.pyplot as plt
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

def frequency_of_age(sorted_by_age):
    frequency = {}
    for persona in sorted_by_age:
        if persona[0] in frequency:
            frequency[persona[0]] += 1
        else:
            frequency[persona[0]] = 1
    
    return frequency

def generate_DataFrame(frequency):
    edades = []
    for edad in frequency:
        edades.append(edad)
    
    fi = {}
    
    for i in edades:
        if i in fi:
            fi[i] += frequency[i]+1
        else:
            fi[i] = frequency[i]
    
    edades_keys = fi.keys()
    edades_values = fi.values()
    df = pd.DataFrame({'Edades': edades_keys, 'fi': edades_values})
    return df

def generate_graphic(DataFrame):
    plt.plot(DataFrame['Edades'], DataFrame['fi'])
    plt.xlabel('Edades')
    plt.ylabel('Frecuencia')
    plt.title('Frecuencia de edades')
    plt.show()

def ejecutar_programa():
    archivo = 'D:\\Practica\\Practica-Modelo-Examen-Python\\edades.csv'
    over_of_25_years = import_data_over_25_years(archivo)
    print('lista de personas con mas de 25 años: ', over_of_25_years)
    print('')
    sorted_by_age = order_by_age(over_of_25_years)
    print('Lista de edades ordenadas: ', sorted_by_age)
    print('')
    count_age_different = age_different(sorted_by_age)
    print('Cantidad de edades diferentes: ', count_age_different)
    frequency = frequency_of_age(sorted_by_age)
    print('Frecuencia de las edades: ', frequency)
    print('')
    DataFrame = generate_DataFrame(frequency)
    print('DataFrame creado con los datos de frecuencia de edades:')
    print(DataFrame)
    print('')
    generate_graphic(DataFrame)
    print('Grafico creado con exito')

if __name__ == '__main__':
    ejecutar_programa()