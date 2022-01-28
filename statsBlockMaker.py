import json
# from json import encode
# import jsonpickle
from os import path

print("this stat blocks name is")
name = input()

file = name + ".json"

statBlock = {}

statBlock["name"] = name


statBlock["basic stats"] = {}


print("physical stats")
statBlock["basic stats"]["Physical"] = {}

print("strength is (default 10)")
inputval = input()
if inputval == "":
    statBlock["basic stats"]["Physical"]["strength"] = 10
    statBlock["basic stats"]["Physical"]["strengthpercent"] = "100%"
else:
    statBlock["basic stats"]["Physical"]["strength"] = int(inputval)
    statBlock["basic stats"]["Physical"]["strengthpercent"] = inputval + "0%"

print("dexterity is (default 10)")
inputval = input()
if inputval == "":
    statBlock["basic stats"]["Physical"]["dexterity"] = 10
    statBlock["basic stats"]["Physical"]["dexteritypercent"] = "100%"
else:
    statBlock["basic stats"]["Physical"]["dexterity"] = int(inputval)
    statBlock["basic stats"]["Physical"]["dexteritypercent"] = inputval + "0%"

print("constitution is (default 10)")
inputval = input()
if inputval == "":
    statBlock["basic stats"]["Physical"]["constitution"] = 10
    statBlock["basic stats"]["Physical"]["constitutionpercent"] = "100%"
else:
    statBlock["basic stats"]["Physical"]["constitution"] = int(inputval)
    statBlock["basic stats"]["Physical"]["constitutionpercent"] = inputval + "0%"

print("endurance is (default 10)")
inputval = input()
if inputval == "":
    statBlock["basic stats"]["Physical"]["endurance"] = 10
    statBlock["basic stats"]["Physical"]["endurancepercent"] = "100%"
else:
    statBlock["basic stats"]["Physical"]["endurance"] = int(inputval)
    statBlock["basic stats"]["Physical"]["endurancepercent"] = inputval + "0%"

statBlock["basic stats"]["Physical"]["vigor"] = statBlock["basic stats"]["Physical"]["constitution"] * statBlock["basic stats"]["Physical"]["endurance"]
statBlock["basic stats"]["Physical"]["vigorpercent"] = str(statBlock["basic stats"]["Physical"]["constitution"] * statBlock["basic stats"]["Physical"]["endurance"]) + "%"


print("social stats")
statBlock["basic stats"]["Social"] = {}

print("charisma is (default 10)")
inputval = input()
if inputval == "":
    statBlock["basic stats"]["Social"]["charisma"] = 10
    statBlock["basic stats"]["Social"]["charismapercent"] = "100%"
else:
    statBlock["basic stats"]["Social"]["charisma"] = int(inputval)
    statBlock["basic stats"]["Social"]["charismapercent"] = inputval + "0%"

print("manipulation is (default 10)")
inputval = input()
if inputval == "":
    statBlock["basic stats"]["Social"]["manipulation"] = 10
    statBlock["basic stats"]["Social"]["manipulationpercent"] = "100%"
else:
    statBlock["basic stats"]["Social"]["manipulation"] = int(inputval)
    statBlock["basic stats"]["Social"]["manipulationpercent"] = inputval + "0%"

print("composure is (default 10)")
inputval = input()
if inputval == "":
    statBlock["basic stats"]["Social"]["composure"] = 10
    statBlock["basic stats"]["Social"]["composurepercent"] = "100%"
else:
    statBlock["basic stats"]["Social"]["composure"] = int(inputval)
    statBlock["basic stats"]["Social"]["composurepercent"] = inputval + "0%"

print("pride is (default 10)")
inputval = input()
if inputval == "":
    statBlock["basic stats"]["Social"]["pride"] = 10
    statBlock["basic stats"]["Social"]["pridepercent"] = "100%"
