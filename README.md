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

- [x] Route `/health` — commit `17d9d0d`
- [x] Route `/pokemons/{number}` — commit `17d9d0d`
- [x] Modèle Pydantic — commit `b933d32`
- [x] Base SQLite — commits `b933d32` (création) et `d6f9f12` (connexion)
- [x] Repository — commit `d6f9f12`
- [x] Route de scan `/pokemons/{number}/scan` — commit `d6f9f12`
- [x] Nom français — commit `832a1b9`
- [ ] Types traduits et évolution précédente
- [ ] Cache des types
- [ ] Route de liste `/pokemons`
- [ ] Sécurité par jeton Bearer
- [ ] CORS et intégration avec les pages HTML


## commande terminal pour push sur github

git status                 # voir les fichiers modifiés
git add README.md          # préparer le fichier pour le commit
git commit -m "Ajout des commits dans l'avancement du README"
git pull                   # récupérer d'abord le travail des autres membres du groupe
git push                   # envoyer ton commit
