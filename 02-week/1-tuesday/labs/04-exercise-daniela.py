def word_count(string):
  my_string = string.lower().split()
  my_dict = {}
  for item in my_string:
    my_dict[item] = my_string.count(item)
  print(my_dict)

word_count(input("Enter phrase here:"))

