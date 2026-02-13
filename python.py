# ACTIVATE RUFF source .venv/bin/activate

# OR: if one of the condition is true then the entire statement is true
# temp = 25
# is_raining = True

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")

# AND: all conditions have to be true
# NOT: inverts the condition
temp = 0
is_raining = False

if temp > 10 and temp < 30 and not is_raining:
    print("The outdoor event is on going!")
else:
    print("The weather is not good enough!")
