import pandas as pd

def process_tweets(tweets):
    """Processa os tweets em um DataFrame."""
    data = [
        {
            "user": tweet.user.screen_name,
            "text": tweet.text,
            "created_at": tweet.created_at,
            "likes": tweet.favorite_count,
            "retweets": tweet.retweet_count,
        }
        for tweet in tweets
    ]
    return pd.DataFrame(data)

