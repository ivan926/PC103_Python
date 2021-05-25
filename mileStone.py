
price_of_child_meal = float(input("What is the price of a child's meal? "))

price_of_adult_meal = float(input("What is the price of a adult's meal? "))

num_of_children = int(input("How many children are there? "))

num_of_adults = int(input("How many adults are there? "))

num_of_drinks = int(input("How many drinks would you like? "))

price_per_drink = float(input("What is the price of a drink? "))

amount_of_appetizer = int(input("How many appetizers would you like? "))

price_of_appetizer = float(input("What is the price of the appetizer? "))

sales_tax_input = float(input("What is the sales tax rate? "))

sales_tax_input = sales_tax_input / 100

#Finding the total price of drinks

total_drink_price = price_per_drink * num_of_drinks

#finding the price of appetizer

total_appetizer_price = price_of_appetizer * amount_of_appetizer




print()

#finding the subtotal

subtotal = ((price_of_child_meal * num_of_children) + total_drink_price + total_appetizer_price + (price_of_adult_meal * num_of_adults))

sales_tax = (subtotal * sales_tax_input)



print(f"Subtotal:  ${subtotal:.2f}")

print(f"Sales Tax:  ${sales_tax:.2f}")

total_amount = sales_tax + subtotal

print(f"Total:  ${total_amount:.2f}")

print()

payment_amount = float(input("What is the payment amount? "))

total_amount = payment_amount - (sales_tax + subtotal)

print(f"Change: ${total_amount:.2f}")
