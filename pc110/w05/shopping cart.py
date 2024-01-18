'''
Author: Mosiah Andrade

Purpose: calculate a cart value and manipule them, adding more items and removing them.

added a delivery option calculing the price according the distance of there
'''



cart = []
prices = []
answer = ''
item = ''
sum = 0
#km = 0
#km_price = 0

while answer != '5':
    #menu block:
    print('''
Please select one of following:
1. add item
2. view cart
3. remove item
4. compute total
5. Quit
''')
    answer = input("Please enter an action: ")
    if answer ==  '1':
        print('-' * 50)
        #add block
        item = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{item}' ? "))
        print(f"{item} has been added to cart")
        cart.append(item)
        prices.append(price)
        print('-' * 50)

    elif answer == '2':
        if len(cart) == 0: 
            print('-' * 50)
            print('The cart is blank')
            print('-' * 50)
        else:
            print('-' * 50)
            #view chart block
            for i in range(len(cart)):
                print(f"{i + 1}. {cart[i]} - ${prices[i]:.2f}")
            print('-' * 50)

    elif answer == '3':
        if len(cart) == 0: 
            print('-' * 50)
            print('The cart is blank')
            print('-' * 50)

        else:
            #view chart block
            print('-' * 50)
            for i in range(len(cart)):
                print(f"{i + 1}. {cart[i]} - ${prices[i]:.2f}")
            print('-' * 50)

            #remove block
            remove = int(input("which item wold you like to change? "))
            while remove > len(cart) or remove < 0:
                print('-' * 50)
                print("Sorry, that is not a valid item number.")
                remove = int(input("which item wold you like to change? "))
            cart.pop(remove - 1)
            prices.pop(remove - 1)
            print("Item removed")
            print('-' * 50)

    elif answer == '4':
        if len(cart) == 0: 
            print('-' * 50)
            print('The cart is blank')
            print('-' * 50)

        else:
            #total
            print('-' * 50)
            #delivery block
            delivery = input("Do you need a delivery? [y/n] ")
            if delivery == 'y'or delivery == 'Y':
                km = int(input('how many km distance of  there? '))
                km_price = km * 2

            for price in prices:
                sum += price
            
            #view chart block
            for i in range(len(cart)):
                print(f"{i + 1}. {cart[i]} - ${prices[i]:.2f}")
            print('-' * 50)
            print(f"The subtotal price of the items in the shopping cart is ${sum:.2f} \n+ Delivery ${km_price:.2f} \nTotal ${sum + km_price :.2f}")
            sum = 0 # reset variable to evit bug when the user want to view the total
            print('-' * 50)
            answer = '5'
        

    elif answer == '5':
        print("Thank You. Good bye *-* ")

    else:
        print("Invalid Answer")