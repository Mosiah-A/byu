import csv

def main():
    id = input('Please enter an I-Number (xxxxxx):')
    dictionary = read_dictionary('students.csv')
    name_of_student = dictionary.get(id, 'No such student') 
    print(name_of_student)



def read_dictionary(filename):
        """Read the contents of a CSV file into a compound
        dictionary and return the dictionary.
    
        Parameters
            filename: the name of the CSV file to read.
            key_column_index: the index of the column
                to use as the keys in the dictionary.
        Return: a compound dictionary that contains
            the contents of the CSV file.
        """
        dictionary= {}
        with open(filename, 'rt') as csv_file:
            csv_reader = csv.reader(csv_file)

            next(csv_reader)

            for row in csv_reader:
                
                student_id, name = row
                dictionary[student_id]= name
        return dictionary
                
                  




if __name__ == "__main__":
    main()
