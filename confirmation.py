import time
from datetime import date
import credentials
import tweepy


def confirmar(full_textPlus, full_text):
    '''
    condicion = 'No'
    intentos = 0
    tomiID = '286367061'
    while intentos <= 4:
        try:
            creds = credentials.credentials(1)
            consumer_key = creds[0]
            consumer_secret = creds[1]
            access_token = creds[2]
            access_token_secret = creds[3]
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            api = tweepy.API(auth)
            print('\nSending confirmation question... ', time.strftime("%X"))
            respRapida = 'options'
            try:
                api.send_direct_message(recipient_id=tomiID, text=full_textPlus, quick_reply_type=respRapida)
            except:
                api.send_direct_message(recipient_id=tomiID, text=full_text, quick_reply_type=respRapida)
            intentos = 10
            condicion = 'Si'
            #print(intentos)
            time.sleep(1200)
            break
        except:
            print('\nSending confirmation question FAILED... ',time.strftime("%X"))
            time.sleep(300)
            intentos += 1
            if intentos >= 3:
                print("\nTwitt: "+ full_text +"\n")
                print('La confirmacion ha fallado, por favor ingrese "Si" para retwittear, o ingrese "No" para no retwittear.\n')
                respuesta = input("Ingrese su decision: ")
                resp = respuesta.lower()
                if resp == "si":
                    condicion = 'Si'
                elif resp == "no":
                    condicion = "No"'''
    condicion = 'Si'
    return condicion


def esperarConfirmacion():
    '''
    global respuesta
    confirmacionRecibida = True
    creds = credentials.credentials(1)
    consumer_key = creds[0]
    consumer_secret = creds[1]
    access_token = creds[2]
    access_token_secret = creds[3]
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    print('\nAwaiting confirmation...')
    time.sleep(300)
    while confirmacionRecibida:
        lastMsg = api.list_direct_messages(6)
        respuesta = lastMsg[0]
        respuesta = str(respuesta.message_create)
        empieza = respuesta.find('text')
        termina = respuesta.find('entities')
        respuestaReal = respuesta[empieza:termina]
        if 'Si quiero Boti.' in respuestaReal:
            print("\nAffirmative answer.")
            respuesta = 'Si'
            confirmacionRecibida = False
        elif 'No quiero Boti.' in respuestaReal:
            print('\nNegative answer.')
            respuesta = 'No'
            confirmacionRecibida = False
        else:
            time.sleep(1200)
    return respuesta
    '''
    return "Si"
