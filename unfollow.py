import tweepy, credentials
from progress.bar import IncrementalBar, ChargingBar
import os, time, random


def unfollow():
    creds = credentials.credentials(2)
    consumer_key = creds[0]
    consumer_secret = creds[1]
    access_token = creds[2]
    access_token_secret = creds[3]
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    seguidores = []

    seguidores = api.followers_ids('HayHilos')
    bar1 = IncrementalBar('Processing:', max=len(seguidores))
    for follower in seguidores:
        try:
            api.destroy_friendship(follower)
            usuarioSeguido = api.get_user(follower)
            bar1.next()
            #print('User is no longer being followed: @' + usuarioSeguido.screen_name)
            time.sleep(3)

        except:
            print('\nThe user couldn\'t been unfollowed')
            time.sleep(60)
    bar1.finish()


def unfollowNon():
    creds = credentials.credentials(2)
    consumer_key = creds[0]
    consumer_secret = creds[1]
    access_token = creds[2]
    access_token_secret = creds[3]
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    arrFriends = api.friends_ids(screen_name='HayHilos')
    arrFollowers = api.followers_ids(screen_name='HayHilos')
    print("Unfollow process started...\n")
    contador = 0
    arrFr = len(arrFriends)
    arrFo = len(arrFollowers)
    diferencia = int(arrFr)-int(arrFo)
    bar1 = ChargingBar('Processing:', max=diferencia)
    try:
        for follower in arrFriends:
            if follower not in arrFollowers:
                api.destroy_friendship(follower)
                time.sleep(3)
                contador += 1
                bar1.next()
                if contador >= 50:
                    contador = 0
                    time.sleep(180)
        bar1.finish()
        print('\nProcess completed successfully.')
    except tweepy.RateLimitError:
        print('\nAn error ocurred.')
        time.sleep(15 * 60)

    print('\n')