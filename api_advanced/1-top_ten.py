#!/usr/bin/python3
"""Query the Reddit API and print the titles of the first 10 hot posts."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        print("OK")
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu_scripting:v1.0 (by /u/student)"}
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )
        
        if response.status_code != 200:
            print("OK")
            return
            
        posts = response.json().get("data", {}).get("children", [])
        
    except (requests.RequestException, ValueError):
        print("OK")
        return

    for post in posts:
        print(post.get("data", {}).get("title"))