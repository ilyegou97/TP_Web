import json

from db.database import get_connection


# LIRE un Pokémon à partir de son numéro
def get_pokemon_by_number(number):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pokemon WHERE number = ?", (number,))
    pokemon = cursor.fetchone()  
    connection.close()
    return pokemon


# LIRE tous les Pokémon enregistrés, triés par numéro
def get_all_pokemons():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pokemon ORDER BY number")
    pokemons = cursor.fetchall()  
    return pokemons


# ÉCRIRE (ajouter) un nouveau Pokémon dans la base
def save_pokemon(pokemon):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO pokemon (number, name, name_fr, types, image_url, height, weight, evolves_from_number, evolves_from_name)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            pokemon["number"],
            pokemon["name"],
            pokemon["name_fr"],
            json.dumps(pokemon["types"], ensure_ascii=False),  
            pokemon["image_url"],
            pokemon["height"],
            pokemon["weight"],
            pokemon["evolves_from_number"],
            pokemon["evolves_from_name"],
        ),
    )
    connection.commit()
    connection.close()
