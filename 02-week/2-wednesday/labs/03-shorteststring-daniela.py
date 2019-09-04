animals = ["Elephant", "Tiger", "Chicken", "Lion"]

def shortest(animals):
    return min(animals, key=len)

print(shortest(animals))    

