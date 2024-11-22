import praw
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


reddit = praw.Reddit(
    client_id="w-H3wffb9s6nrOzq8p04Tw",
    client_secret="99vqay0FggpVckjRM1LU1SmAOK10Lg",
    user_agent="my_reddit_app v1.0 by /u/EastButterscotch3819"
)

def fetch_reddit_data(keyword, subreddit="all", limit=50):
    """
    Fetch Reddit posts based on a keyword.
    """
    posts = reddit.subreddit(subreddit).search(keyword, limit=limit)
    data = [{"title": post.title, "text": post.selftext} for post in posts]
    return data

def analyze_sentiment(text):
    """
    Analyze sentiment using VADER.
    """
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(text)
