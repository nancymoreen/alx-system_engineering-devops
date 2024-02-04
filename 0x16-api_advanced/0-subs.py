#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    if subreddit is None or type(subreddit) is not str:
        return 0
     r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
              headers = {'User-Agent': 'SubscriberCounter:
                      v1.0.0 (by /u/Nancy_Moreen_3103)'}).json()
              subs = r.get("data", {}).get("subscribers", 0)
              return subs

