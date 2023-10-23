#!/usr/bin/python3
"""
This script gets data from an API and exports it in CSV
"""
import requests
import sys


if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com'
    user = requests.get('{}/users/{}'.format(base_url, sys.argv[1])).json()
    todo_list = requests.get('{}/todos?userId={}'.
                             format(base_url, sys.argv[1])).json()

    filename = '{}.csv'.format(sys.argv[1])
    with open(filename, 'w') as file:
        for task in todo_list:
            file.write('"{}","{}","{}","{}"\n'.format(
                sys.argv[1], user.get('username'),
                task.get('completed'), task.get('title')))
