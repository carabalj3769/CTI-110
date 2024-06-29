# Caraballo, Joseph
# 29 June 2024
# P3LAb
# Creating a Money Float where the program is going to break down the amount of money into different pieces

def breakdown_money(amount):
 if amount == 0:
   return ["No Change"]

 amount_in_cents = round(amount * 100) 
 dollars = amount_in_cents // 100 
 amount_in_cents %= 100 
 
 quarters = amount_in_cents // 25 
 amount_in_cents %= 25 
 
 dimes = amount_in_cents // 10 
 amount_in_cents %= 10 
 
 nickels = amount_in_cents // 5 
 amount_in_cents %= 5 
 
 pennies = amount_in_cents 
 
 results = [] 
 if dollars > 0: 
   results.append(f"{dollars} Dollars") 
 if quarters > 0: results.append(f"{quarters} Quarters") 
 if dimes > 0: results.append(f"{dimes} Dimes") 
 if nickels > 0: results.append(f"{nickels} Nickels") 
 if pennies > 0: results.append(f"{pennies} Pennies") 
 
 return results 

def main(): 
    amount = float(input("Enter the amount of money as a float: $")) 
    breakdown = breakdown_money(amount) 
    for part in breakdown: print(part) 
    
if __name__ == "__main__": main()