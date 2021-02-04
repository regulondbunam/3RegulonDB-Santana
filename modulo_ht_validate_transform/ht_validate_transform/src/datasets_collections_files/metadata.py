import pandas as pd
import json

'''#

# name: Metadata.py	Version [1.0]

Clase que se encargara de recibir un dataframe con datos del metadata y se encargara
de manipularlos y poder crear un dataframe con los datos del metadadata estructurados como
se requieren.

```python
program_name [options list] arguments
```

## examples

```python
put here your code example
```

## description
Manipulacion de datos atraves de dataframes para poder crear el metadata

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

class Metadata():
  
    DATASET_TITLE = "#DATASET TITLE"
    PMID = "#PMID:"
    CORRESPONDING_AUTHOR = "#CORRESPONDING AUTHOR (EMAIL):"
    STRAIN = "#STRAIN:"
    REFERENCE_GENOME = "#REFERENCE GENOME:"
    DATASET_ACCESION_NUMBER = "#DATASET ACCESION NUMBER[DATABASE]:"
    EXPERIMENTAL_DETAILS = "#EXPERIMENTAL DETAILS"
    METHOD = "#METHOD:"
    METHOD_DETAILS = "#METHOD DETAILS:"
    INSTRUMENT = "#INSTRUMENT:"
    EVIDENCE = "#EVIDENCE:"
    STATISTICAL_MODEL = "#STATISTICAL MODEL"
    VALUE_COLUMN = 'Value'

    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.title = dataframe
        self.pmid = dataframe
        self.corresponding_author = dataframe
        self.strain = dataframe
        self.reference_genome = dataframe
        self.dataset_accesion_number = dataframe
        self.experiment_details = dataframe
        self.method = dataframe
        self.method_details = dataframe
        self.instrument = dataframe
        self.evidence =dataframe
        self.statistical_model = dataframe

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, dataframe):
        try:
            self._title = dataframe.at[Metadata.DATASET_TITLE, Metadata.VALUE_COLUMN]
        except KeyError:
            self._title = None

    @property
    def pmid(self):
        return self._pmid

    @pmid.setter
    def pmid(self, dataframe):
        try:
            self._pmid = dataframe.at[Metadata.PMID, Metadata.VALUE_COLUMN]
        except KeyError:
            self._pmid = None

    @property
    def corresponding_author(self):
        return self._corresponding_author

    @corresponding_author.setter
    def corresponding_author(self, dataframe):
        try:
            self._corresponding_author = dataframe.at[Metadata.CORRESPONDING_AUTHOR, Metadata.VALUE_COLUMN]
        except KeyError:
            self._corresponding_author = None

    @property
    def strain(self):
        return self._strain

    @strain.setter
    def strain(self, dataframe):
        try:
            self._strain = dataframe.at[Metadata.STRAIN, Metadata.VALUE_COLUMN]
        except KeyError:
            self._strain = None

    @property
    def reference_genome(self):
        return self._reference_genome

    @reference_genome.setter
    def reference_genome(self, dataframe):
        try:
            self._reference_genome = dataframe.at[Metadata.REFERENCE_GENOME, Metadata.VALUE_COLUMN]
        except KeyError:
            self._reference_genome = None

    @property
    def dataset_accesion_number(self):
        return self._dataset_accesion_number

    @dataset_accesion_number.setter
    def dataset_accesion_number(self, dataframe):
        try:
            self._dataset_accesion_number = dataframe.at[Metadata.DATASET_ACCESION_NUMBER, Metadata.VALUE_COLUMN]
        except KeyError:
            self._dataset_accesion_number = None

    @property
    def experiment_details(self):
        return self._experiment_details

    @experiment_details.setter
    def experiment_details(self, dataframe):
        try:
            self._experiment_details = dataframe.at[Metadata.EXPERIMENTAL_DETAILS, Metadata.VALUE_COLUMN]
        except KeyError:
            self._experiment_details = None

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, dataframe):
        try:
            self._method = dataframe.at[Metadata.METHOD, Metadata.VALUE_COLUMN]
        except KeyError:
            self._method = None

    @property
    def method_details(self):
        return self._method_details

    @method_details.setter
    def method_details(self, dataframe):
        try:
            self._method_details = dataframe.at[Metadata.METHOD_DETAILS, Metadata.VALUE_COLUMN]
        except KeyError:
            self._method_details = None

    @property
    def instrument(self):
        return self._instrument

    @instrument.setter
    def instrument(self, dataframe):
        try:
            self._instrument = dataframe.at[Metadata.INSTRUMENT, Metadata.VALUE_COLUMN]
        except KeyError:
            self._instrument = None

    @property
    def evidence(self):
        return self._evidence

    @evidence.setter
    def evidence(self, dataframe):
        try:
            self._evidence = dataframe.at[Metadata.EVIDENCE, Metadata.VALUE_COLUMN]
        except KeyError:
            self._evidence = None

    @property
    def statistical_model(self):
        return self._statistical_model

    @statistical_model.setter
    def statistical_model(self, dataframe):
        try:
            self._statistical_model = dataframe.at[Metadata.STATISTICAL_MODEL, Metadata.VALUE_COLUMN]
        except KeyError:
            self._statistical_model = None

    def __call__(self): 
        metadata_frame = {
            'title': self.title,
            'pmid': self.pmid,
            'author': self.corresponding_author,
            'strain': self.strain,
            'reference genome': self.reference_genome,
            'dataset accesion number': self.dataset_accesion_number,
            'experiment details': self.experiment_details,
            'method': self.method,
            'method details': self.method_details,
            'instrument': self.instrument,
            'evidence': self.evidence,
            'statistical model': self.statistical_model
        }

        return metadata_frame 
      
'''#

dateCreated: [2020-12-22] -  author: [Santana Estrada Hernandez]

dateModified [2021-01-07] - contributor: [Se realizo una optimizacion de codigo]

#'''
                