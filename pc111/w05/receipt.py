import csv
key_column_index = 0 

def main():
    dictionary = read_dictionary('products.csv')
    print(dictionary)

def read_dictionary(filename):

    dictionary= {}
    with open(filename, 'rt') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)

        for row in csv_reader:
            
            product, name, price = row
            dictionary[student_id]= [name, price]
    return dictionary
                           
                
                  

if __name__ == '__main__':
    main()