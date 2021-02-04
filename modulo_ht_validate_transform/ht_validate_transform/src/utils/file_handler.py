import pandas as pandas
import os

'''#

# name: file_handler.py	Version [1.0]

Clase que se encargara de recibir y leer una carpeta de archivos que contiene
todos los archivos de diferentes tipos a procesar, y asi dependiendo su tipo
poder determinar que tipo de metodo aplicar para cada archivo.

```python
program_name [options list] arguments
```

## examples

```python
put here your code example
```

## description
Manipulacion de archivos de diferentes tipos.

## arguments

No necesita de argumentos para la ejecuion de dicha clase 

## requirements
Sin requerimientos

## softwareRequirements

Se necesita la libreria de python llamadas

os - Este módulo proporciona una forma portátil de utilizar la funcionalidad dependiente del sistema operativo.
json - Es un formato de intercambio de datos ligero inspirado en la sintaxis literal de objetos de JavaScript.

## memoryRequirements

Se recomienda al menos tener 8gb de ram para que el proceso se ejecute a una velocidad
estandar a la hora de correrlo.

#'''

"""
Keyword arguments: path, file_name
argument -- Path es la ruta donde se encuentra el archivo a procesar,
file_name es el tipo de archivo a procesar.
Return: Retorna un objeto de tipo dataframe del archivo procesado
"""
def get_dataframe_by_txt(path, file_name):
    df = pandas.read_csv(os.path.join(path, file_name))
    dataframe = df.where(pandas.notnull(df), None)
    return dataframe


"""
Keyword arguments: path, file_name, sn="Dataset"
argument -- Path es la ruta donde se encuentra el archivo a procesar,
file_name es el tipo de archivo a procesar y sn es la hoja que se leera del archivo.
Return: Retorna un objeto de tipo dataframe del archivo procesado.
"""
def get_dataframe_by_xlsx(path, file_name, sn="Dataset"):
    df = pandas.read_excel(os.path.join(path, file_name), sheet_name=sn, na_values=['*'])
    dataframe = df.where(pandas.notnull(df), None)
    return dataframe


"""
Keyword arguments: path, file_name, sn="Dataset"
argument -- Path es la ruta donde se encuentra el archivo a procesar,
file_name es el tipo de archivo a procesar y sn es la hoja que se leera del archivo.
Return: Retorna un objeto de tipo dataframe del archivo procesado.
"""
def get_dataframe_by_csv(path, file_name, sn="Dataset"):
    df = pandas.read_csv(os.path.join(path, file_name), sheet_names=sn, na_values=['*'])
    dataframe = df.where(pandas.notnull(df), None)
    return dataframe


"""
# TODO: Este metodo o funcion implementar logica para determinar si se trata de xls, tsv, txt
:param ruta: el parametro path que recibe es la ruta que contiene un directorio de archivos que 
    se encargara de leer este metodo.
:param file_type: possible values: txt, xls, tsv
:return {key: value} key = nombre del archivo, value = dataframes
"""
def read_files(path):
    files_in_path = os.listdir(path)
    ht_dataframes = {}
    for file_name in files_in_path:
        valores = file_name
        if file_name.endswith(".xlsx"):
            dataframe = get_dataframe_by_xlsx(path, file_name)
            ht_dataframes.setdefault(file_name, dataframe)
            # ht_dataframes[file_name] = dataframe
        if file_name.endswith(".txt"):
            dataframe = get_dataframe_by_txt(path, file_name)
            ht_dataframes.setdefault(file_name, dataframe)
        if file_name.endswith(".csv"):
            dataframe = get_dataframe_by_csv(path, file_name)
            ht_dataframes.setdefault(file_name, dataframe)
    return ht_dataframes
    

'''#

dateCreated: [2020-12-20] -  author: [Santana Estrada Hernandez]

dateModified [2020-12-29] - contributor: [Se realizo una optimizacion de codigo]

#'''