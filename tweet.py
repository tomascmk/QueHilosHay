import tweepy, time, controller, confirmation, credentials
from datetime import date


def tweet():
    creds = credentials.credentials(2)
    consumer_key = creds[0]
    consumer_secret = creds[1]
    access_token = creds[2]
    access_token_secret = creds[3]

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    print("Boti esta iniciando")
    queries = ["Abro Hilo", "Abro hilo", "abro hilo"]
    mensajes = [
        'Hola! Los invitamos a pasarse por nuestro perfil para estar al tanto de todos los hilos que son tendencia y ayudarnos con un follow! #QueHilosHay #AbroHilo #HilosDeTwitter']

    msj = ['Nuevo hilo! #QueHilosHay #AbroHilo #HilosDeTwitter',
           'Habemus hilo nuevo! #QueHilosHay #AbroHilo #HilosDeTwitter',
           'Ya viste este hilo? #QueHilosHay #AbroHilo #HilosDeTwitter',
           'Te traemos un nuevo hilo #QueHilosHay #AbroHilo #HilosDeTwitter',
           'Otro hilo más! #QueHilosHay #AbroHilo #HilosDeTwitter',
           'Dejo este hilo por aca... #QueHilosHay #AbroHilo #HilosDeTwitter']

    tweets_per_query = 300
    loop = True
    ownTweet = 0
    notRetweeted = 0
    minimo = [50000, 6000, 10000]
    crasheos = 0
    num = 0
    fechaTweet = False
    confirmado = ''
    resp = ''
    nacChecked = ''
    textChecked = ''
    while loop:
        try:
            for monto in minimo:
                # print('Searching tweets with more than '+ minimo[monto] +' retweets')
                print("Volvi a empezar.")
                new_tweets = 0
                for querry in queries:
                    if ownTweet >= 2:
                        time.sleep(240)
                        ownTweet = 0
                    if notRetweeted >= 20:
                        time.sleep(180)
                        notRetweeted = 0
                    print("")
                    print("#" * 39)
                    print("#    Starting new query: " + querry + "    #")
                    print("#" * 39)
                    print("")
                    for tweet in tweepy.Cursor(api.search, q=querry, tweet_mode="extended").items(tweets_per_query):
                        user = tweet.user.screen_name
                        id = tweet.id
                        # print(tweet)
                        retweets = tweet.retweet_count
                        url = 'https://twitter.com/' + user + '/status/' + str(id)
                        try:
                            text = tweet.retweeted_status.full_text.lower()
                        except:
                            text = tweet.full_text.lower()
                        if "Abro Hilo" in text or "Abro hilo" in text or "abro hilo" in text:
                            txtt = open("docs/idsRT.txt")
                            txt = txtt.read()
                            try:
                                rtStatus = tweet.retweeted_status.id_str
                            except:
                                rtStatus = tweet.id_str
                            txtt.close()
                            print(url)
                            # print('retweets: '+retweets)
                            nacionalidad = ''
                            todayMonth = date.today().month
                            try:
                                tweetMonth = tweet.retweeted_status.created_at.month
                            except:
                                tweetMonth = tweet.created_at.month
                            if todayMonth == tweetMonth or todayMonth == tweetMonth - 1:
                                fechaTweet = True
                            if 'RT' in tweet.full_text and retweets >= 1500 and fechaTweet:
                                nacionalidad = tweet.user._json['location']
                                nacChecked = controller.checkNation(nacionalidad, 'Nation')
                            try:
                                print("Retweets: " + retweets)
                            except:
                                print(retweets)
                            try:
                                if nacionalidad != '':
                                    print('Location: ' + nacionalidad)
                                else:
                                    print('Location: Undefined')
                            except:
                                print('Location: Undefined')
                            retwittear = True
                            # textChecked = controller.checkNation(tweet.full_text, 'Text')
                            if tweet.id_str in txt or rtStatus in txt or retweets < 1500 or nacChecked:
                                retwittear = False
                            else:
                                try:
                                    try:
                                        textChecked = controller.checkNation(tweet.full_text, 'Text')
                                        if textChecked:
                                            retwittear = False
                                    except:
                                        nacionalidadUser = tweet.retweeted_status.user._json['location']
                                        textChecked = controller.checkNation(nacionalidadUser, 'Text')
                                        if textChecked:
                                            retwittear = False
                                except:
                                    pass
                            if retwittear:
                                if 'RT' in tweet.full_text:
                                    textRtFv = tweet.retweeted_status.full_text + '\nRts: ', str(tweet.retweeted_status.retweet_count) + '\nFavs: ', str(tweet.retweeted_status.favorite_count)
                                    resp = confirmation.confirmar(textRtFv, tweet.retweeted_status.full_text)
                                else:
                                    textRtFv = tweet.full_text + '\nRts: ' + str(tweet.retweet_count) + '\nFavs: ' + str(tweet.favorite_count)
                                    resp = confirmation.confirmar(textRtFv, tweet.full_text)
                                if resp == 'Si':
                                    confirmado = confirmation.esperarConfirmacion()
                                if confirmado == 'Si':
                                    txt = open("docs/idsRT.txt", "a")
                                    try:
                                        miUrl = url
                                        if num > 5:
                                            num = 0
                                        twit = msj[num]
                                        num += 1
                                        api.update_status(status=twit, in_reply_to_status_id=tweet.id_str,
                                                          attachment_url=miUrl)
                                        print("\n\t √ Retweeted")
                                        print("")
                                        new_tweets += 1
                                        ownTweet += 1
                                        try:
                                            if "RT" in tweet.full_text:
                                                idSaved = tweet.retweeted_status.id_str
                                                txt.write(idSaved + "\n")
                                                txt.close()
                                            else:
                                                idSaved = tweet.id_str
                                                txt.write(idSaved + "\n")
                                                txt.close()
                                        except:
                                            pass
                                        try:
                                            pass
                                            replyTo = tweet.retweeted_status.user.screen_name
                                            reply = "@" + replyTo + " Hola, los invitamos a pasar por nuestro perfil para estar al tanto de todos los hilos que son tendencia y ayudarnos con un follow! #QueHilosHay #AbroHilo #HilosDeTwitter"
                                            api.update_status(reply, tweet.retweeted_status.id_str)
                                        except:
                                            pass
                                        time.sleep(1400)
                                    except tweepy.TweepError as e:
                                        # miUrl = url
                                        # api.update_status('Síguenos para enterarte de los mejores hilos de twitter!! #QueHilosHay #AbroHilo', str(id), attach_url=miUrl)

                                        print('\n\t ! Not Retweeted')
                                        print("")
                                        notRetweeted += 1
                                        txt.close()
                                elif confirmado == 'No':
                                    txt = open("docs/idsRT.txt", "a")
                                    if "RT" in tweet.full_text:
                                        idSaved = tweet.retweeted_status.id_str
                                        txt.write(idSaved + "\n")
                                        txt.close()
                                    else:
                                        idSaved = tweet.id_str
                                        txt.write(idSaved + "\n")
                                        txt.close()
                            else:
                                print('\n\t ! Not Retweeted')
                                print("")
                                txt = open("docs/idsRT.txt", "a")
                                if "RT" in tweet.full_text:
                                    idSaved = tweet.retweeted_status.id_str
                                    txt.write(idSaved + "\n")
                                    txt.close()
                                else:
                                    idSaved = tweet.id_str
                                    txt.write(idSaved + "\n")
                                    txt.close()
            print("New Tweets: " + str(new_tweets))
        except:
            crasheos += 1
            print("#" * 60)
            print("#" * 60)
            print("#" * 60)
            print("\t Crasheo el programa, reconectando...")
            print("#" * 60)
            print("#" * 60)
            print("#" * 60)
            time.sleep(100)
            if crasheos >= 2:
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                print("Reiniciando el servicio...\n")
                print(time.strftime("%X"))
                time.sleep(1000)
                crasheos = 0
