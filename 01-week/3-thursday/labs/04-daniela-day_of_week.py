day = int(input("Day (0-6)?"))

# 0 is sunday, 1 is monday, 2 is tuesday, 3 is wedsnedsy, 4 is tuesday, 5 is frday, 6 is sat
 
if day == 0:
    print("Sunday")
elif day == 1:
    print ("Monday")
elif day == 2: 
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
else:
    print("not a number between 0-6")