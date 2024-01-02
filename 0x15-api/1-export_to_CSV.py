#!/usr/bin/python3
"""Using a REST API for todo lists of employees"""


import requests
import sys

def fetch_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        if user_response.status_code != 200 or todos_response.status_code != 200:
            print('Failed to retrieve data. Please check the employee ID.')
            return

        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_data['name']
        total_tasks = len(todos_data)
        completed_tasks = [task for task in todos_data if task['completed']]

        print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        fetch_employee_todo_progress(employee_id)
