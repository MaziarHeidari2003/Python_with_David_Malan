# its like a vending machine we are going to insert some coins to by a soda 
"""
due = 50
coin_sum = 0
print("Amount due: 50")
while coin_sum < 50 :
    coins = int(input("Insert coin: "))
    if coins == 5 or coins == 10 or coins == 25 :
        coin_sum += coins
        if coin_sum > 50:
            break
        print("Amount due: "+ str(50 - coin_sum))
print("change owed: "+str(coin_sum - 50))

"""

amount_due = 50
while amount_due > 0 :
  print("Amount_due: ", amount_due)
  coin = int(input("Insert coin: "))
  if coin in [5,10,25] :
    amount_due -= coin
change_owed = abs(amount_due)
print("change owed: ", change_owed)    