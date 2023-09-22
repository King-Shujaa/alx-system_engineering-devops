#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""

import requests

def count_words(subreddit, word_list, after=None, word_dict=None):
    """ A function that queries the Reddit API parses the title of
    all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces.
    Javascript should count as javascript, but java should not).
    If no posts match or the subreddit is invalid, it prints nothing.
    """

    if word_dict is None:
        word_dict = {word.lower(): 0 for word in word_list}

    if after is None:
        word_dict_sorted = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in word_dict_sorted:
            if count:
                print('{}: {}'.format(word, count))
        return

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-Agent': 'redquery'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    try:
        data = response.json()['data']
        hot = data['children']
        aft = data['after']
        
        for post in hot:
            title = post['data']['title'].lower()
            
            for word in word_dict:
                word_dict[word] += title.count(word)
    
    except Exception:
        return

    count_words(subreddit, word_list, aft, word_dict)
