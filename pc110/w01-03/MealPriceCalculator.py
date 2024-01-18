#Author: Mosiah Andrade

#Purpose: Calculate meal price

#I add a ask about if the person want a table and to make a reserve and hava output telling the informations about your reserve

#taking information about price and how many person are there
child_meal = input("What is the price of a child's meal? ")
adult_meal = input("What is the price of a adult's meal? ")
Children_number = input("How many children are there? ")
adult_number = input("How many adults are there? ")

#asking about reserve time
table_for = int(adult_number) + int(Children_number)
hour = input("What time do you want reseve? (07 PM / 08 PM / 09 PM ) ")

#calculate subtotal
subtotal = float(child_meal) * int(Children_number) + float(adult_meal) * int(adult_number)
print(f"Subtotal: ${subtotal}")

#calculate the tax
sales_tax_rate = input("What is the sales tax rate? ")
sales_tax = int(sales_tax_rate) * subtotal / 100
print(f"Sales Tax: ${sales_tax:.2f}")

#outpur total to pay
total = sales_tax + subtotal
print(f"Total: ${total:.2f}")

#Calculate the paymant
paymant_amount = input("What is the payman amount? ")
change = int(paymant_amount) - total
print(f"Change: ${change:.2f}")

#Reserve information
print("RESERVED!!")
print(f" A table for {table_for} at {hour}")