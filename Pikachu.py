from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

print("\n\nRunning query 1 (pikachu query)\n")

queryPikachu = {"name": "Pikachu"}
allPikachu = pokemonColl.find(queryPikachu)
for pokemons in allPikachu:
    print(pokemons)

print("\nFinished running query 1 (pikachu query)\n\n")