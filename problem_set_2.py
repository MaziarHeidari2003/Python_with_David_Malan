# we are going to get an input in camel case and hand back the snake case
# remember that in python the strings are immutable, meaning that you cant change a simple charactor within a string

n = input("Enter: ")
new_n = ""
for char in n :
  if char.isupper():
    new_n += "_" + char.lower()
  else:
    new_n += char
print(new_n)       