import credentials
import tweepy


def compareFollows():
    creds = credentials.credentials(1)
    consumer_key = creds[0]
    consumer_secret = creds[1]
    access_token = creds[2]
    access_token_secret = creds[3]
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    arrFriends = api.friends_ids(screen_name ='HayHilos', count=1000)
    arrFollowers = api.followers_ids(screen_name ='HayHilos', count=1000)
    print("\n Users than not follows you: ")
    for follower in arrFriends:
        if follower not in arrFollowers:
            nonFollower = api.get_user(follower)
            print('@'+nonFollower.screen_name)
    print('\n')