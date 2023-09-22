#!/usr/bin/python3
import praw
import re
def count_words(subreddit, word_list):
    # Convert word_list to lowercase and split it into a list of words
    word_list = [word.lower() for word in word_list.split()]
    # Create a praw instance
    reddit = praw.Reddit(client_id='', client_secret='', user_agent='')
    # Get the hot posts from the subreddit
    posts = reddit.subreddit(subreddit).hot(limit=100)
    # Create a dictionary to store the word counts
    word_counts = {}
    # Recursively call the function on each post
    for post in posts:
        count_words_in_post(post, word_list, word_counts)
    # Sort the word counts in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    # Print the word counts
    for word, count in sorted_word_counts:
        print(f"{word}: {count}")
def count_words_in_post(post, word_list, word_counts):
    # Get the title of the post
    title = post.title.lower()
    # Remove any words that are not in the word list
    words = [word for word in title.split() if word in word_list]
    # Count the words
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    # Recursively call the function on the comments
    for comment in post.comments:
        count_words_in_post(comment, word_list, word_counts)
