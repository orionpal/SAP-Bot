import json

file = open('data/api.json')
data = json.load(file)

tfile = open('data/turns.json')
turns = json.load(tfile)

# get pets data
parsepets = False
pets = {"Pets" : {}}

if parsepets:
    for pet in data['pets']:
        petsObject = data['pets'][pet]
        # only add pets that are in standard pack
        if "StandardPack" in petsObject['packs']:
            name = petsObject['name']
            tier = petsObject['tier']
            try: # some pets have no abilities
                ability = petsObject['level1Ability']
            except:
                ability = {}
            try:
                probObject = petsObject['probabilities']
            except:
                probObject = {}
            probabilities = probObject

            # make pet object with name being key
            pets["Pets"][name] = {
                'Tier' : tier,
                'Ability' : ability,
                'Prob' : probabilities
            }
    pets_object = json.dumps(pets, indent = 2)
    # write pets data
    with open('data/pets.json', "w") as outfile:
        outfile.write(pets_object)

# get foods data

parsefoods = False
foods = {"Foods" : {}}

if parsefoods:
    for food in data['foods']:
        foodsObject = data['foods'][food]
        if "StandardPack" in foodsObject['packs'] and foodsObject['tier']!='Summoned':
            name = foodsObject['name']
            tier = foodsObject['tier']
            ability = foodsObject['ability']
            
            probObject = foodsObject['probabilities']
            probabilities = probObject

            # make food object with name being key
            foods["Foods"][name] = {
                'Tier' : tier,
                'Ability' : ability
            }
    foods_object = json.dumps(foods, indent = 2)
    # write foods data
    with open('data/foods.json', "w") as outfile:
        outfile.write(foods_object)

file.close()
tfile.close()