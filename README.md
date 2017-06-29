# tweepysri
```
Simple Twitter image post based on Tweepy
```

Twitter feed for Smile with yoga

To use this program, put your Twitter OAuth credentials in `oauth.json` (or customize this path in `tweepysri.py`). 
oauth.json should look like

```
{
    "consumer_key": "...",
    "consumer_secret": "...",
    "access_token": "...",
    "access_token_secret": "..."
}
```
We can post simple twitter post or with image. 
If the `image` field in `settings.py` is 
- loaded with image name, then its twitter post with image
- empty, then its twitter post

The tweet data is in `settings.data`. Populate the `data` field which needs to be tweeted.

```
Note: follow below link for setting your twitter account:
https://www.digitalocean.com/community/tutorials/how-to-create-a-twitter-app
```
