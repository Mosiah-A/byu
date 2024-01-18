shopping_cart = [
    ["chips", 2.99],
    ["bread", 2.50], 
    ["Milk", 3.19], 
    ["Ice Cream", 6.99],
    ["Cheese", 5.99],
    ["Candy bar", 0.99]
]

max_price = -1
max_product = ''

for item in shopping_cart:
    product_name = item[0]
    prince = item[1]

    if prince > max_price:
        max_price = prince
        max_product = product_name

print(f"The maximum product with maximum price is {max_product} ${max_price}")