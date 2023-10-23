#!/usr/bin/python3
"""
This script gets data from an API
"""
import requests
import sys


if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com'
    user = requests.get('{}/users/{}'.format(base_url, sys.argv[1])).json()
    todo_list = requests.get('{}/todos?userId={}'.
                             format(base_url, sys.argv[1])).json()

    completed = []
    for todo in todo_list:
        if todo.get('completed'):
            completed.append(todo.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format
          (user.get('name'), len(completed), len(todo_list)))
    for task in completed:
        print('\t {}'.format(task))
