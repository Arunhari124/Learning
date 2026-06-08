import requests

base_url="https://pokeapi.co/api/v2/"

def get_pokemoninfo(name):
    url=f"{base_url}/pokemon/{name}"
    response=requests.get(url)
    if response.status_code==200:
       pokemon_data = response.json()
       return pokemon_data
    else:
        print(f"failed to retriver data {response.status_code}")



pok_mon_name="pikachu"
pokmon_info = get_pokemoninfo(pok_mon_name)

if pokmon_info:
    print(f"name= {pokmon_info["name"].capitalize()}")
    print(f"id= {pokmon_info["id"]}")
    print(f"height ={pokmon_info["height"]}")
    print(f"weight ={pokmon_info["weight"]}")