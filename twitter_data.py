# from searchtweets import ResultStream, gen_request_parameters, load_credentials
#
# premium_search_args = load_credentials('~/.twitter_keys.yaml',
#                                        yaml_key='search_tweets_v2',
#                                        env_overwrite=False)
#
# query = gen_request_parameters('weather', results_per_call=10)
# print(query)



import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)