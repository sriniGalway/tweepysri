import os, json
import tweepy
import settings

### setting the directory
directory = os.path.expanduser('~/Downloads/twitter/')
file = directory + settings.image
print directory
status_log_file = directory + '/status.log'

### set up oauth
oauth_json_file = os.path.expanduser('oauth.json')
if not os.path.exists(oauth_json_file):
    print_error('no ' + oauth_json_file)
    exit(1)

oauth = json.loads(open(oauth_json_file, 'r').read())

auth = tweepy.OAuthHandler(oauth['consumer_key'], oauth['consumer_secret'])
auth.set_access_token(oauth['access_token'], oauth['access_token_secret'])
api = tweepy.API(auth)

# Write a tweet to push to our Twitter account
tweet = settings.data

msglen = len(tweet)
if msglen > 140:
   print "length of message is " + str(msglen)
   print "The Number of character is more than 140." 
   exit()

if file is not directory:
    fn = os.path.abspath(file)
    api.update_with_media(fn, status=tweet)
else:
    api.update_status(status=tweet)
