import sqlite3


# Ouvrir la connexion à la base pokedex.db
def get_connection():
    connection = sqlite3.connect("pokedex.db")
    connection.row_factory = sqlite3.Row
    return connection
