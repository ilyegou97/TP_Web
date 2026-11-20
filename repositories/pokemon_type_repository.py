from db.database import get_connection
from schemas.pokemon_type import PokemonType


# LIRE un type dans le cache à partir de son nom anglais ("fire")
def get_type_by_name(name):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pokemon_types WHERE name = ?", (name,))
    row = cursor.fetchone()   
    connection.close()

    if row is None:
        return None

    # on recopie chaque colonne de la ligne dans un PokemonType
    pokemon_type = PokemonType(id=row["id"], name=row["name"], name_fr=row["name_fr"])
    return pokemon_type


# ÉCRIRE (ajouter) un type dans le cache
def save_type(pokemon_type):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO pokemon_types (id, name, name_fr) VALUES (?, ?, ?)",
        (pokemon_type.id, pokemon_type.name, pokemon_type.name_fr),
    )
    connection.commit()
    connection.close()
