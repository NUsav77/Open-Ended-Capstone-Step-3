# Open-Ended Capstone Step 3
Next Generation Weather Radar (NEXRAD) network releases public datasets of both real-time and archival datasets in AWS S3 Buckets. This dataset will be enriched with Twitter sentiments using key-word searches, location/time, and hashtags.

This project utilizes nexradaws module, boto3 SDK, tweepy, searchtweets, and pytz library. Pandas dataframe is used to print Twitter query results.

## Installation for Archive Bucket Access

In terminal 
1. run command ```pip install nexradaws``` to install nexradaws module
2. run command ```pip install pytz``` to install pytz library

## Installation for Real-Time Bucket Access

In terminal
1. run command ```pip install boto3```

## Instalation for Twitter data

In terminal
1. run command ```pip install searchtweets``` - option to obtain Twitter data
2. run command ```pip install searchtweets-v2``` - option to obtain Twitter data
3. run command ```pip install tweepy``` - option to obtain Twitter data
4. run command ```pip install pandas``` - to better analyze Twitter data
5. run command ```pip install spacy```
5. run command ```pip install matplotlib``` - to analyze Twitter data using graphs/charts