#!/usr/bin/python3
"""Module that consumes the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers (not
    active users, total subscribers) for a given subreddit.

    If not a valid subreddit, return 0.
    Invalid subreddits may return a redirect to search results. Ensure that
    you are not following redirects.

    Args:
        subreddit (str): subreddit

    Returns:
        int: number of subscribers
    """
    if subreddit is None:
        return (0)

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    results = requests.get(url, headers=headers)
    return results.get("data", {}).get("subscribers", 0)
