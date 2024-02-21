
#purpose:  Simple Task Manager
#author: Mosiah Andrade

import os
import csv
from datetime import datetime


def main():
    print("Main")
    csv_name = 'tasks.csv'
    csv_path = os.path.join(os.getcwd(), csv_name)

    #verify if task.csv exist in the same Folder
    if not os.path.exists(csv_path):
    # If false, create a file
        with open(csv_name, 'w', newline='') as file_name:
            writer_csv = csv.writer(file_name)
            
            # write the headline
            datas = [
                ["Date", "Task Name", "Description","Priority", "Due date (month-day ex: 02-20)", "Completed"]
            ]
            
            # write the dates in the csv file
            writer_csv.writerows(datas)
        
        print(f"File '{csv_name}' created successeful")

    answer = True

    #Menu block
    while answer:
        answer = input('(1) Add Task\n(2) View Task\n(3) Complete Task\n(4) Remove Task\n(5) Priority Task\n(6) Quit\n \nEnter your answer: ')
        if answer not in ['1','2','3','4','5','6']:
            print("INVALID ANSWER")
        elif int(answer) == 1:
            task_name = input('Task Name: ').strip().capitalize()
            description = input('Enter quikly description: ')
            priority = None
            while not isinstance(priority, bool):
                priority =  input('Priority (True/False): ').lower()
                if priority == 'true':
                    priority = True
                if priority == 'false':
                    priority = False

            due_date = input('Enter the Due date (02-20): ')
            
            add_task(task_name, description, priority, due_date, csv_name)
        elif int(answer) == 2:
            view_tasks(csv_name)
        elif int(answer) == 3:
            print('Complete Task')
            view_tasks(csv_name)
            choice = input("Enter the task name to mark as completed: ").capitalize().strip()
            complete_task(choice, csv_name)
        elif int(answer) == 4:
            with open(csv_name, 'r') as tasks:
                print('Remove Task')
                reader = csv.DictReader(tasks)
                print_task_list(reader)
            choice_name = input("Enter the task name to remove(ALL para todos): ").strip()

            remove_task(csv_name, choice_name)
        elif int(answer) == 5:
            priority_task(csv_name)
        elif int(answer) == 6:
            break
    print('quit')
def add_task(task, description, priority, due_date, csv_name):
    print("add Task")
    current_date_and_time = datetime.now()
    formated_data = current_date_and_time.strftime('%m %d %Y')
    new_row = [formated_data, task, description, str(priority), due_date, "False"]

    with open(csv_name, 'a', newline='') as task_file:
        csv.writer(task_file).writerow(new_row)

    print('Task appended successfully')
    print()
    print()
    
def view_tasks(csv_name):
    with open(csv_name, 'r') as tasks:
        print("\nTask List:")
        print(f"{'-' * 83}")
        print(f"| {'Date':<20} | {'Task':<20} | {'Description':<20} | {'Priority':<10} | {'Due Date':<10} |")
        print(f"{'-' * 83}")

        reader = csv.DictReader(tasks)
        
        for row in reader:
            completed = row.get("Completed", '').capitalize()
            if completed == 'False':
                date = row.get('Date', '')
                task = row.get('Task Name', '')  
                description = row.get('Description', '')
                priority = row.get('Priority', '')
                due_date = row.get('Due date (month-day ex: 02-20)', '')  
                print(f"| {date:<20} | {task:<20} | {description:<20} | {priority:<10} | {due_date:<10} |")
        print(f"{'-' * 83}")



def find_task_index_by_name(task_name,csv_name):
    with open(csv_name, 'r') as file:
        reader = csv.DictReader(file)
        for index, row in enumerate(reader):
            if row['Task Name'].strip().lower() == task_name.strip().lower():
                return index
    return None

def complete_task(choice, csv_name):
    # finding index by name
    choice_index = find_task_index_by_name(choice, csv_name)

    if choice_index is not None:
        # update status
        with open(csv_name, 'r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        rows[choice_index]['Completed'] = 'True'

        # rewrite the csv file with the task marked as completed
        with open(csv_name, 'w', newline='') as file:
            fieldnames = ['Date', 'Task Name', 'Description', 'Priority', 'Due date (month-day ex: 02-20)', 'Completed']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        print(f"The task '{choice}' has been marked as completed.")
    else:
        print(f"The task '{choice}' was not found.")


def print_task_list(reader):
    print("\nTask List:")
    print(f"{'-' * 83}")
    print(f"| {'Date':<20} | {'Task':<20} | {'Description':<20} | {'Priority':<10} | {'Due Date':<10} |")
    print(f"{'-' * 83}")

    for row in reader:
        completed = row.get("Completed", '').capitalize()
        date = row.get('Date', '')
        task = row.get('Task Name', '')
        description = row.get('Description', '')
        priority = row.get('Priority', '')
        due_date = row.get('Due date (month-day ex: 02-20)', '')
        print(f"| {date:<20} | {task:<20} | {description:<20} | {priority:<10} | {due_date:<10} |")
        
def remove_task(csv_name, choice_name):

    if choice_name is None:
        choice_name = input("Enter the task name to remove(ALL para todos): ").strip()

    if choice_name == 'ALL':
        with open(csv_name, 'w', newline='') as file_name:
            writer_csv = csv.writer(file_name)
            
            # write the headline
            datas = [
                ["Date", "Task Name", "Description","Priority", "Due date (month-day ex: 02-20)", "Completed"]
            ]
            
            # write the dates in the csv file
            writer_csv.writerows(datas)
        print('ALL TASKS DELETED SUCCESSEFUL')
    else:
        with open(csv_name, 'r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        found = False
        updated_rows = []

        for row in rows:
            # Comparing names
            if row['Task Name'].strip().lower() == choice_name.strip().lower():
                found = True
                print(f"Removing task: {row['Task Name']}")
            else:
                updated_rows.append(row)

        if found:
            # rewriting the csv file with task removed
            with open(csv_name, 'w', newline='') as file:
                fieldnames = ['Date', 'Task Name', 'Description', 'Priority', 'Due date (month-day ex: 02-20)', 'Completed']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(updated_rows)

            print(f"The task '{choice_name}' has been removed.")
        else:
            print(f"The task '{choice_name}' was not found.")


def priority_task(csv_name):
    print('Priority Task')
    with open(csv_name, 'r') as tasks:
        print("\nTask List:")
        print(f"{'-' * 83}")
        print(f"| {'Date':<20} | {'Task':<20} | {'Description':<20} | {'Priority':<10} | {'Due Date':<10} |")
        print(f"{'-' * 83}")

        reader = csv.DictReader(tasks)
        
        for row in reader:
            priority = row.get('Priority', '').lower()
            if priority == 'true':
                date = row.get('Date', '')
                task = row.get('Task Name', '')
                description = row.get('Description', '')
                completed = row.get("Completed", '').lower()
                due_date = row.get('Due date (month-day ex: 02-20)', '')
                print(f"| {date:<20} | {task:<20} | {description:<20} | {priority:<10} | {due_date:<10} |")
        print(f"{'-' * 83}")






if __name__ == "__main__":
    main()