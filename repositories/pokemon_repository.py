import json

from db.database import get_connection


def get_pokemon_by_number(number):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pokemon WHERE number = ?", (number,))
    pokemon = cursor.fetchone()   # le Pokémon, ou None s'il n'existe pas
    connection.close()
    return pokemon


def save_pokemon(pokemon):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO pokemon (number, name, name_fr, types, image_url, height, weight, evolves_from_number)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            pokemon["number"],
            pokemon["name"],
            pokemon["name_fr"],
            json.dumps(pokemon["types"], ensure_ascii=False),   # la liste devient du texte
            pokemon["image_url"],
            pokemon["height"],
            pokemon["weight"],
            pokemon["evolves_from_number"],
        ),
    )
    connection.commit()
    connection.close()
