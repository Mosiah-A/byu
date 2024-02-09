import csv

key_column_index = 0 
product_name = 0
price = 1
quantity = 1

def main():
    products_dic = read_dictionary('pc111/w05/products.csv')
    
    print(f'All products\n{products_dic}')
    print()

    with open ('pc111/w05/request.csv', 'rt') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)
        print('Requested Items')
        for row in csv_reader:
            product_name_request = row[0]
            product_quantity_request = row[1]
            product_in_dict = products_dic.get(product_name_request)
            product_name_in_dic = product_in_dict[1]
            product_price_in_dic = product_in_dict[2]
            print(f'{product_name_in_dic}: {product_quantity_request} @ {float(product_price_in_dic)}')

def read_dictionary(filename):
    dictionary = {}
    with open(filename, 'rt') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)

        for row in csv_reader:
            key = row[key_column_index]
            name, price = row[1], row[2]
            dictionary[key] = [key,name, price]
            

    return dictionary

if __name__ == '__main__':
    main()
