from pydantic import BaseModel


class PokemonType(BaseModel):
    id: int         # identifiant du type dans PokéAPI
    name: str       # nom anglais utilisé par PokéAPI ("fire")
    name_fr: str    # nom français ("Feu")
