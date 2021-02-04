from abc import ABC, abstractmethod
import pandas as pd
import json
import logging
from io import open
import jsonschema 
from src.datasets_collections_files.GeneralAbstractClass import GeneralAbstractClass
from src.datasets_collections_files.metadata import Metadata
from src.datasets_collections_files.data import Data
from src.utils import file_handler

'''#

# name: geneExpresionContrast.py	Version [1.0]

Clase que se encargara de enviar la carpeta de la ruta con los archivos,
obtencion de los indices para poder tomar el metadata y data de los archivos
y poder crea un diccionario con ellos.
Tambien se encargara de validar si el matadata y data contienen datos validos
mediante JSONSchemas, confirmando esto creara un archivo JSON con los datos
validos o no validos.

```python
program_name [options list] arguments
```

## examples

```python
put here your code example
```

## description
Manipulacion de datos atraves de dataframes para poder tomar su data y metada
de cada archivo, validarlos y poder generar un JSON con dichos datos.

## arguments

No necesita de argumentos para la ejecuion de dicha clase 

## requirements
Sin requerimientos

## softwareRequirements

Se necesita la libreria de python llamadas

ABC - Biblioteca para mencionar clases astractas
abstractmethod - Biblioteca para mencionar metodos astractos
pandas - Es un paquete de Python que proporciona estructuras de datos similares a los dataframes de R. 
Pandas depende de Numpy, la librería que añade un potente tipo matricial a Python.

json - Es un formato de intercambio de datos ligero inspirado en la sintaxis literal de objetos de JavaScript
logging -  Es una herramienta útil para prevenir errores, controlar los ataques de piratas informáticos o, simplemente, 
llevar a cabo análisis. 
open - Modulo que nos ayuda a abrir archivos JSON
jsonschema - Modulo para poder trabajar con los JSONSchema que nos ayudan a validar los datos
GeneralAbstractClass - Clase astracta creada en este modulo Para gestionar metodos
Metadata - Clase que nos ayuda a generar el Metadata de los archivos
Data - Clase que nos ayuda a generar el Data de los archivos
file_handler - Clase que nos ayuda a leer los archivos y decirnos que tipo de archivo cargamos

## memoryRequirements

Se recomienda al menos tener 8gb de ram para que el proceso se ejecute a una velocidad
estandar a la hora de correrlo.

#'''

class GeneExpressionContrast(GeneralAbstractClass):

    def __init__(self,input_path, valid_output_path, invalid_output_path,js_metadata,js_data):
        self.input_path = input_path
        self.valid_output_path = valid_output_path
        self.invalid_output_path = invalid_output_path
        self.js_metadata = js_metadata
        self.js_data = js_data
        self.dataframes = input_path
        
    
    @property
    def dataframes(self):
        return self._dataframes


    @dataframes.setter
    def dataframes(self,input_path):
        self._dataframes = file_handler.read_files(input_path)
        

    @property
    def dictionary(self):
        return self._dictionary 


    def get_collection_datasets(self):
        
        dictionary_format = {}
        for filename, dataframe in self.dataframes.items():
            start_position_metadata, end_position_metadata = self.get_metadata_indexes(dataframe)
            start_position_data, end_position_data  = self.get_data_indexes(dataframe)
            metadata = self.get_dataframe_metadata_iloc(dataframe, start_position_metadata, end_position_metadata)
            data = self.get_dataframe_data_iloc(dataframe, start_position_data, end_position_data)
            metadata_object = Metadata(metadata)
            data_object = Data(data)

            dictionary_format[filename] = { 'metadata' : metadata_object(),'data' : data_object()}

        self.new_dictionary = dictionary_format
        return (dictionary_format)


    def transform_json_valid_o_invalid(self):
        for filename, dataframe in self.dataframes.items():
            start_position_metadata, end_position_metadata = self.get_metadata_indexes(dataframe)
            start_position_data, end_position_data  = self.get_data_indexes(dataframe)
            metadata = self.get_dataframe_metadata_iloc(dataframe, start_position_metadata, end_position_metadata)
            data = self.get_dataframe_data_iloc(dataframe, start_position_data, end_position_data)
            metadata_object = Metadata(metadata)
            data_object = Data(data)

            jsonS_metadata = open(self.js_metadata) 
            schema_metadata = json.load(jsonS_metadata) 

            jsonS_data = open(self.js_data) 
            schema_data = json.load(jsonS_data)
            
            try:
            
                schema_m= jsonschema.validate(instance=metadata_object(), schema=schema_metadata, format_checker=jsonschema.draft4_format_checker)
                schema_d = jsonschema.validate(instance=data_object(), schema=schema_data, format_checker=jsonschema.draft4_format_checker)

                logging.info('Archivo ' + filename + ' validado')

                with open(self.valid_output_path, 'w', encoding='utf-8') as file:
                    json.dump(self.new_dictionary, file)
                logging.info('Finished')
            except jsonschema.exceptions.ValidationError:
                logging.info('Archivo ' + filename + ' no validado')
                print('error en el match con los schemas')
                with open(self.invalid_output_path, 'w', encoding='utf-8') as file:
                    json.dump(self.new_dictionary, file)
                logging.info('Finished')
'''#

dateCreated: [2020-11-12] -  author: [Santana Estrada Hernandez]

dateModified [2021-09-01] - contributor: [Se realizo una optimizacion de codigo]

#'''
