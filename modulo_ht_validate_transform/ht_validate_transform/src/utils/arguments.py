import argparse

'''#

# name: arguments.py	Version [1.0]

Programa que se encargara de crear los argumentos necesarios
para llevar a cabo la ejecucion del modulo.

```python
program_name [options list] arguments
```

## examples

```python
put here your code example
```

## description
creacion y implementacion de los arguments solicitados para la ejecuion
del programa a realizar

## arguments

No necesita de argumentos para la ejecuion de dichac clase 

## requirements
Sin requerimientos

## softwareRequirements

Se necesita la libreria de python llamada argparse , este modulo
módulo facilita la escritura de interfaces de línea de comandos fáciles de usar. 
El programa define qué argumentos necesita y argparse descubrirá cómo analizarlos 
sys.argv. El argparse módulo también genera automáticamente mensajes de ayuda y 
uso y emite errores cuando los usuarios dan al programa argumentos no válidos.

## memoryRequirements

Se recomienda al menos tener 8gb de ram para que el proceso se ejecute a una velocidad
estandar a la hora de correrlo.

#'''

def load_arguments():
    parser = argparse.ArgumentParser(description="Argumentos del proyecto RegulonDB-HT")
    parser.add_argument(
        '-i', '--input',
        help='Ruta absoluta del directorio que contiene los archivos a procesar'
    )

    parser.add_argument(
        '-s', '--schemas',
        help='Muestra los schemas con los cuales contamos'
    )

    parser.add_argument(
        '-t',
        '--type',
        choices=[
            'geneExpression',
            'tfBinding',
            'regulatoryInteraction',
            'transcriptionUnit',
            'transcriptionStartSite',
            'transcriptionTerminatorSite',
            'geneExpressionContrast',
            'tfBindingContrast',
            'regulatoryInteractionContrast',
            'transcriptionUnitContrast',
            'transcriptionStartSiteContrast',
            'transcriptionTerminatorSiteContrast'],
        help='Es el tipo de archivo que se manipulara',
        required=True
    )

    parser.add_argument(
        '-out', '--outputValid',
        help='Datos validos',
        dest='valid_output_path'
    )

    parser.add_argument(
        '-o', '--outputInValid',
        help='Datos no validos',
        dest='invalid_output_path'
    )

    parser.add_argument(
        '-js_metadata', '--jsonSchema_metadata',
        help='Esquemas para validar metadata',
        dest='js_metadata'
    )

    parser.add_argument(
        '-js_data', '--jsonSchema_data',
        help='Esquemas para validar data',
    dest='js_data'
    )

    parser.add_argument(
        '-log', '--file_log',
        help='Archivo que nos dice lo ejecutado en el codigo',
    dest='log'
    )
    arguments = parser.parse_args()
    return arguments

'''#

dateCreated: [2020-11-13] -  author: [Santana Estrada Hernandez]

dateModified [2020-11-18] - contributor: [Se realizo una optimizacion de codigo]

#'''
