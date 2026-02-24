sandwich_order = [
    "Bacon Egg Cheese",
    "Chopped Cheese",
    "Ham and Cheese Sandwich",
    "Tuna Sandwich",
    "Pastrami Sandwich",
    "Pastrami Sandwich",
    "Pastrami Sandwich",
]
finished_sandwiches = []

print("The deli has run out of pastrami")

while "Pastrami Sandwich" in sandwich_order:
    sandwich_order.remove("Pastrami Sandwich")
    print("Removed Pastrami Sandwich")

while sandwich_order:
    current_sandwich = sandwich_order.pop()
    print(f"I made your {current_sandwich}")
    finished_sandwiches.append(current_sandwich)

print("Here's a list of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
