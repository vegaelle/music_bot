from time import *
import tweepy
from gen import *

passwords = open('keys.txt', 'r')

consumer_key = passwords.readline()[:-1]
consumer_secret = passwords.readline()[:-1]
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

access_key = passwords.readline()[:-1]
access_secret = passwords.readline()[:-1]

auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

while True :
    g = genre_cplx()
    api.update_status(g)
    print("Tweeting : ", g, " at ", localtime(time()))
    sleep(7200)
