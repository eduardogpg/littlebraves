import requests
from GiagantBrave import LittleBrave
from GiagantBrave import catch_result

@catch_result
def show_pokemon_name(name):
    print('El nombre del pokemon es:', name)

def get_pokemon_name(url):
    response = requests.get(url)

    if response.status_code == 200:
        response_json = response.json()
        name = response_json.get('forms')[0].get('name')

        return name

brave1 = LittleBrave(
    get_pokemon_name,
    args=('https://pokeapi.co/api/v2/pokemon/1/',)
)
brave1.set_callback(show_pokemon_name)
brave1.start()