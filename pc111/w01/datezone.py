from datetime import datetime

dt = datetime.now()

wd = (dt.weekday())


subtotal = float(input('Please enter the subtotal: '))
tax = subtotal * 0.06
discount = subtotal * 0.1


if wd == 1 or wd == 2:
    if subtotal >= 50:
        print(f'Discount amount: {discount:.2f}')
        tax = (subtotal - discount) * 0.06
        print(f'Sales Tax amount: {tax:.2f}')
        print(f'Total: {subtotal + tax - discount:.2f}')
    
    else:
        print(f'Sales Tax amount: {tax:.2f}')
        print(f'Total: {subtotal + tax :.2f}')
else:
    print(f'Sales Tax amount: {tax:.2f}')
    print(f'Total: {subtotal + tax :.2f}')