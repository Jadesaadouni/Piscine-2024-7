import json


Laureates=open('nobelLaureates.json')
data = json.load(Laureates)
print(type(data))
print (data ["laureates"][:5])
Laureates.close()

