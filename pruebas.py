import tweepy
import credentials


creds = credentials.credentials(1)
consumer_key = creds[0]
consumer_secret = creds[1]
access_token = creds[2]
access_token_secret = creds[3]
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

info = api.get_user('tricolorbolso96')
print(info)



'''
full_text = 'probando funcionalidad'
tomiID = '286367061'
print('\nSending confirmation question...')
respRapida = 'options'
api.send_direct_message(recipient_id=tomiID, text=full_text, quick_reply_type=respRapida)
print'''