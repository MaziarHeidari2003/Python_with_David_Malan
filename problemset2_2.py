"""
In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
"""

def main() :
  plate = input("Enter the plate: ")
  if is_valid(plate):
      print("Valid")
  else:
      print("Invalid")

def is_valid(plate):
    if 2 > len(plate)  or len(plate) > 6 :
        return False
    if plate[0].isalpha() == False  or plate[1].isalpha() == False:
        return False
    i = 0
    while i < len(plate) :
        if plate[i].isdigit() == True :
            if plate[i] == '0' :
                return False
            else:
                break
        i += 1
    x = (len(plate) - 1)    
    if plate[-1].isalpha() :
        while x >= 0 :
            if plate[x].isdigit():
                return False
            x -= 1    
            
    for c in plate :
        if c in ['.','!','?','.',' '] :
            return False
    return True            

main()