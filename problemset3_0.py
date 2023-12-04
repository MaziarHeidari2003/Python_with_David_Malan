while True:
  fuel = input("Fraction: ")
  try:
    numerator,denominator = fuel.split("/")
    new_numerator = int(numerator)
    new_denominator = int(denominator)
    percentage = new_numerator / new_denominator
    if percentage <= 1 :
      break 
  except (ValueError, ZeroDivisionError) :  
    pass
percentage = int(percentage * 100)
if (percentage) <= 1 :
  print("E")  
elif (percentage) >= 99 :
  print("F")  
else :
  print(f"{percentage}%")

    