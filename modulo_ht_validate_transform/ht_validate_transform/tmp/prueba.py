import os
import logging
from src.utils import file_handler
from src.utils import arguments
from dotenv import load_dotenv
from src.datasets_collections_files.geneExpressionContrast import GeneExpressionContrast

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
    input_path = kwargs.get('input_path', None)
    valid_output_path = kwargs.get('outputValid', None)
    invalid_output_path = kwargs.get('outputInValid', None)
    js_metadata = kwargs.get('jsonSchema_metadata', None)
    js_data = kwargs.get('jsonSchema_data', None)
    log = kwargs.get('file_log', None)

    logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s',filename=log, level=logging.INFO)
    logging.info('Started')
    dataset_type = kwargs.get("datasets_type", None)

    try:
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
        "file_log":args.log,
        "multigenomicdb_user": os.getenv("MULTIGENOMICDB_USER"),
        "multigenomicdb_pass": os.getenv("MULTIGENOMICDB_PASS"),
        "identifiersdb_user": os.getenv("IDENTIFIERS_USER"),
        "identifiersdb_pass": os.getenv("IDENTIFIERS_PASS")
    }

    run(**lista_variables_ejecucion)
