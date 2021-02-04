import os
from src.utils import file_handler
from src.utils import arguments
from dotenv import load_dotenv
from src.datasets_collections_files.geneExpressionContrast import GeneExpressionContrast
'''#

# name: __main__.py	Version [1.0]

Es el programa principal, debido a que se encargara de ejecutar todo el modulo llamando a 
los programas o metodos secundarios

```python
program_name [options list] arguments
```

## examples

```python
put here your code example
```

## description
Este programa cuenta con su funcion principal, la cual se encarga
de cargar la clase arguments.py, la cual contiene los argumentos
requeridos para la ejecuion del modulo.
Tambien crea un diccionario llamado datasets_process, el cual crea
un listados de todos los diferentes tipos de archivos que leera la 
la clase y se encarga de asiganar a cada archivo con el nombre del 
mismo. Se le da vida al metodo run, el cual se encarga de inicializar 
los ragumentos a necesitar y de llamar a diferectes clases creadas 
en otras carpetas para llevar acabo la ejecucion

## arguments

* __input__ Ruta absoluta del directorio que contiene los archivos a procesar

* __schemas__ Muestra los schemas con los cuales contamos

* __type__ Es el tipo de archivo que se manipulara

* __outputValid__ Datos validos

* __outputInValid__ Datos no validos

* __jsonSchema_metadata__ Esquemas para validar metadata

* __jsonSchema_data__ Esquemas para validar data

## requirements
Los requerimentos son los argumentos que se necesitan para 
la ejecucion y almacenamiento de informacion, duran la ejecucion
del modulo.

## softwareRequirements
Las clases secundarias para poder llevar a cabo la ejecucion de la clase son

os - Este módulo proporciona una forma portátil de utilizar la funcionalidad 
dependiente del sistema operativo.

file_handler - Clase contenedora de los metodos de lectura de archivos.
arguments - Clase contenedora de los argumentos del modulo.
load_dotenv - Credenciales para la gestion de Identifiers API
GeneExpressionContrast - Clase contenedora con los metodos de manipulacion de
dataframes y creacion de archivos JSON.

## memoryRequirements

Se recomienda al menos tener 8gb de ram para que el proceso se ejecute a una velocidad
estandar a la hora de correrlo.

## storageRequirements
No se requiere mucho espacio para el almacenamiento debido a que el resultado de la ejecucion
son archivos JSON.

* __Input Format - __ __[Name]__ Description

El formato de entrada son un carpeta con n archivos de diferentes tipos, las rutas donde 
se colocaran los JSON validados y los No validados, asi como tambien las rutas donde se 
encuentran los JSONSchemas los cuales se encargaran de validar los datos obtenidos, la 
ruta donde se estara generando nuestro archivo Log, el cual se encargara de controlar la 
bitacora de ejcucion del modulo.

* __Format - __ __[Name]__ Description

__Return:__

__Type -__  __[Name]__ Description

## [Program Code]

#'''

load_dotenv()

datasets_process = {
    'geneExpression':"",
    'tfBinding': "",
    'regulatoryInteraction': "",
    'transcriptionUnit': "",
    'transcriptionStartSite': "",
    'transcriptionTerminatorSite': "",
    'geneExpressionContrast': GeneExpressionContrast,
    'tfBindingContrast': "",
    'regulatoryInteractionContrast': "",
    'transcriptionUnitContrast': "",
    'transcriptionStartSiteContrast': "",
    'transcriptionTerminatorSiteContrast': "",
}


def run(**kwargs):
    dataset_type = kwargs.get("datasets_type", None)

    try:
        input_path = kwargs.get('input_path', None)
        valid_output_path = kwargs.get('outputValid', None)
        invalid_output_path = kwargs.get('outputInValid', None)
        js_metadata = kwargs.get('jsonSchema_metadata', None)
        js_data = kwargs.get('jsonSchema_data', None)
        datasets = datasets_process[dataset_type](input_path,valid_output_path,invalid_output_path,js_metadata,js_data)
        datasets.get_collection_datasets()
        datasets.transform_json_valid_o_invalid()
        

    except KeyError:
        raise KeyError("Argument Type(Dataset Type) value not valid")


if __name__ == "__main__":
    args = arguments.load_arguments()

    lista_variables_ejecucion = {
        "input_path": args.input,
        "datasets_type": args.type,
        "outputValid":args.valid_output_path,
        "outputInValid":args.invalid_output_path,
        "jsonSchema_metadata":args.js_metadata,
        "jsonSchema_data":args.js_data,
        "multigenomicdb_user": os.getenv("MULTIGENOMICDB_USER"),
        "multigenomicdb_pass": os.getenv("MULTIGENOMICDB_PASS"),
        "identifiersdb_user": os.getenv("IDENTIFIERS_USER"),
        "identifiersdb_pass": os.getenv("IDENTIFIERS_PASS")
    }

    run(**lista_variables_ejecucion)

'''#

dateCreated: [2020-11-20] -  author: [Santana Estrada Hernandez]

dateModified [2021-01-10] - contributor: [Se realizo una optimizacion de codigo]

#'''


