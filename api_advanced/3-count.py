#!/usr/bin/python3
"""Recursively count keywords in the titles of a subreddit's hot posts."""
import requests


def count_words(subreddit, word_list, counts=None, after=None):
    """Print a sorted count of keywords found in hot post titles."""
    if counts is None:
        counts = {}
    if subreddit is None or not isinstance(subreddit, str):
        return

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
            return
        data = response.json().get("data", {})
    except (requests.RequestException, ValueError):
        return

    for post in data.get("children", []):
        title = post.get("data", {}).get("title") or ""
        for word in title.lower().split():
            counts[word] = counts.get(word, 0) + 1

    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, counts, after)

    totals = {}
    for word in word_list:
        key = word.lower()
        totals[key] = totals.get(key, 0) + counts.get(key, 0)

    results = [(word, total) for word, total in totals.items() if total > 0]
    results.sort(key=lambda item: (-item[1], item[0]))
    for word, total in results:
        print("{}: {}".format(word, total))
