# operator, the 2 numbers and the result
# round function goes to closest whole number
# operator = input("Enter an arithmetic operator: (+,-,*,/) ")
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# if operator == "+":
#     sum = num1 + num2
#     print(f"Sum: {round(sum,2)}")
# elif operator == "-":
#     difference = num1 - num2
#     print(f"Difference: {round(difference,2)}")
# elif operator == "*":
#     product = num1 * num2
#     print(f"Product: {round(product,2)}")
# elif operator == "/":
#     quotient = num1/num2
#     print(f"Quotient{round(quotient,2)}")
# else:
#     print(f"Please select an arithmetic operator from the four given choices. {operator} is an invalid operator")


# python weight converter
# convert pounds to kilograms or kilo to lbs, user will decide
# weight, in kilos or pounds, do some type of conversion operation depending on ans, give converted weight

# weight = int(input("What is you weight?"))
# unit = input("Kilograms or Pounds? (kg or lbs)")

# if unit == "kg":
#     converted_weight = weight*2.2
#     print(f"Weight in pounds: {round(converted_weight,2)}lbs")
# elif unit == "lbs":
#     converted_weight = weight / 2.2
#     print(f"Weight in kilograms {round(converted_weight,2)}kg")
# else:
#     print(f"Please input a valid weight and unit. Input: {weight} {unit}")


# temp converter

# unit = input("Is this temperature in Celsius or Fahrenheit? (C or F) ")
# temperature = float(input("Please input temperature: "))

# if unit == "F":
#     new_temperature = (temperature - 32) * 5/9
#     print(f"Temperature in Celsius: {round(new_temperature,3)}")
# elif unit == "C":
#     new_temperature = (temperature * 9/5) + 32
#     print(f"Temperature in Fahrenheit: {round(new_temperature,3)}")
# else:
#     print("Please input a valid unit & temperature")
def greet(name: str, times=3):
    msg = f"hello, {name}!"
    for i in range(times):
        print(msg)


def add(a, b):
    return a + b


def main():
    nums = [1, 2, 3, 4, 5]
    total = 0
    for n in nums:
        total = add(total, n)
    greet("oshaun", 2)
    if total > 10:
        print("big total:", total)
    else:
        print("small total:", total)


if __name__ == "__main__":
    main()
