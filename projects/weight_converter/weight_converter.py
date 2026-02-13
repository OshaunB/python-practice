# python weight converter
# convert pounds to kilograms or kilo to lbs, user will decide
# weight, in kilos or pounds, do some type of conversion operation depending on ans, give converted weight

weight = int(input("What is you weight?"))
unit = input("Kilograms or Pounds? (kg or lbs)")

if unit == "kg":
    converted_weight = weight * 2.2
    print(f"Weight in pounds: {round(converted_weight, 2)}lbs")
elif unit == "lbs":
    converted_weight = weight / 2.2
    print(f"Weight in kilograms {round(converted_weight, 2)}kg")
else:
    print(f"Please input a valid weight and unit. Input: {weight} {unit}")
