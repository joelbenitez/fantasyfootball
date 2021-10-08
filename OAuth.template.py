from yahoo_oauth import OAuth2
import json
creds = {'consumer_key': 'YourConsumerKey', 'consumer_secret': 'YourConsumerSecret'}
with open("oauth2.json", "w") as f:
   f.write(json.dumps(creds))
oauth = OAuth2(None, None, from_file='oauth2.json')