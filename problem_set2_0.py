# we are going to get an input in camel case and hand back the snake case
# remember that in python the strings are immutable, meaning that you cant change a simple charactor within a string
# when you use for loop to iterate in an string the  item recieves the char dirctly so you dant have to use index
"""
n = input("Enter: ")
new_n = ""
for letter in n :
  if letter.isupper() :
    new_n += "_" + letter.lower()
  else : 
    new_n += letter  
print(new_n)   
print() 

"""

camleCase = input("Enter the camlecase: ")
print("snake_case: ", end = "")
for letter in camleCase :
  if letter.isupper():
    print("_"+letter.lower(), end = "")
  else:
    print(letter,end = "")
print()      