from schemas.pokemon import Pokemon
import requests
from fastapi import FastAPI, HTTPException

app = FastAPI()





@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/pokemons/{number}", response_model=Pokemon)
def get_pokemon(number: int):
    url = f"https://pokeapi.co/api/v2/pokemon/{number}"
    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Pokémon introuvable")

    data = response.json()

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



