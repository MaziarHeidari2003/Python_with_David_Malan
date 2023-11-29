"""
try:
  x = int(input("Enter: "))
except ValueError:
  print("x is not an integer")
else:  
  print(f"x is {x}")    
"""
"""

while True:
  try: 
    x = int(input("Enter: "))
  except ValueError:
    print("x is not an integer")
  else:
    break
print(f"x is {x}")  
"""
def main():
  x= get_int()
  print(f"x is {x}")


def get_int():
  while True:
    try:
      #return int(input("Enter"))
      x= int(input("Enter: "))
      return x
    except ValueError:
      print("x is not an integer")

main()