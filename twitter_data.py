# from searchtweets import ResultStream, gen_request_parameters, load_credentials
#
# premium_search_args = load_credentials('~/.twitter_keys.yaml',
#                                        yaml_key='search_tweets_v2',
#                                        env_overwrite=False)
#
# query = gen_request_parameters('weather', results_per_call=10)
# print(query)



import tweepy
import secrets

auth = tweepy.OAuthHandler(secrets.API_Key, secrets.API_Secret_Key)
auth.set_access_token(secrets.Access_Token, secrets.Access_Token_Secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)