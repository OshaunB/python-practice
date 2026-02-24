active = True

while active:
    age = int(input("What is your age?"))
    if age < 4:
        ticket_price = 0
    elif age < 13:
        ticket_price = 10
    elif age >= 13:
        ticket_price = 15
    active = False
    print(f"The price of your ticket is {ticket_price}")
