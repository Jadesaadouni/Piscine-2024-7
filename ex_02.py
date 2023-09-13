import json
import sqlite3

nb_laureates = open('nobelLaureates.json')

data_laureates = json.load(nb_laureates)

laureates_list = [(entry['id'], entry.get('firstname', None), entry.get('gender', None), entry.get('data_de_naissance', None), entry.get('date_de_décès', None), entry.get('bornCountryCode', None), entry.get('diethCountryCode', None)) for entry in data_laureates['laureates']]
print(laureates_list)

#Ouvrez la connexion à la base de données
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

#Remplissez la table 'person' avec les valeurs de 'laureates_list'
for laureate_data in laureates_list:
    cursor.execute("INSERT INTO person (id, nom, sexe, date_de_naissance, date_de_décès, bornCountry_id, diethCountry_id) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   laureate_data)

#Enregistrez les modifications et fermez la connexion
conn.commit()
conn.close()

print("La table 'person' a été remplie avec succès.")