# 1 False
room_light = "blue"
print("Is my room light red? no its not")
print(room_light == "red")

# 2 True
print("What about blue?")
print(room_light == "blue")

# 3 False
weight_lbs = 300
print("This roller coaster has a weight limit of 260, can I go on it?")
print(weight_lbs < 260)
print("that sucks")

# 4 True
print("The limit is 500 for this other one, lets do it!")
print(weight_lbs < 500)
print("Lets go!")

# 5
fav_music_genre = "pop"
friend_name = "Chris"
friend_fav_music_genre = input(f"Hey {friend_name}, what is your favorite music genre?")
if friend_fav_music_genre == fav_music_genre:
    print(f"Wow, I love {fav_music_genre} as well!")
else:
    print("Interesting, maybe I should try that one out")

# 6
my_major = "CS"
friend_major = input(f"What is your college major {friend_name}?")

if my_major == friend_major:
    print("See you in class!")
else:
    print("Good luck!")

# 7
my_hobbies = ["reading", "knitting", "sleeping", "gaming"]
friend_hobbies = ["snowboarding", "producing", "coding"]

print(f"Hey {friend_name}, I need some new hobbies tell me about yours!")
print("yea sure, I like:")
for hobbies in friend_hobbies:
    print(hobbies)

print(f"Wow I think I like {friend_hobbies[-1]}")
my_hobbies.append(friend_hobbies[-1])

print("coding" in my_hobbies)
print(my_hobbies)

print("I can only know 3 though")
while len(my_hobbies) > 3:
    my_hobbies.pop(0)

print(my_hobbies)

# 8
girlfriend = "Lucy"
print(type(girlfriend) is str)

# 9
my_hunger_status = False
girlfriend_hunger_status = input(f"Hey {girlfriend}, are you hungry? (yes/no)")

if my_hunger_status or girlfriend_hunger_status == "yes":
    print("Lets get some food!")
else:
    print("Alrighty, then lets watch a movie")

# 10
active_light = False
if active_light:
    print("The lights are bright...")
else:
    print("Turn on the lights!")
