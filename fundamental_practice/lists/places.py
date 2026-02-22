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