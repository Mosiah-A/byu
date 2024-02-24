import pytest
from datetime import datetime
import csv
from unittest.mock import patch
from io import StringIO
from task_manager import main
from task_manager import add_task, view_tasks, complete_task, remove_task, priority_task



# pytest for add_task function
def test_add_task():
    # Set up initial data
    task_name = "Test task"
    description = "Test Description"
    priority = True
    due_date = "02-28"
    csv_name = 'tasks.csv'

    # Call the add_task function
    add_task( task_name, description, priority, due_date, csv_name)

    # Read the content of the csv file after adding the task
    with open(csv_name, 'r') as file:
        content = file.read()

    # Assert that the added task is present in the csv content
    assert task_name in content
    assert description in content
    assert str(priority) in content
    assert due_date in content
    assert "False" in content

# pytest for view_tasks function
def test_view_tasks(capsys):
    # Set up initial data
    csv_name = 'tasks.csv'

    # Add a task to the CSV for testing
    add_task("Test task", "Test Description", True, "02-28", csv_name)

    # Call the view_tasks function
    view_tasks(csv_name)

    # Capture the printed output
    captured = capsys.readouterr()

    # Print the captured output for debugging
    print("Captured Output:")
    print(captured.out)

    # Assert that the task name is present in the printed output
    assert "Test task" in captured.out


@pytest.fixture
def setup_initial_csv():
    csv_name = 'tasks.csv'
    with open(csv_name, 'w', newline='') as file:
        writer_csv = csv.writer(file)
        datas = [
            ["Date", "Task Name", "Description", "Priority", "Due date (month-day ex: 02-20)", "Completed"],
            ["02 20 2024", "Test task", "Test Description", True, "02-28", "False"]
        ]
        writer_csv.writerows(datas)

def test_complete_task(setup_initial_csv):
    # Call the complete_task function
    task_name_to_complete = "Test task"
    complete_task(task_name_to_complete, 'tasks.csv')

    # Verify that the task is marked as completed
    with open('tasks.csv', 'r') as file:
        reader = csv.DictReader(file)
        completed_values = [row['Completed'] for row in reader if row['Task Name'] == task_name_to_complete]

    assert completed_values == ['True']

def test_remove_task(capsys):
    # Set up initial data
    csv_name = 'tasks.csv'

    # Add a task to the CSV for testing
    add_task("Test Task", "Test Description", True, "02-28", csv_name)

    # Capture the printed output before removing the task
    captured_before = capsys.readouterr()

    # Call the remove_task function
    remove_task(csv_name, "Test Task")

    # Capture the printed output after removing the task
    captured_after = capsys.readouterr()

    # Check that the task has been removed and the appropriate message is printed
    assert "The task 'Test Task' has been removed." in captured_after.out

def test_priority_task():
    task_name_priority = "priority"
    description = "Test Description"
    priority = True
    due_date = "02-28"
    csv_name = 'tasks.csv'

    # Call the add_task function
    add_task( task_name_priority, description, priority, due_date, csv_name)

    # Verify that the task is marked as completed
    with open('tasks.csv', 'r') as file:
        reader = csv.DictReader(file)
        completed_values = [row['Priority'] for row in reader if row['Task Name'] == task_name_priority]

    assert completed_values == ['True']



pytest.main(["-v", "--tb=line", "-rN", __file__])
