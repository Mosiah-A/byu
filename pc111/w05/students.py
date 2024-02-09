import csv
I_NUM_INDEX = 0
NAME_INDEX = 1

def main():
    search_ID = input('Please enter an I-Number (xxxxxxxx): ')
    student = read_dictionary('students.csv', I_NUM_INDEX)
    student = student[search_ID]
    print(student[NAME_INDEX])

def read_dictionary(filename, key_column_index):
        """Read the contents of a CSV file into a compound
        dictionary and return the dictionary.
    
        Parameters
            filename: the name of the CSV file to read.
            key_column_index: the index of the column
                to use as the keys in the dictionary.
        Return: a compound dictionary that contains
            the contents of the CSV file.
        """
        dictionary = {}
        

        with open(filename, 'rt') as students_csv:
                
            reader = csv.reader(students_csv)

            next(reader)

            for row_list in reader:

                if len(row_list) != 0:

                    # From the current row, retrieve the data
                    # from the column that contains the key.
                    key = row_list[key_column_index]

                    # Store the data from the current
                    # row into the dictionary.
                    dictionary[key] = row_list
            return dictionary


if __name__ == '__main__':
        main()
