import requests


# Récupérer la fiche d'un Pokémon sur PokéAPI
def get_pokemon_from_api(number):                           #construit l'URL correspondant au numéro demandé
    url = f"https://pokeapi.co/api/v2/pokemon/{number}"   
    response = requests.get(url)                            #effectue la requête HTTP avec requests

    if response.status_code != 200:                         #détecte les erreurs HTTP ;
        return None
    return response.json()

# Récupérer un type sur PokéAPI
def get_type_from_api(name):
    url = f"https://pokeapi.co/api/v2/type/{name}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    return response.json()

# Récupérer l'espèce d'un Pokémon (nom FR, évolution) sur PokéAPI
def get_species_from_api(number):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{number}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    return response.json()