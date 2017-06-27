import tweepy

access_token = 'Get from Twitter API'
access_token_secret = 'Get from Twitter API'
consumer_key = 'Get from Twitter API'
consumer_secret = 'Get from Twitter API'

def login(consumer_key, consumer_secret):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	return api
		
def batch_delete(api):
	print("Are you sure you want to delete all tweets?")
	response = input("> ")
	if response.lower() == 'yes':
		for status in tweepy.Cursor(api.user_timeline).items():
			try:
				api.destroy_status(status.id)
				print("deleted ", status.id)
			except:
				print("failed to delete ", status.id)
			
if __name__ == "__main__":
	api = login(consumer_key, consumer_secret)
	batch_delete(api)



		
