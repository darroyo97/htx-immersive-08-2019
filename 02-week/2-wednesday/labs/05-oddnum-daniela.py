import evennum_daniela

def isOdd(x):
    if evennum_daniela.isEven(x) == True:
        return False
    else:
        return True

x = int(input("Number?"))

print(isOdd(x))