# strings
pizzas = ["pineapple", "pepperoni", "cheese"]

for pizza in pizzas:
    print(f"I really love {pizza} pizzas")

print("Pizza is just so good!")


animals = ["elephant", "reindeer", "horse"]

for animal in animals:
    print(f"I like {animal}s and...")

print("Okay I'm done!")
# -------------------------

# ints

million = list(range(1, 1_00_001))
print(min(million))
print(max(million))
print(sum(million))

# for int in range(1,21,2):
#     print(int)

# for int in range(1, 11):
#     print(int * 3)

# for int in range(1, 11):
#     print(pow(int, 3))

first_ten = [pow(int, 3) for int in range(1, 11)]
print(first_ten)

# ----------

animals = ["elephant", "reindeer", "horse", "dog", "cat", "lion"]
print(f"First three: {animals[:3]}")
print(f"Middle: {animals[1:4]}")
print(f"Last three: {animals[-3:]}")

my_pizzas = ["pineapple", "pepperoni", "cheese"]
friend_pizzas = my_pizzas[:]

my_pizzas.append("vegetable")
friend_pizzas.append("mushrooms")
friend_pizzas.sort()
print(my_pizzas)

for pizza in my_pizzas:
    print(f"My favorite pizzas are {pizza}")

for pizza in friend_pizzas:
    print(f"My friends favorite pizzas are {pizza}")
