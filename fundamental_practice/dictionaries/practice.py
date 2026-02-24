pet_one = {"name": "rex", "type": "dog", "owner": "deku"}

pet_two = {"name": "pebble", "type": "cat", "owner": "bakugo"}

pet_three = {"name": "merica", "type": "eagle", "owner": "shiro"}

pets = [pet_one, pet_two, pet_three]

for pet in pets:
    print(
        f"This pets name is {pet['name'].title()} and it is a {pet['type'].upper()} owned by {pet['owner'].title()}"
    )
# ----

favorite_places = {
    "john": ["tokyo", "paris", "rome"],
    "mickey": ["toronto", "london"],
    "tyrone": ["dubai"],
}


for name, places in favorite_places.items():
    print(f"{name.title()}(s) favorite places are:")
    for place in places:
        print(place.title())

# # -------

cities = {
    "Los Angeles": {"country": "USA", "population": 500_000, "fact": "Second to NYC"},
    "New York City": {"country": "USA", "population": 1_000_000, "fact": "The best"},
    "Chicago": {
        "country": "USA",
        "population": 100_000,
        "fact": "I dont know any facts about this place",
    },
}

for name, information in cities.items():
    print(f"Here's some information about {name}:")
    for title, details in information.items():
        print(f"The {title} is {details}")


# -----

people_numbers = {"Melissa": [11, 2, 4], "Kenny": [1], "Derek": [3, 5, 7, 9]}

for name, numbers in people_numbers.items():
    print(f"{name} favorite numbers are:")
    for number in numbers:
        print(number)


# -----
# Make an empty list to store people in.
people = []

# Define some people, and add them to the list.
person = {
    "first_name": "eric",
    "last_name": "matthes",
    "age": 46,
    "city": "sitka",
}
people.append(person)

person = {
    "first_name": "lemmy",
    "last_name": "matthes",
    "age": 2,
    "city": "sitka",
}
people.append(person)

person = {
    "first_name": "willie",
    "last_name": "matthes",
    "age": 11,
    "city": "sitka",
}
people.append(person)

for person in people:
    print(
        f"This persons name is {person['first_name'].title()} {person['last_name'].title()}, they are {person['age']} and live in {person['city'].title()}"
    )
