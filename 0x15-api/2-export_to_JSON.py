#!/usr/bin/python3
"""
This script gets data from an API and exports to JSON
"""
import json
import requests
import sys


if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com'
    user = requests.get('{}/users/{}'.format(base_url, sys.argv[1])).json()
    todo_list = requests.get('{}/todos?userId={}'.
                             format(base_url, sys.argv[1])).json()

    json_dict = {sys.argv[1]: []}
    for todo in todo_list:
        json_dict[sys.argv[1]].append({
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": user.get('username')
        })

    filename = '{}.json'.format(sys.argv[1])
    with open(filename, 'w') as file:
        json.dump(json_dict, file)
