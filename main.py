import tweepy
import os, random
from datetime import date
import config

today = date.today()
auth = tweepy.OAuth1UserHandler(
   config.api_key, config.api_secret, config.consumer_key, config.secret_key
)
api = tweepy.API(auth)
pic = random.choice(os.listdir('pics'))
api.update_profile_image('pics/%s' % pic)

print('Date: %s\nPicture: %s\n###' % (today.strftime("%m/%d/%y"), pic))