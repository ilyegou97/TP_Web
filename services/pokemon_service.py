import json

from fastapi import HTTPException

from clients.pokeapi import get_pokemon_from_api, get_species_from_api, get_type_from_api
from repositories.pokemon_repository import get_pokemon_by_number, save_pokemon, get_all_pokemons
from repositories.pokemon_type_repository import get_type_by_name, save_type
from schemas.pokemon_type import PokemonType


# Traduire un type en français (cache SQLite, sinon PokéAPI)
def get_type(name):
    # 1. Le type est déjà dans le cache SQLite : on l'utilise directement
    pokemon_type = get_type_by_name(name)
    if pokemon_type is not None:
        return pokemon_type

    # 2. Sinon, on le demande à PokéAPI
    data = get_type_from_api(name)

    name_fr = name   # nom anglais en secours
    for n in data["names"]:
        if n["language"]["name"] == "fr":
            name_fr = n["name"]

    # 3. On l'enregistre dans le cache pour les prochains scans
    pokemon_type = PokemonType(id=data["id"], name=name, name_fr=name_fr)
    save_type(pokemon_type)
    return pokemon_type


# Lister les Pokémon présents dans SQLite
def list_pokemons():
    pokemons = []
    for pokemon_base in get_all_pokemons():
        pokemon = dict(pokemon_base)
        pokemon["types"] = json.loads(pokemon["types"])   # le texte redevient une liste
        pokemons.append(pokemon)
    return pokemons


# Consulter un Pokémon dans SQLite (404 s'il n'est pas enregistré)
def get_pokemon(number):
   
    pokemon_base = get_pokemon_by_number(number)
    if pokemon_base is None:
        raise HTTPException(status_code=404, detail="Pokémon non enregistré")

    pokemon = dict(pokemon_base)
    pokemon["types"] = json.loads(pokemon["types"])   # le texte redevient une liste
    return pokemon


# Scanner : récupérer sur PokéAPI, convertir, enregistrer
def scan_pokemon(number):
 
    pokemon_base = get_pokemon_by_number(number)
    if pokemon_base is not None:
        pokemon = dict(pokemon_base)
        pokemon["types"] = json.loads(pokemon["types"])   # le texte redevient une liste
        raise HTTPException(
            status_code=404,
            detail={"message": "Pokémon déjà enregistré", "pokemon": pokemon},
        )

    
    data = get_pokemon_from_api(number)
    if data is None:
        raise HTTPException(status_code=404, detail="Pokémon introuvable")

    species = get_species_from_api(number)

   

  
    name_fr = data["name"]

    if species is not None:
        names_fr = [n["name"] for n in species["names"] if n["language"]["name"] == "fr"]
                    # valeur gardée   | collection          | condition
       
        if names_fr:                 
            name_fr = names_fr[0]    

    #if species is not None:
     #   for n in species["names"]:
      #      if n["language"]["name"] == "fr":
       #         name_fr = n["name"]

    # Évolution précédente
    evolves_from_number = None
    evolves_from_name = None
    
    if species is not None and species["evolves_from_species"] is not None:
        mothers_species = species["evolves_from_species"]
        evolves_from_name = mothers_species["name"]   # "pikachu"
        url = mothers_species["url"]   # ".../pokemon-species/25/"
        morceaux = url.split("/")                      # [..., "pokemon-species", "25", ""]
        evolves_from_number = int(morceaux[-2])        # avant-dernier morceau : "25" -> 25

        if evolves_from_number > 151:
            evolves_from_number = None
            evolves_from_name = None

    # Types (traduits en français grâce au cache)
    types = []
    for t in data["types"]:
        pokemon_type = get_type(t["type"]["name"])
        types.append(pokemon_type.name_fr)

    pokemon = {
        "number": data["id"],
        "name": data["name"],
        "name_fr": name_fr,
        "types": types,
        "image_url": data["sprites"]["front_default"],
        "height": data["height"],
        "weight": data["weight"],
        "evolves_from_number": evolves_from_number,
        "evolves_from_name": evolves_from_name,
    }


    save_pokemon(pokemon)


    return pokemon
