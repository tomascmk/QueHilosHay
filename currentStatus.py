import tweepy, credentials
import time


def status(account):
    creds = credentials.credentials(1)
    consumer_key = creds[0]
    consumer_secret = creds[1]
    access_token = creds[2]
    access_token_secret = creds[3]
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    user = api.get_user(account)
    userInfo = user._json
    print('User: ', userInfo['name'])
    print('')
    print('Description: "', userInfo['description'], '"')
    print('')
    print('Number of tweets: ', userInfo['statuses_count'])
    print('')
    followers = int(userInfo['followers_count'])
    friends = int(userInfo['friends_count'])
    nonFollowers = friends - followers
    if nonFollowers < 0:
        nonFollowers = 'You have not non followers'
    print('Followers: ', followers, "\nFollowing: ", friends, '\nFollow-Friends count: ', nonFollowers, '\n')
    enter = input('\n\nPress enter to go back to menu.')
