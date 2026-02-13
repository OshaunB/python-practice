# temp converter

unit = input("Is this temperature in Celsius or Fahrenheit? (C or F) ")
temperature = float(input("Please input temperature: "))

if unit == "F":
    new_temperature = (temperature - 32) * 5 / 9
    print(f"Temperature in Celsius: {round(new_temperature, 3)}")
elif unit == "C":
    new_temperature = (temperature * 9 / 5) + 32
    print(f"Temperature in Fahrenheit: {round(new_temperature, 3)}")
else:
    print("Please input a valid unit & temperature")
