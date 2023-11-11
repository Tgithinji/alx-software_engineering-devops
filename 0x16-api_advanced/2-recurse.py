#!/usr/bin/python3
"""2-recurse module"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries reddit api and returns a list containing
    the titles of all hot articles in a subreddit
    """
    if len(hot_list) >= 100 or after == 'STOP':
        return hot_list

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        posts = response.json()['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        after = response.json()['data']['after']
        return recurse(subreddit, hot_list, after)
    else:
        return None
