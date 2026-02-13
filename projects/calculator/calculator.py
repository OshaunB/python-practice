# operator, the 2 numbers and the result
# round function goes to closest whole number
operator = input("Enter an arithmetic operator: (+,-,*,/) ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    sum = num1 + num2
    print(f"Sum: {round(sum, 2)}")
elif operator == "-":
    difference = num1 - num2
    print(f"Difference: {round(difference, 2)}")
elif operator == "*":
    product = num1 * num2
    print(f"Product: {round(product, 2)}")
elif operator == "/":
    quotient = num1 / num2
    print(f"Quotient{round(quotient, 2)}")
else:
    print(
        f"Please select an arithmetic operator from the four given choices. {operator} is an invalid operator"
    )
