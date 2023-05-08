# Extra Credit #2: Improve the Battle.py script. The algorithm in the Battle.py
# script is pretty lame. (Team Rocket is NOT known for its skills in
# evaluating Pokemon.) Improve it and commit the changes to this repository.
# Make sure to point out to your TA that you have improved it, so they can
# verify it and give you the extra point.

# Improvements for extra credit:
# Improvement 1: I changed the script a little to make it "better/more fun" and
#                 added spacing to make the text easier to read.
# Improvement 2: I added an else statement to check if the there is a tie in a stat.
# Improvement 3: I added a stat counter to count how many stats each pokemon has advantage in.
# Improvement 4: Based on the stat counter, whichever pokemon "won" in more stats won the battle;
#                if both pokemon "won" an equal number of stats, the battle would result in a tie.

import random
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

def fetch(pokemonid):
    return pokemonColl.find_one({"pokedex_number":pokemonid})

def battle(pokemon1, pokemon2):
    print("\nLet the Pokemon battle begin! ================")
    print("\nWe have a great match between " + pokemon1['name'] + " and " + pokemon2['name'] + "!!!\n")

    p1StatCount = 0
    p2StatCount = 0
    for stat in ['hp', 'attack', 'defense', 'speed', 'sp_attack', 'sp_defense']:
        if pokemon1[stat] > pokemon2[stat]:
            print(pokemon1['name'] + " has the advantage in " + stat)
            p1StatCount += 1
        elif pokemon2[stat] > pokemon1[stat]:
            print(pokemon2['name'] + "'s " + stat + " is superior")
            p2StatCount += 1
        else:
            print(pokemon1['name'] + " and " + pokemon2['name'] + " are equal for " + stat)

    if p1StatCount > p2StatCount:
        print("\n" + pokemon1['name'] + " had " + str(p1StatCount) + " point(s), while " +
              pokemon2['name'] + " only had " + str(p2StatCount) + " point(s).")
        print("Battle results: " + pokemon1['name'] + " wins!\n\n")
    elif p1StatCount < p2StatCount:
        print("\n" + pokemon2['name'] + " had " + str(p2StatCount) + " point(s), while " +
              pokemon1['name'] + " only had " + str(p1StatCount) + " point(s).")
        print("Battle results: " + pokemon2['name'] + " wins!\n\n")
    else:
        print("\n" + "Both " + pokemon1['name'] + " and " + pokemon2['name'] + " had " + str(p1StatCount) + " points.")
        print("Battle results: " + pokemon1['name'] + " and " + pokemon2['name'] + " are equal!\n\n")

def main():
    # Fetch two pokemon from the MongoDB database
    pokemon1 = fetch(random.randrange(801))
    pokemon2 = fetch(random.randrange(801))

    # Pit them against one another
    battle(pokemon1, pokemon2)

main()