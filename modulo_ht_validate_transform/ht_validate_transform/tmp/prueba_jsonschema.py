import json
from io import open
from jsonschema import validate
from jsonschema._validators import Draft4Validator



cadena_json = json.load(open('metadata.json', encoding="utf8"))
# jsonSchema = pd.read_json(path, orient='split')
# for key,value in cadena_json.iteritems():
#     print('key',key)
#     # print('value',value)
#     if value == '$jsonSchema':
#         dato = value
#         print('value', value)
#     else:
#         print('no encontrado')
todo = []
for dato in cadena_json:
    todo.append(dato)
print(todo)