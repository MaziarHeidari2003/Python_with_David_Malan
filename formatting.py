animal = "cow"
item = "moon"

#print("the "+animal+" jumped over the "+item)
#print("the {1} jumped over the {0}".format(animal,item)) #positional arguements
#print("the {animal} jumped pver the {item}".format(animal = "cow", item = "moooon")) # key word arguement 
text = "the {} jumped over the {}"
print(text.format(animal,item))


name = "Maziar"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:<10} nice to meet you".format(name))
print("Hello, my name is {:>10} nice to meet you".format(name))
print("Hello, my name is {:^10} nice to meet you".format(name))


pi = 3.14159
print("The number is {:.2f}".format(pi))


