# from searchtweets import ResultStream, gen_request_parameters, load_credentials
import secrets  # contains Twitter Dev keys in local
import tweepy
import pandas as pd
import matplotlib.pyplot as plt
import re
import spacy




auth = tweepy.OAuthHandler(secrets.API_Key, secrets.API_Secret_Key)
auth.set_access_token(secrets.Access_Token, secrets.Access_Token_Secret)

api = tweepy.API(auth)

# Cursor object allows us to navigate through Twitter
cursor = tweepy.Cursor(api.user_timeline, id='weatherchannel', tweet_mode='extended').items(1)

# print dir to get the information contained within a single tweet
[print(dir(i)) for i in cursor]

# print full text of a tweet
[print(i.full_text) for i in cursor]



# Cursor object searching for 'tropical storm'
storm_q_cursor = tweepy.Cursor(api.search, q='tropical storm', tweet_mode='extended').items(1)

# print full text of a tweet
[print(i.full_text) for i in storm_q_cursor]



# Get full information on multiple tweets containing a keyword
number_of_tweets = 10
tweets = []
likes = []
time = []

for tweet in tweepy.Cursor(api.search, q='evacuate', tweet_mode='extended').items(number_of_tweets):
    tweets.append(tweet.full_text)
    likes.append(tweet.favorite_count)
    time.append(tweet.created_at)

df = pd.DataFrame({'tweets':tweets,'likes':likes,'time':time})
print(df)



# Remove retweets from query results
df_no_rt = df[~df.tweets.str.contains('RT')]
print(df_no_rt)
