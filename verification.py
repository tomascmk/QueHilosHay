import tweepy, credentials
import time

autentications = ['First', 'Second', 'Third', 'Fourth', 'Fifth']


def verify():
    cont = 1
    while cont <= 2:
        try:
            creds = credentials.credentials(cont)
            consumer_key = creds[0]
            consumer_secret = creds[1]
            access_token = creds[2]
            access_token_secret = creds[3]
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            api = tweepy.API(auth)
            cont += 1
            api.verify_credentials()
            print('\n'+autentications[cont - 2] + " authentication OK.")
            time.sleep(2)
        except:
            print("\nError during authentication. \n")
            time.sleep(2)
