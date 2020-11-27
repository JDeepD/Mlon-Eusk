import json
import praw  # pylint: disable=import-error


with open(r'apis/creds/creds.json', 'r') as jsdat:
    data = json.load(jsdat)
reddit = praw.Reddit(**data["reddit"])


def jokes(val="Jokes"):  # pylint: disable=all
    sub = reddit.subreddit(val).random()
    return sub.title, sub.selftext, sub.url


def meme(val="gifs"):
    sub = reddit.subreddit(val).random()
    return sub.title, sub.url
