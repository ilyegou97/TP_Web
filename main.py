from schemas.pokemon import Pokemon
from fastapi import FastAPI
from services import pokemon_service


app = FastAPI()


# Route : vérifier que le serveur fonctionne
@app.get("/health")
def health():
    return {"status": "ok"}


# Route : lister les Pokémon enregistrés
@app.get("/pokemons", response_model=list[Pokemon])
def list_pokemons():
    return pokemon_service.list_pokemons()


# Route : consulter un Pokémon enregistré
@app.get("/pokemons/{number}", response_model=Pokemon)
def get_pokemon(number: int):
    return pokemon_service.get_pokemon(number)


# Route : scanner un Pokémon (le découvrir sur PokéAPI)
@app.get("/pokemons/{number}/scan", response_model=Pokemon)
def scan_pokemon(number: int):
    return pokemon_service.scan_pokemon(number)
