import tweepy
import settings

consumer_key = 'kK1HOL2VHpALx6cusvDSQYxGq'
consumer_secret = 'XzXRrYEJkGbODliTH1FiXlClIE9dpeI0dHJDSpif6FS94iUVRY'
access_token = '851934408085037058-fefMA6orZtkrZ1noznia7sGTobEO5uh'
access_token_secret = 'GwLgCUjuDTyvbbMtnUhwp1KsHeivoumVPnu8rYecEdSes'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Write a tweet to push to our Twitter account
tweet = settings.data
api.update_status(status=tweet)
