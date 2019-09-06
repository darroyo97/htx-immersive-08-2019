def Remove(names): 
    list1 = [] 
    for x in names: 
        if x not in list1: 
            list1.append(x) 
    return list1 
       
names = ['Alex', 'John', 'Mary', 'Steve', 'John', 'Steve'] 

print(Remove(names))