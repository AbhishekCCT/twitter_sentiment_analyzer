import tweepy
from textblob import TextBlob

#These keys can be obtained from the developer account you will create at twitter
consumer_key = 'xxxxxxxxxxxxxxxxxxxxxx'
consumer_secret ='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#search by topic
public_tweets = api.search('#BharatRatna')

#create and open file in writing mode
f = open('tweet_Bharat_Ratna.csv' , 'w')

for tweet in public_tweets :
	f.write(tweet.text + '\n\n\n')

for tweet in public_tweets :
	analysis = TextBlob(tweet.text)

	if (analysis.sentiment.polarity > 0 ) :
		f.write(tweet.text + '\n' + 'positive' + ',' + '\n\n\n')

	elif (analysis.sentiment.polarity < 0 ) :
		f.write(tweet.text + '\n'  + 'negetive' + ',' + '\n\n\n')

	elif (analysis.sentiment.polarity == 0) :
		f.write(tweet.text + '\n'  + 'neutral' + ',' + '\n\n\n')


f.close()

f = open('tweet_Bharat_Ratna.csv', 'r')

#printing all the tweets and their sentiment
print(f.read())

f.close()
