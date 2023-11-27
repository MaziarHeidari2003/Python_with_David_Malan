""""
def main():
  print_column(3)
def print_column(height):
    print("#\n"* height , end="")  
main()
"""
"""
def print_square(size):
  for i in range(size):
    for j in range(size):
      print("#",end="")
    print()  

print_square(4)    
"""
for i in range(5):
  print("#" * 5)