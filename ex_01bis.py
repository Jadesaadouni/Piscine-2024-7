import sqlite3
import json
import ex_00bis

# Connexion à la base de données SQLite
conn = sqlite3.connect('database.db')

# Création d'un curseur
cursor = conn.cursor()

# Insérer les données dans la table "category"
for category_name in ex_00bis.category_list:
    cursor.execute("INSERT INTO category (nom) VALUES (?)", (category_name,))


# Insérer les données dans la table "country"
for country_name,country_code in ex_00bis.country_list:
    cursor.execute("INSERT INTO country (nom, code) VALUES (?, ?)", (country_name, country_code))

# Valider la transaction et fermer la connexion
conn.commit()
conn.close()