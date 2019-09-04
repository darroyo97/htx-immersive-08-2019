def isEven(x):
    if x % 2 == 0:
        print("True")
        return True
    else:
        print("False")
        return False

x = int(input("Number?"))

isEven(x)