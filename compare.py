import credentials
import tweepy


def compareOwnFollows():
    creds = credentials.credentials(1)
    consumer_key = creds[0]
    consumer_secret = creds[1]
    access_token = creds[2]
    access_token_secret = creds[3]
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    arrFriends = api.friends_ids(screen_name ='HayHilos')
    arrFollowers = api.followers_ids(screen_name ='HayHilos')
    print("\n Users than not follows you: ")
    for follower in arrFriends:
        if follower not in arrFollowers:
            nonFollower = api.get_user(follower)
            print('@'+nonFollower.screen_name)
    print('\n')

def compareFollowers(user):
    creds = credentials.credentials(1)
    consumer_key = creds[0]
    consumer_secret = creds[1]
    access_token = creds[2]
    access_token_secret = creds[3]
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    arrFw = api.followers_ids(screen_name ='HayHilos')
    arrOtherFw = api.followers_ids(screen_name =user)
    totalArr = len(arrOtherFw)
    for follower in arrFw:
        if follower in arrOtherFw:
            arrOtherFw.pop()
    
    perCnt = (len(arrOtherFw)*100)/totalArr
    
    print('For @', user , ' followers:\n\nThe ',100-perCnt,'% are following you (',totalArr-len(arrOtherFw),' followers),\nThe ',perCnt,'% are not following you (',len(arrOtherFw),' followers).')
    enter = input('\n\nPress enter to go back to menu.')
