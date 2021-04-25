import re, os, json

path = "/path/to/pdf"
dirs = os.listdir( path )

with open('api.json') as f:
    data = json.load(f)

for carta in data:
    id_carta = carta['id_carta']
    pdf = carta['digitalitzacio']
    newName = path + '/' + str(pdf)

    # Llistem els arxius de la carpeta
    for file in dirs:
        res = re.split('(\d+)', file)
       
        # Ignorem arxius que no son cartes
        if(len(res)>1):
            id_file = res[1]

        if id_file == id_carta: 
            os.rename(file, newName)
