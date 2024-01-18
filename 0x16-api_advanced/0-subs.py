#!/usr/bin/python3
""" a function that queries the Reddit API """

import sys
import requests


def number_of_subscribers(subreddit):
    """a function that queries the Reddit API"""
    headers = {"User-Agent": "MyBot/0.0.1"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return
