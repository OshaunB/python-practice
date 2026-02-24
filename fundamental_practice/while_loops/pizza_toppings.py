pizza_toppings = []

requested_topping = ""

while requested_topping != "None":
    requested_topping = input(
        "What topping would you like on your pizza? (Enter 'None' to stop adding)"
    )
    if requested_topping == "None":
        break

    pizza_toppings.append(requested_topping)


print("The toppings on your pizza are:")
for topping in pizza_toppings:
    print(f"{topping}")
