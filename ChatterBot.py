# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "PKQK1IXOsnSxcv7LEuejMMVFM"
consumer_secret = "dVUQcsUlKw4uC5KLLDuK9FUtgCWadzCJzx9eqgOUjSh83oG8AM"
access_token = "967430128237244421-WDEZ5qvwMFDWlFSRFFuKFivITDATdpn"
access_token_secret = "4tVHJVVvDr8vtiq1Vh4Bsp5pfK6aqqsg71CUHzu3zjAkl"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE