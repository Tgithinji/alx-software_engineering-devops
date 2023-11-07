#!/usr/bin/python3
"""subs module"""
import requests


def top_ten(subreddit):
    """
    Gets the title of hottest post
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        posts = response.json()['data']['children'][:10]
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
