#!/usr/bin/python3
"""100-count module"""
import requests


def count_words(subreddit, word_list, list_found=[], after=None):
    """
    Recursive function that queries the Reddit API,
    parses the title of all hot articles
    prints a sorted count of given keywords
    """
    url = 'http://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    if after is None:
        word_list = [word.lower() for word in word_list]

    if response.status_code == 200:
        data = response.json()['data']
        after = data['after']
        posts = data['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in title.split(' '):
                if word in word_list:
                    list_found.append(word)
        if after is not None:
            count_words(subreddit, word_list, list_found, after)
        else:
            res = {}
            for word in list_found:
                if word.lower() in res.keys():
                    res[word.lower()] += 1
                else:
                    res[word.lower()] = 1
            for key, value in sorted(res.items(),
                                     key=lambda item: item[1], reverse=True):
                print('{}: {}'.format(key, value))
    else:
        return None
