import csv
I_NUM_INDEX = 0
NAME_INDEX = 1

def main():
        search_ID = input('Please enter an I-Number (xxxxxxxx): ')

        student = read_dictionary('students.csv', I_NUM_INDEX, search_ID)

        print(student)

def read_dictionary(filename, key_column_index, search_student):
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
                key = row_list[key_column_index]

                if key == search_student:
                      return row_list[1]
                else:
                      return "No such Student"


if __name__ == '__main__':
        main()