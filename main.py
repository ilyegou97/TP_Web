from schemas.pokemon import Pokemon
from db.database import get_connection
from fastapi import FastAPI, HTTPException
from repositories.pokemon_repository import get_pokemon_by_number, save_pokemon
from clients.pokeapi import get_pokemon_from_api


app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/pokemons/{number}", response_model=Pokemon)
def get_pokemon(number: int):
    data = get_pokemon_from_api(number)

    if data is None:
        raise HTTPException(status_code=404, detail="Pokémon introuvable")

    types = []
    for t in data["types"]:
        types.append(t["type"]["name"])

    return {
        "number": data["id"],
        "name": data["name"],
        "name_fr": data["name"],
        "types": types,
        "image_url": data["sprites"]["front_default"],
        "height": data["height"],
        "weight": data["weight"],
    }


@app.get("/pokemons/{number}/scan", response_model=Pokemon)
def scan_pokemon(number: int):
    pokemon_trouve=None
    pokemon_base=None
    pokemon_base = get_pokemon_by_number(number)
    
    # 1. Déjà dans la base ? On ne l'ajoute pas une deuxième fois
    if pokemon_base:
        print("pokemon trouve en base", dict(pokemon_base))
        raise HTTPException(
            status_code=404,
            detail={"message": "Pokémon déjà enregistré", "pokemon": dict(pokemon_base)},
        )

    # 2. On demande ce Pokémon (et seulement lui) à PokéAPI
    data = get_pokemon_from_api(number)
    if data is None:
        raise HTTPException(status_code=404, detail="Pokémon introuvable")

    # 3. On garde uniquement les infos utiles
    types = []
    for t in data["types"]:
        types.append(t["type"]["name"])

    pokemon = {
        "number": data["id"],
        "name": data["name"],
        "name_fr": data["name"],   # le vrai nom français viendra à la question 11
        "types": types,
        "image_url": data["sprites"]["front_default"],
        "height": data["height"],
        "weight": data["weight"],
        "evolves_from_number": None,   # question 11 aussi
    }

    # 4. On l'enregistre dans SQLite
    save_pokemon(pokemon)

    # 5. On renvoie la fiche enregistrée
    return pokemon
