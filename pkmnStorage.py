# id, Name, Type, ability, moveset(4), location(Party or storage)
party = {
    1:("","","",("","","",""),"Party"),
    1:("","","",("","","",""),"Party"),
    1:("","","",("","","",""),"Party"),
    1:("","","",("","","",""),"Party"),
}

storage = {
    3:("","","",("","","",""),"Storage"),
    3:("","","",("","","",""),"Storage"),
    3:("","","",("","","",""),"Storage"),
    3:("","","",("","","",""),"Storage"),
    3:("","","",("","","",""),"Storage"),
    3:("","","",("","","",""),"Storage"),
}

# user can move pkmn between storage and party, party has a stict length of 6, moveset is a tuple inside value tuple

def move_to_party(pkmn):
    """
    """
    return 

def move_to_storage(pkmn):
    """
    """
    return

def menu():
    """
    """
    return


# Dictionary methods
# (1) print brand value of dictionary
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])

# (2) Adding items to a dictionary
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)

# (3) Update Dictionary 
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"color": "red"})

# (4) Removing items
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)

# Loop through both keys and values in Dictionary <-------------!!!!
# for x, y in thisdict.items():
#   print(x, y)

# (5) Copying a dictionary
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)

# (6) Creating a nested dictionary, 3 dictionaries into one dictionary 
# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

# print(myfamily)

# (7) Access items in Nested Dictionaries 
# print(myfamily["child2"]["name"])

# (8) Unpacking a tuple
# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

# (9) add items to a tuple by converting it to a list and back to a tuple
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)

# another way
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)

# (10) functions with unknown amount of parameters
# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")