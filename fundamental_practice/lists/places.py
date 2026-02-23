places = ["Vietnam", "Belize", "China", "Japan", "Brazil"]

print(places)

# sorted doesnt modify original list
print(sorted(places))
print(places)

# reverse the view of a sorted list, original not mutated
print(sorted(places, reverse=True))

places.reverse()
print(places)

places.reverse()
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)

# ----------------------------------------------

languages = ["English", "Mandarin", "Spanish", "French", "Swahili", "Russian"]

removed_language = languages.pop()
print(removed_language)

print(languages)

languages.append("German")
print(languages)

languages.reverse()
print(languages)

languages.sort(reverse=True)
print(languages)

languages.insert(0, "Arabic")
print(languages)

languages.sort()
print(languages)

print(f"Length {len(languages)}")
