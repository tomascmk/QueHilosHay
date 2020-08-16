import tweepy, credentials
import time

def follow():
    creds = credentials.credentials(1)
    consumer_key = creds[0]
    consumer_secret = creds[1]
    access_token = creds[2]
    access_token_secret = creds[3]
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    seguidores = []
    seguidos = 0
    nombres = []
    nombres = input("Please insert de screen names: ").strip().split(" ")
    print('')
    for nombre in nombres:
        print('Starting following the users that follows to: ' + nombre)
        user_info = api.get_user(nombre)
        fallos = 0
        try:
            seguidores = api.followers_ids(nombre)
        except:
            user_info = api.get_user(nombre)
            seguidores = api.followers_ids(user_info.id)
        users = []
        for follower in seguidores:
            t = 15
            #print(len(str(follower)))
            if len(str(follower)) == 19:
                try:
                    txt = open("docs/idsF.txt")
                    txtR = txt.read()
                    txt.close()
                    #   print(txtR)
                    if str(follower) not in txtR:
                        txtF = open('./docs/F2F.txt')
                        txtF2F = txtF.read()
                        if txtF2F == 0 or txtF2F == '0':
                            api.create_friendship(follower)
                            usuarioSeguido = api.get_user(follower)
                            print('The user has been followed: @'+ usuarioSeguido.screen_name)
                            fallos = 0
                            txtW = open("docs/idsF.txt", "a")
                            txtW.write(str(follower) + "\n")
                            txtW.close()
                            seguidos += 1
                            t = 15
                        else:
                            user = api.get_user(follower)
                            userInfo = user._json
                            usuarioSeguido = api.get_user(follower)
                            limit = int(txtF2F)
                            flw = int(userInfo['followers_count'])
                            if flw >= limit:
                                api.create_friendship(follower)
                                print('The user has been followed: @' + usuarioSeguido.screen_name)
                                fallos = 0
                                txtW = open("docs/idsF.txt", "a")
                                txtW.write(str(follower) + "\n")
                                txtW.close()
                                seguidos += 1
                                t = 15
                            else:
                                print('User cannot reach the conditions.')
                                t = 5

                        if seguidos == 400:
                            break
                        time.sleep(t)

                except:
                    if fallos >= 3:
                        break
                    print('The user couldn\'t been followed')
                    fallos += 1
                    time.sleep(60)


def setF2F():
    loop = True
    while loop:
        try:
            print('Please insert the followers limit to follow someone new.')
            print('Enter 0 for no limit.')
            limit = int(input('Limit: '))
            txt = open('./docs/F2F.txt', 'wt')
            txt.write(str(limit))
            loop = False
            time.sleep(2)
            print('\nFollowers limit updated succesfully.')
            time.sleep(3)
        except:
            pass