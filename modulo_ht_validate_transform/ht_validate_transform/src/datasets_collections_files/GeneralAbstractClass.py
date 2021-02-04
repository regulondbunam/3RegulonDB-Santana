import pandas as pd
from abc import ABC
import abc 


'''#

# name: GeneralAbstractClass.py	Version [1.0]

Clase que se encargara de leer los dataframes para asi poder tomar
los valor de inicio y fin, los cuales serviran para poder tomar el
data y el metadata de cada archivo.

```python
program_name [options list] arguments
```

## examples

```python
put here your code example
```

## description
Manipulacion de datos atraves de dataframes para poder tomar los valores de inicio
y fin para poder obtener metadata y data.

## arguments

No necesita de argumentos para la ejecuion de dicha clase 

## requirements
Sin requerimientos

## softwareRequirements

Se necesita la libreria de python llamadas

pandas - Es un paquete de Python que proporciona estructuras de datos similares a los dataframes de R. 
Pandas depende de Numpy, la librería que añade un potente tipo matricial a Python.
ABC - Biblioteca para mencionar clases astractas
abc - Bliniteca para asignar el la property a un metodo astracto

## memoryRequirements

Se recomienda al menos tener 8gb de ram para que el proceso se ejecute a una velocidad
estandar a la hora de correrlo.

#'''

class GeneralAbstractClass(ABC):
    def __init__(self, input_path, valid_path, output_path, js_metadata, js_data):
        self.input_path = input_path
        self.valid_path = valid_path
        self.output_path = output_path
        self.js_metadata = js_metadata
        self.js_data = js_data


    @abc.abstractmethod
    def get_collection_datasets(self):
        pass


    """
    Keyword arguments: dataframe, start_position, end_position
    argument -- Dataframe es el objeto con los datos a analizar,
    start_position es el valor inicial y end_position en el valor final.
    Return: Retorna un dataframe con los datos de data, tambien transforma
    la primera columna de datos como nombre de los indices de las filas del dataframe
    """
    def get_dataframe_metadata_iloc(self, dataframe, start_position, end_position):
        metadata_dataframe = dataframe.rename(index=dataframe.iloc[:, 0],
            columns=dataframe.iloc[3,:]).iloc[0:, 1:]
        metadata = metadata_dataframe.iloc[start_position : end_position, 0:2]
        return metadata
    

    """
    Keyword arguments: dataframe, start_position, end_position
    argument -- Dataframe es el objeto con los datos a analizar,
    start_position es el valor inicial y end_position en el valor final.
    Return: Retorna un dataframe con los datos de data y ademas transforma
    la primera fila de datos como nombre de las columnas del dataframe
    """
    def get_dataframe_data_iloc(self, dataframe, start_position, end_position):
        dataframe_data = dataframe.iloc[start_position: end_position, :]
        data_columns = dataframe_data.rename(columns=dataframe_data.iloc[0])
        df = dataframe.iloc[start_position: :,:]
        data_columns = df.rename(columns=dataframe_data.iloc[0])
        data = data_columns.iloc[1: :,:]
        return data
       

    """
    Keyword arguments: dataframe, sn="Dataset"
    argument -- Dataframe es el objeto con los datos a analizar,
    y sn es la hoja que se leera del archivo.
    Return: Retorna dos valores los cuales son dos valores, los cuales indican el punto de partida
    y finalizacion para tomar los datos que contendra el metadata.S
    """
    def get_metadata_indexes(self, dataframe, sn="Dataset"):
        valor_inicial = None
        valor_final = None
        for index,row in dataframe.iterrows():
            if str(row[0]).startswith("#"):
                if not valor_inicial:
                    valor_inicial = index
            elif valor_inicial:
                if not valor_final:
                    valor_final = index
            if valor_inicial and valor_final:
                return valor_inicial,valor_final
        return None


    """
    Keyword arguments: dataframe, sn="Dataset"
    argument -- Dataframe es el objeto con los datos a analizar,
    y sn es la hoja que se leera del archivo.
    Return: Retorna dos valores los cuales son dos valores, los cuales indican el punto de partida
    y finalizacion para tomar los datos que contendra el data.
    """
    def get_data_indexes(self, dataframe,sn="Dataset"):
        valor_inicial = None
        valor_final = None
        for index,row in dataframe.iterrows():
            if str(row[0]).startswith("!"):
                if not valor_inicial:
                    valor_inicial = index
            elif valor_inicial:
                if not valor_final:
                    valor_final = index
            if valor_inicial and valor_final:
                return valor_inicial,valor_final
        return None


'''#

dateCreated: [2020-12-02] -  author: [Santana Estrada Hernandez]

dateModified [2021-01-10] - contributor: [Se realizo una optimizacion de codigo]

#'''
