import tweepy

class TwitterClient:
    def __init__(self, api_key, api_secret_key, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(api_key, api_secret_key)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def search_tweets(self, query, count=100, lang="pt"):
        return self.api.search_tweets(q=query, count=count, lang=lang)
