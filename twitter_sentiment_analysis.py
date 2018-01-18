import tweepy
from textblob import TextBlob
import pandas as pan


consumer_api_key='s456zLiJLhnwm8lSR4AtXt9YE'
consumer_secret='cGlvRgoISQuj65JbTGjbzMmY54F0brpUgZK3mpPxkBoSXCtZlk'

access_token='1274870916-GhWZKsoFCF9dOH2eDrKa6XZacwTwXvw09NQS0kz'
access_token_secret='43KuaNXLtMgnCbOh5AkQAf4ns7ivqOR297eFxUxAap6tz'

auth=tweepy.OAuthHandler(consumer_api_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

tweets=api.search(input('Enter your fav topic==>'))
count = 0


with open('tweets.csv','w+') as file:
	for tweet in tweets:
		analysis=TextBlob(tweet.text)
		csv_data=pan.DataFrame({'Tweet':[tweet.text],'Polarity':[analysis.sentiment.polarity],
		'Subjectivity':[analysis.sentiment.subjectivity]},index=[count])
		csv_data.to_csv(file,columns=['Tweet','Polarity','Subjectivity'])
		print(csv_data)
		count=count + 1
	print("No of TWEETS %d" % count)
