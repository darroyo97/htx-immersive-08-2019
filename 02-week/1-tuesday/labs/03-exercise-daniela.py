#print ('Hello Dani!')

#word = input(' Enter a word here:')

#Alphabet = [
#    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#    'u', 'v', 'w', 'x', 'y', 'z'
#]

#word_count = [
#    (Alphabet[i], word.count(Alphabet[i]))
#    for i in range(len(Alphabet))
#    if word.count(Alphabet[i])
#]

#print(word_count)

#code will NOT tally a letter if typed in caps. 

word = input("Enter phrase here:")

word_count = {} 
  
for i in word: 
    if i in word_count: 
        word_count[i] += 1
    else: 
        word_count[i] = 1



print(word_count)
