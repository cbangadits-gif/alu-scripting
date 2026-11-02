#!/usr/bin/python3
"""Recursively query the Reddit API and return titles of all hot posts."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of titles of all hot posts, or None if invalid."""
    if hot_list is None:
        hot_list = []
    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu_scripting:v1.0 (by /u/student)"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )
        if response.status_code != 200:
            return None
        data = response.json().get("data", {})
    except (requests.RequestException, ValueError):
        return None

    for post in data.get("children", []):
        hot_list.append(post.get("data", {}).get("title"))

    after = data.get("after")
    if after is None:
        return hot_list if hot_list else None
    return recurse(subreddit, hot_list, after)
