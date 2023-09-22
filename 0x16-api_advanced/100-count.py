#!/usr/bin/python3
import requests

def count_words(subreddit, word_list):
    # Define a dictionary to store word counts
    word_counts = {}

    # Define a helper function to recursively fetch and process posts
    def fetch_posts(subreddit, word_list, after=None):
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        params = {"limit": 100, "after": after}
        headers = {"User-Agent": "YourAppName"}  # Set your user agent here

        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            posts = data.get("data", {}).get("children", [])

            for post in posts:
                title = post.get("data", {}).get("title", "").lower()
                for word in word_list:
                    word = word.lower()
                    if word in title:
                        word_counts[word] = word_counts.get(word, 0) + 1

            after = data.get("data", {}).get("after")
            
            # Recursively fetch more posts if there are more pages
            if after:
                fetch_posts(subreddit, word_list, after)

    fetch_posts(subreddit, word_list)

    # Sort word_counts in descending order of counts and alphabetically
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

    # Print the sorted word counts
    for word, count in sorted_word_counts:
        print(f"{word}: {count}")
