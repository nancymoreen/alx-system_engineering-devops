#!/usr/bin/python3
"""
This module provides a function to query the Reddit API and return the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom_user_agent'}  # Set a custom User-Agent to avoid Too Many Requests error

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            return data['data']['subscribers']
        except KeyError:
            # Handle the case where the expected data structure is not found
            return 0
    elif response.status_code == 404:
        # Subreddit not found
        return 0
    else:
        # Handle other HTTP response codes if needed
        return 0

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        print("{:d}".format(number_of_subscribers(subreddit)))

