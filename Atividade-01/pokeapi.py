# POKEAPI 

# Endpoint: http://pokeapi.co/api/v2/

# API com dados relacionados a Pokemon, cobrindo especificamente a franquia de videogames.
# Informacoes sobre Pokemons, seus movimentos, habilidades, tipos, grupos de ovos e muito mais.

# Recursos: Berries, Contests, Encounters, Evolution, Games, Items, Machines, Moves, Locations, Pokemon, Utility

# Metodos: GET


import requests

print("Lista os os 20 primeiros Pokemons")
url = 'http://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
json = response.json()
for i in json['results']:
 pokemon = i['name']
 print(pokemon)

print("")
print("Primeiro pokemon")
url = 'http://pokeapi.co/api/v2/pokemon/1'
response = requests.get(url)
json = response.json()

for i in json['forms']:
 pokemon = i['name']
 print(pokemon)