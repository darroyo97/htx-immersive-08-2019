#Given a histogram tally 
#(one returned from either letter_histogram or word_summary), 
#print the top 3 words or letters.

word = input("Enter word here:")

word_count = {} 
  
for i in word: 
    if i in word_count: 
        word_count[i] += 1
    else: 
        word_count[i] = 1


print(word_count)
