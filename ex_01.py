import sqlite3

# Connexion à la base de données SQLite
conn = sqlite3.connect('database.db')

# Création de tables
cursor = conn.cursor()

# Création de la table "prize"
cursor.execute('''
    CREATE TABLE prize_new (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        laureate_id INTEGER,
        category_id INTEGER,
        année INTEGER,
        affiliation_id INTEGER,
        FOREIGN KEY (laureate_id) REFERENCES person(id),
        FOREIGN KEY (category_id) REFERENCES category(id),
        FOREIGN KEY (affiliation_id) REFERENCES country(id)
    )
''')

# Création de la table "person"
cursor.execute('''
    CREATE TABLE person (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom VARCHAR,
        sexe VARCHAR,
        date_de_naissance DATE,
        date_de_décès DATE,
        bornCountry_id INTEGER,
        deathCountry_id INTEGER,
        FOREIGN KEY (bornCountry_id) REFERENCES country(id),
        FOREIGN KEY (deathCountry_id) REFERENCES country(id)
    )
''')

# Création de la table "category"
cursor.execute('''
    CREATE TABLE category (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom VARCHAR NOT NULL UNIQUE
    )
''')

# Création de la table "country"
cursor.execute('''
    CREATE TABLE country (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom VARCHAR,
        code VARCHAR
    )
''')

# Valider la transaction et fermer la connexion
conn.commit()
conn.close()