else:
    statBlock["basic stats"]["Social"]["pride"] = int(inputval)
    statBlock["basic stats"]["Social"]["pridepercent"] = inputval + "0%"

statBlock["basic stats"]["Social"]["courage"] = statBlock["basic stats"]["Social"]["composure"] * statBlock["basic stats"]["Social"]["pride"]
statBlock["basic stats"]["Social"]["couragepercent"] = str(statBlock["basic stats"]["Social"]["composure"] * statBlock["basic stats"]["Social"]["pride"])


print("mental stats")
statBlock["basic stats"]["Mental"] = {}

print("intellect is (default 10)")
inputval = input()
if inputval == "":
    statBlock["basic stats"]["Mental"]["intellect"] = 10
    statBlock["basic stats"]["Mental"]["intellect"] = "100%"
else:
    statBlock["basic stats"]["Mental"]["intellect"] = int(inputval)
    statBlock["basic stats"]["Mental"]["intellect"] = inputval + "0%"

print("wits is (default 10)")
inputval = input()
if inputval == "":
    statBlock["basic stats"]["Mental"]["wits"] = 10
    statBlock["basic stats"]["Mental"]["witspercent"] = "100%"
else:
    statBlock["basic stats"]["Mental"]["wits"] = int(inputval)
    statBlock["basic stats"]["Mental"]["witspercent"] = inputval + "0%"

print("resolve is (default 10)")
inputval = input()
if inputval == "":
    statBlock["basic stats"]["Mental"]["resolve"] = 10
    statBlock["basic stats"]["Mental"]["resolvepercent"] = "100%"
else:
    statBlock["basic stats"]["Mental"]["resolve"] = int(inputval)
    statBlock["basic stats"]["Mental"]["resolvepercent"] = inputval + "0%"

print("magic is (default 10)")
inputval = input()
if inputval == "":
    statBlock["basic stats"]["Mental"]["magic"] = 10
    statBlock["basic stats"]["Mental"]["magicpercent"] = "100%"
else:
    statBlock["basic stats"]["Mental"]["magic"] = int(inputval)
    statBlock["basic stats"]["Mental"]["magicpercent"] = inputval + "0%"

statBlock["basic stats"]["Mental"]["mana"] = statBlock["basic stats"]["Mental"]["resolve"] * statBlock["basic stats"]["Mental"]["magic"]
statBlock["basic stats"]["Mental"]["manapercent"] = str(statBlock["basic stats"]["Mental"]["resolve"] * statBlock["basic stats"]["Mental"]["magic"])


print("health stats")
statBlock["basic stats"]["HealthCat"] = {}

print("vitality is (default 10)")
inputval = input()
if inputval == "":
    statBlock["basic stats"]["HealthCat"]["vitality"] = 10
    statBlock["basic stats"]["HealthCat"]["vitalitypercent"] = "100%"
else:
    statBlock["basic stats"]["HealthCat"]["vitality"] = int(inputval)
    statBlock["basic stats"]["HealthCat"]["vitalitypercent"] = inputval + "0%"

print("resistance is (default 10)")
inputval = input()
if inputval == "":
    statBlock["basic stats"]["HealthCat"]["resistance"] = 10
    statBlock["basic stats"]["HealthCat"]["resistancepercent"] = "100%"
else:
    statBlock["basic stats"]["HealthCat"]["resistance"] = int(inputval)
    statBlock["basic stats"]["HealthCat"]["resistancepercent"] = inputval + "0%"

statBlock["basic stats"]["HealthCat"]["health"] = statBlock["basic stats"]["HealthCat"]["vitality"] * statBlock["basic stats"]["HealthCat"]["resistance"]
statBlock["basic stats"]["HealthCat"]["healthpercent"] = str(statBlock["basic stats"]["HealthCat"]["vitality"] * statBlock["basic stats"]["HealthCat"]["resistance"]) + "%"


with open(file, 'w') as f:
    json.dump(statBlock , f)
