# Camden, 2024
import pprint
from typing import Any
from random import randint
#Location

toon: dict[str, Any] = {
    "name":"",
    "level":0,
    "toontype":"",
    "hp":0,
    "mp":0,
    "location":[0,0,0],
    "skills":[],
    "inventory":[],
    "attributes": {
        "strength":0,
        "agility":0,
        "intelect":0,
        "charisma":0,
        "luck":0
    } 
}

"""toon['name'] = "Camden"
toon['hp'] = 20
toon['location'][0] = 1
toon['skills'].append(1)
toon['attributes']['strength'] = 99

print(toon)"""

orc: dict[str, Any] = {
            
    "name":"Orc",
    "level":10,
    "class type":"orc",
    "hp":10,
    "mp":0,
    "location":[0,0,0],
    "skills":[],
    "inventory":[],
    "attributes": {
        "strength":10,
        "agility":1,
        "intelect":1,
        "charisma":1,
        "luck":1
    }
}

troll: dict[str, Any] = {
    "name":"Troll",
    "level":10,
    "class type":"troll",
    "hp":10,
    "mp":0,
    "location":[0,0,0],
    "skills":[],
    "inventory":[],
    "attributes": {
        "strength":10,
        "agility":1,
        "intelect":1,
        "charisma":1,
        "luck":1
    }
}

goblin: dict[str, Any] = {
    "name":"Goblin",
    "level":10,
    "class type":"goblin",
    "hp":10,
    "mp":0,
    "location":[0,0,0],
    "skills":[],
    "inventory":[],
    "attributes": {
        "strength":10,
        "agility":1,
        "intelect":1,
        "charisma":1,
        "luck":1
    }
}

shrek: dict[str, Any] = {
    "name":"Wreck and Shreck",
    "level":"",
    "class type":"ogre",
    "hp":100,
    "mp":0,
    "location":[0,0,0],
    "skills":[],
    "inventory":[],
    "attributes": {
        "strength":10,
        "agility":10,
        "intelect":10,
        "charisma":10,
        "luck":10
    }
}

mage: dict[str, Any] = {
    "name":"Mage",
    "level":10,
    "class type":"squishable",
    "hp":20,
    "mp":100,
    "location":[0,0,0],
    "skills":[],
    "inventory":[],
    "attributes": {
        "strength":10,
        "agility":10,
        "intelect":10,
        "charisma":10,
        "luck":10
    }
}

he_man: dict[str, Any] = {
    "name":"He Man",
    "level":100,
    "class type":"squishable",
    "hp":100,
    "mp":20,
    "location":[0,0,0],
    "skills":[],
    "inventory":[],
    "attributes": {
        "strength":10,
        "agility":10,
        "intelect":10,
        "charisma":10,
        "luck":10
    }
}

archer: dict[str, Any] = {
    "name":"Archer",
    "level":10,
    "class type":"squishable",
    "hp":20,
    "mp":20,
    "location":[0,0,0],
    "skills":[],
    "inventory":[],
    "attributes": {
        "strength":10,
        "agility":10,
        "intelect":10,
        "charisma":10,
        "luck":10
    }
}

medic_tf2: dict[str, Any] = {
    "name":"Medic TF2",
    "level":69,
    "toontype":"battle medic",
    "hp":150,
    "mp":10,
    "location":[0,0,0],
    "skills":[],
    "inventory":[],
    "attributes": {
        "strength":10,
        "agility":10,
        "intelect":50,
        "charisma":10,
        "luck":10
    }
}

player: dict[str, Any] = {
    "name":"Camden",
    "level":0,
    "toontype":"",
    "hp":0,
    "mp":0,
    "location":[0,0,0],
    "skills":[],
    "inventory":[],
    "attributes": {
        "strength":0,
        "agility":0,
        "intelect":0,
        "charisma":0,
        "luck":0
    } 
}

printer = pprint.PrettyPrinter

def Move(toon):
    toon["location"][0] += randint(-2,2)
    toon["location"][1] += randint(-2,2)
    #toon["location"][2] += 5

    if toon["location"][0] < 0 :
        toon["location"][0] = 0

    if toon["location"][1] < 0 :
        toon["location"][1] = 0

    if toon["location"][0] > 99 :
        toon["location"][0] = 0

    if toon["location"][1] > 0 :
        toon["location"][1] = 0

    print(toon["name"],toon["location"])
    return toon

enemies: list[dict] = [orc, troll, goblin, shrek]
heros: list[dict] = [mage, he_man, archer, medic_tf2, player]

Move(player)
print(player['location'])

print(f"{enemies = }")
print(f"{heros = }")

print(f"{enemies[0]}")
print(f"{heros[0]}")

for enemy in enemies:
    enemy['attributes']['strength'] = randint(1,100)
    print(f"{enemy['name']}\n {enemy['attributes'] = }\n")

for hero in heros:
    hero['attributes']['strength'] = randint(1,100)
    print(f"{hero['name']}\n {hero['attributes'] = }\n")




