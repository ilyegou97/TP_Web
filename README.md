# Pokédex - API REST

TP Développement Web - GOUGIS, DURU, BOUBEKEUR

API REST d'un Pokédex de la première génération (151 Pokémon), réalisée dans le cadre d'un TP.

Les Pokémon ne sont pas tous téléchargés au départ : un Pokémon est récupéré depuis [PokéAPI](https://pokeapi.co/) uniquement quand un utilisateur demande son scan, puis il est enregistré dans une base SQLite.

## Technologies

- Python
- FastAPI
- Pydantic
- SQLite
- requests
- PokéAPI

## Installation

1. Cloner le projet puis se placer dans le dossier :

```bash
git clone https://github.com/ilyegou97/TP_Web.git
cd TP_Web
```

2. Créer et activer un environnement virtuel :

```bash
python -m venv .venv
```

Sous Windows :

```bash
.venv\Scripts\activate
```

Sous macOS ou Linux :

```bash
source .venv/bin/activate
```

3. Installer les dépendances :

```bash
pip install -r requirements.txt
```

4. Créer la base de données (une seule fois) :

```bash
python create_database.py
```

## Lancer le serveur

```bash
fastapi dev main.py
```

L'API est disponible sur http://127.0.0.1:8000 et la documentation interactive sur http://127.0.0.1:8000/docs.

## Routes

| Méthode | Route | Description |
|---|---|---|
| GET | `/health` | Vérifie que le serveur fonctionne |
| GET | `/pokemons/{number}` | Renvoie la fiche d'un Pokémon |

## Structure du projet

```
POKEDEX/
├── main.py               # application FastAPI et routes
├── create_database.py    # création de la base SQLite
├── schemas/
│   └── pokemon.py        # modèle Pydantic Pokemon
└── requirements.txt      # dépendances
```

## Avancement

- [x] Route `/health`
- [x] Route `/pokemons/{number}`
- [x] Modèle Pydantic
- [x] Base SQLite
- [ ] Repository
- [ ] Route de scan `/pokemons/{number}/scan`
- [ ] Nom français, types traduits et évolution précédente
- [ ] Cache des types
- [ ] Route de liste `/pokemons`
- [ ] Sécurité par jeton Bearer
- [ ] CORS et intégration avec les pages HTML
