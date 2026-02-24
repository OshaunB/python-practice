# person = {"first_name": "Lavar", "last_name": "Miles", "age": 23, "city": "NYC"}

# for info in person:
#     print(person[info])

# Maya, Jordan, Elias, Serena, Kai | 17, 42, 86, 113, 290

# favorite_numbers = {"Maya": 17, "Jordan": 42, "Elias": 86, "Serena": 113, "Kai": 290}

# for person in favorite_numbers:
#     print(person, favorite_numbers[person])

# 5 programming words
# Integer (int): whole number

# Float: number with decimals

# String (str): text

# Boolean (bool): true/false

# List: ordered collection of items
# code_terminology = {
#     "variable": "stores a value",
#     "function": "reusable block of code",
#     "loop": "repeats code",
#     "array": "ordered list of items",
#     "API": "way for programs to communicate",
#     "Integer": "whole number",
#     "Float": "number with decimals",
#     "String": "text",
#     "boolean": "true/false",
#     "List": "ordered collection of items",
# }

# for word, definition in code_terminology.items():
#     print(f"{word.upper()}: {definition}!")

# another way
# for key, value in dictionary.items()

# major_rivers = {"Amazon": "Peru", "Nile": "Egypt", "Yangtze": "China"}

# for name, origin in major_rivers.items():
#     if name.title() == "Amazon":
#         print(f"The {name} river is the biggest by volume")
#     elif name.title() == "Nile":
#         print(f"The {name} river is one of the longest")
#     else:
#         print(f"The {name} river is longest in asia")

# for name in major_rivers.keys():
#     print(name)

# for origin in major_rivers.values():
#     print(origin)

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "tre": "c++",
    "jason": "javascript",
}

list_of_people = ["jen", "sarah", "edward", "tre", "jason", "phil"]

for person in list_of_people:
    if person in favorite_languages:
        print("Thank you for  taking the time out to take the survey")
    else:
        print("Please take a moment out to take the survey")
