# We are going to be setting up HTTP requests using Python and the 'requests' library
# If our virtual env is running, installing packages will be \

import requests
import logging

# LOGGING
# Logging configuration:
logging.basicConfig(
    level = logging.INFO, # default level of INFO
    format = "%(asctime)s | %(levelname)s | %(message)s",
    handlers = {
        logging.FileHandler("pokemon.log"),
        logging.StreamHandler()
    }
)

logger = logging.getLogger(__name__)


# query = input(f"Enter a name or dex number to fetch it's data: ")

# # We will use the PokeAPI to fetch pokemon data
# url = f"https://pokeapi.co/api/v2/pokemon/{query.lower()}"

# response = requests.get(url)
# print(response)
# json_data = response.json()

# # Format our JSON response
# name = json_data['name']
# dex_number = json_data['id']
# height = json_data['height']
# weight = json_data['weight']

# # Pokemon types are stored in a list of dictionaries
# types = [t['type']['name'] for t in json_data['types']]

# print(f"Name: {name.capitalize()}")
# print(f"Pokedex Number: {dex_number}")
# print(f"Height: {height/10} m") # height was in decimeters
# print(f"Weight: {weight/10} kg") # weight was in hectograms
# print(f"Types: {','.join(types)}")

def get_pokemon(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    
    try:
        response = requests.get(url, timeout=5) #throws timeout error if this takes longer than 5s
        
        # Handle HTTP errors
        response.raise_for_status()
        data = response.json()

        # Drill into and format our JSON response
        pokemon_info = {
            "name": data['name'].capitalize(),
            "pokedex_number": data['id'],
            "height": data['height'],
            "weight": data['weight'],
            "types": [t['type']['name'] for t in data['types']]
        }

        logger.info(f"Pokemon {pokemon_name} exists and returns some data")
        print(pokemon_info)
    
    except requests.exceptions.HTTPError:
        print(f"Pokemon {pokemon_name} not found.")
        logger.warning(f"Pokemon not found: {pokemon_name}")
        # logger.debug(e, exec_info=True)

    except requests.exceptions.ConnectionError:
        print("Network error occurred.")
        logger.error("Network connection error")

    except requests.exceptions.Timeout:
        print("Request timed out.")
        logger.error("Connection timed out")
    
    except requests.exceptions.RequestException as e:
        print(f"Unexpected error: {e}")
        logger.error("You broke it in a way I did not expect")

pokemon_name = input("Enter a Pokemon name: ")
pokemon = get_pokemon(pokemon_name)

