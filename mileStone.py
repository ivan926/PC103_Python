
price_Of_Child_Meal = float(input("What is the price of a child's meal? "))

price_Of_adult_Meal = float(input("What is the price of a child's meal? "))

numOfChildren = int(input("How many children are there? "))

numOfAdults = int(input("How many adults are there? "))

salesTax = float(input("What is the sales tax rate? "))



print()

subtotal = (price_Of_Child_Meal * numOfChildren) + (price_Of_adult_Meal * numOfAdults

salesTax = subtotal * salesTax

print(f"Subtotal:  {(price_Of_Child_Meal * numOfChildren) + (price_Of_adult_Meal * numOfAdults)}")

print(f"Sales Tax:  {salesTax }")

print(f"Total:  {salesTax + subtotal}")
