usernames = ["Escendency", "vestra5", "InfamousZato", "Yo Vot", "admin"]

for username in usernames:
    if username == "admin":
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again")

del usernames[:]

if len(usernames) == 0:
    print("We need to find some users!")

# checking usernames

current_users = ["John", "Aoife", "Alex", "Brian", "Rob"]
new_users = ["Brian", "Kevin", "JOHN", "Tyler", "Chris"]

# Create a lowercase version of current_users for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

for username in new_users:
    if username.lower() in current_users_lower:
        print(
            f"Sorry, the username '{username}' is already taken. Please enter a new one."
        )
    else:
        print(f"The username '{username}' is available!")

# ordinal numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in nums:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")
