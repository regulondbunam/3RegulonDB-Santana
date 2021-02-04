import pandas as pd
import json

'''#

# name: data.py	Version [1.0]

Clase que se encargara de recibir un dataframe con datos del data y se encargara
de manipularlos y poder crear un dataframe con los datos del data estructurados como
se requieren.

```python
program_name [options list] arguments
```

## examples

```python
put here your code example
```

## description
Manipulacion de datos atraves de dataframes para poder crear el data

## arguments

No necesita de argumentos para la ejecuion de dicha clase 

## requirements
Sin requerimientos

## softwareRequirements

Se necesita la libreria de python llamadas

pandas - Es un paquete de Python que proporciona estructuras de datos similares a los dataframes de R. 
Pandas depende de Numpy, la librería que añade un potente tipo matricial a Python.

json - Es un formato de intercambio de datos ligero inspirado en la sintaxis literal de objetos de JavaScript

## memoryRequirements

Se recomienda al menos tener 8gb de ram para que el proceso se ejecute a una velocidad
estandar a la hora de correrlo.

#'''

class Data():
    
    TARGET_COLUM = 'Target_gene'
    EFFECT_COLUMN = 'Effect' 
    LOG2_COLUMN = 'log2 Fold Change'
    THERESHOLD_COLUMN = 'Threshold'
    COMPARISON_COLUM = 'Comparison order'
    GCS_CONTROL_COLUMN = 'GCs(Control)'
    GCS_EXPERIMENTAL_COLUMN = 'GCs(Experimental)' 
    VARIABLE_COLUMN = 'Variable' 
    FDR_COLUMN = 'FDR'
    BNUMBER_COLUMN = 'bnumber' 
    OPERON_COLUMN = 'operon' 
    START_COLUMN = 'Start' 
    END_COLUMN = 'End' 
    LENGTH_COLUMN = 'Length'

    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.data = dataframe

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, dataframe):
        data = []
        for index,row in dataframe.iterrows():
            gene_expression = {
                Data.TARGET_COLUM : row['!Target_gene*'],
                Data.EFFECT_COLUMN : row['Effect*'],
                Data.LOG2_COLUMN : row['log2 Fold Change*'],
                Data.THERESHOLD_COLUMN : row['Threshold*'],
                Data.COMPARISON_COLUM : row['Comparison order*'],
                Data.GCS_CONTROL_COLUMN : row['GCs (Control)**'],
                Data.GCS_EXPERIMENTAL_COLUMN : row['GCs (Experimental)**'],
                Data.VARIABLE_COLUMN : row['Variable'],
                Data.FDR_COLUMN : row['FDR'],
                Data.BNUMBER_COLUMN : row['bnumber'],
                Data.OPERON_COLUMN : row['operon'],
                Data.START_COLUMN : row['Start'],
                Data.END_COLUMN: row['End'],
                Data.LENGTH_COLUMN : row['Length']
            }
            data.append(gene_expression)
        self._data = data

    def __call__(self): 
        return self.data
      
'''#

dateCreated: [2020-12-25] -  author: [Santana Estrada Hernandez]

dateModified [2021-01-06] - contributor: [Se realizo una optimizacion de codigo]

#'''

    
                