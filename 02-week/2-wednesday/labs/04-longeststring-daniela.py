animals = ["Elephant", "Tiger", "Chicken", "Lion"]

def longest(animals):
    return max(animals, key=len)

print(longest(animals))