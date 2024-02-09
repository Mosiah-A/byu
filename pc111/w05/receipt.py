import csv
from datetime import datetime
import sys

# Constants for column indices in the CSV files
key_column_index = 0
product_name = 0
price = 1
quantity = 1

def main():
    # Initialize variables
    total_of_item = 0
    subtotal = 0.00
    tax = 0.06
    emporium_name = 'Inko Emporium'

    # Display the emporium name
    print(emporium_name)
    
    try:
        # Read the products dictionary from 'products.csv'
        products_dic = read_dictionary('pc111/w05/products.csv', key_column_index)
    except FileNotFoundError as file_error:
        # Handle the case where 'products.csv' is missing
        print(f"Error: missing file\n{file_error}")
        sys.exit()

    # Print an empty line
    print()

    # Initialize a list to store requested items
    request_list = []

    # Read and process the 'request.csv' file
    with open('pc111/w05/request.csv', 'rt') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Skip the header row
        next(csv_reader)

        # Iterate through each row in the 'request.csv'
        for row in csv_reader:
            product_name_request = row[0].strip()
            product_quantity_request = int(row[1])

            # Accumulate the total quantity of items
            total_of_item += product_quantity_request

            # Get product information from the products dictionary
            product_in_dict = products_dic.get(product_name_request)
            
            # Check if the product is not found in the dictionary
            if product_in_dict is None:
                raise KeyError(f"Product {product_name_request} not found in the products dictionary.")

            # Extract product information
            product_name_in_dic = product_in_dict[1].strip()
            product_price_in_dic = float(product_in_dict[2])

            # Calculate the sum of the price for the given quantity
            sum_price = product_price_in_dic * product_quantity_request
            subtotal += sum_price

            # Add the product name to the request list
            request_list.append(product_name_in_dic)

            # Calculate and display information about the product, quantity, and price
            print(f'{product_name_in_dic}: {product_quantity_request} @ {product_price_in_dic}')

    # Print an empty line
    print()

    # Get the current date and time
    current_date_and_time = datetime.now()

    # Display summary information
    print(f'Number of Items: {total_of_item}')
    print(f'Subtotal: {subtotal:.2f}')
    print(f'Sales Tax: {sales_tax:.2f}')

    # Apply a discount if the current day is Tuesday or Wednesday
    if current_date_and_time.weekday() == 1 or current_date_and_time.weekday() == 2:
        total = total - total * 0.1

    print(f'Total: {total:.2f}')

    # Print an empty line
    print()

    # Display a thank you message and the current date and time
    print(f'Thank you for shopping at the {emporium_name}.')
    print(f"{current_date_and_time:%A %I:%M %p}")

# Function to read the products dictionary from a CSV file
def read_dictionary(filename, key_column_index):
    dictionary = {}
    with open(filename, 'rt') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Skip the header row
        next(csv_reader)

        # Iterate through each row in the CSV file
        for row in csv_reader:
            key = row[key_column_index]
            name, price = row[1], row[2]
            dictionary[key] = [key, name, price]

    return dictionary

# Entry point of the script
if __name__ == '__main__':
    main()
