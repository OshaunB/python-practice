dinner_guests = ["Jesus", "Socrates", "Nero", "Jace"]

for guest in dinner_guests:
    print(f"Welcome to my dinner {guest}.")

print(f"Uh Oh! {dinner_guests[-1]} can't make it!")

dinner_guests[-1] = "Jermaine Cole"

print(f"{dinner_guests[3]} will replace him.")

for guest in dinner_guests:
    print(f"Second wave of invites: {guest}.")

# Gordon Ramsey, James Allen, Plato
print("I have found a bigger table")

dinner_guests.insert(0, "Gordon Ramsey")
dinner_guests.insert(int(len(dinner_guests) / 2), "James Allen")
dinner_guests.append("Plato")

for guest in dinner_guests:
    print(f"{guest.title()} please find a seat at this table.")

print(dinner_guests, len(dinner_guests))


print("Apologies every one, it seems only 2 people can go to dinner!")

while len(dinner_guests) > 2:
    uninvited_guest = dinner_guests.pop()
    print(f"Apologies {uninvited_guest}, maybe another time")

print(f"Dear {dinner_guests[0]} and {dinner_guests[1]}, I look forward to seeing you")

del dinner_guests[0]
del dinner_guests[0]

print(dinner_guests)
