import csv
import os
import json


def GenerarJson(archivo):
	columnas=[]
	with open(archivo, 'r',encoding='latin-1') as f:
		#solo para este caso
		d_reader = csv.DictReader(f,delimiter=';')
		
		columnas = d_reader.fieldnames
		row1 = next(d_reader)

	dic={"recurso":{
			"displayName":archivo,
			"description":" ",
			"attributesDescription": []
			},
		"organizacion":{
			"name":" "
			}
		}
	
	listaTipos=[]

	for i in columnas:
		dic['recurso']['attributesDescription'].append({"title": i,"description":i, "type": "string"})

	return dic


listaArchivos=os.listdir()
listaArchivos.remove('generador_metadatos_json.py')
listaArchivos.remove('.git')

print(listaArchivos)

for archivo in listaArchivos:
	myjson=GenerarJson(archivo)
	x = open("metadata_"+archivo+".json", "w",encoding='latin-1')
	x.write(json.dumps(myjson, indent=3))
	x.close()