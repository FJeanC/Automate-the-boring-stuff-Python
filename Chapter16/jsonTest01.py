import json
import string
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'

jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)
pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie','felineIQ': None}
pythonToJson = json.dumps(pythonValue)
print(pythonToJson)