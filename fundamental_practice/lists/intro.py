# list of names
names = ["Lavar", "John", "Dontay", "Geno"]
print(names[0])  # Lavar
print(names[1])  # John
print(names[2])  # Dontay
print(names[3])  # Geno

# simple message w/ personalized name
print(f"You're my friend {names[0]}")
print(f"You're my friend {names[1]}")
print(f"You're my friend {names[2]}")
print(f"You're my friend {names[3]}")

# car companies list
car_companies = ["toyota", "honda", "ford", "Nissan", "kia", "Lexus"]

for companies in car_companies:
    print(f"I would love to own a {companies.title()} car one day!")
