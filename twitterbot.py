from fileinput import filename
from multiprocessing.connection import Client
import tweepy
import random
import time, threading 

API_KEY = ""
API_SECRET = ""

ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Connecté !")
except:
    print("Non connecté :(")

max_tweets = 200
max_image = 12
liste_mot_cherche = ['#SPYFAMILY','#スパイファミリー','#SPYxFamily','#SPY_FAMILY'] # A compléter : liste des mots qui vont être successivement cherché par le bot

i=1

def nom_auteur_tweet(sentence):
    nom=sentence[3:]
    i=0
    for lettre in nom:
        if(lettre!=':'):
            i+=1
        else:
            break
    nom=nom[:i]
    return nom

def behaviorTwitteraccount():
    print(time.ctime())
    for mot_cherche in liste_mot_cherche : 
        tweets = tweepy.Cursor(api.search_tweets, q=mot_cherche).items(max_tweets)
        for tweet in tweets:
            #i=random.randint(1,max_image)
            try:
                api.retweet(tweet.id)
                print("Succès")
                print(i)
                i+=1
                ## Twitter ne me laisse pas faire ce qui suit :(
                ##nom=nom_auteur_tweet(tweet.text)
                ##api.update_status_with_media(status=nom, filename="res/"+str(i)+".jpg",in_reply_to_status_id=tweet.id)
            except:
                print("Erreur")
    print("Waitting...")
    threading.Timer(1800, behaviorTwitteraccount).start()

behaviorTwitteraccount()
