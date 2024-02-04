#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests
import sys


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        results = response.json().get("data")
        subscribers_count = results.get("subscribers")
        print(subscribers_count)
        return subscribers_count
    elif response.status_code == 404:
        print(0)
        return 0
    else:
        print(0)
        return 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        number_of_subscribers(sys.argv[1])

