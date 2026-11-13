from schemas.pokemon import Pokemon
from db.database import get_connection
from fastapi import FastAPI, HTTPException
from repositories.pokemon_repository import get_pokemon_by_number, save_pokemon
from clients.pokeapi import get_pokemon_from_api, get_species_from_api
import json


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
    pokemon_base=None
    pokemon_base = get_pokemon_by_number(number)
    

    if pokemon_base:
        pokemon = dict(pokemon_base)
        pokemon["types"] = json.loads(pokemon["types"])
        return pokemon


       

    # 2. On demande ce Pokémon (et seulement lui) à PokéAPI
    data = get_pokemon_from_api(number)
    if data is None:
        raise HTTPException(status_code=404, detail="Pokémon introuvable")

    # Nom français
    species = get_species_from_api(number)

    name_fr = data["name"]
    if species is not None:
        for n in species["names"]:
            if n["language"]["name"] == "fr":
                name_fr = n["name"]          

    # 3. On garde uniquement les infos utiles
    types = []
    for t in data["types"]:
        types.append(t["type"]["name"])

    pokemon = {
        "number": data["id"],
        "name": data["name"],
        "name_fr": name_fr,
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


# raise HTTPException(
#            status_code=404,
#           detail={"message": "Pokémon déjà enregistré", "pokemon": dict(pokemon_base)},
#        )