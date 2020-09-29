import time


def credentials(type):
    txt = open("docs/credentials.txt")
    txtR = txt.read()
    txt.close()
    creds = txtR.split('\n')
    if type == 1:
        # compare.py / currentStatus.py / follow.py / verification.py / confirmation.py
        credsR = creds[1:5]
    elif type == 2:
        # tweet.py / unfollow.py / verification.py
        credsR = creds[6:10]
    else:
        print('Auth type not supported')
        time.sleep(5)
        return []
    return credsR


def setCredentials():
    txt = open("docs/credentials.txt")
    txtR = txt.read()
    txt.close()
    creds = txtR.split('\n')
    creds1 = creds[1]
    creds2 = creds[6]
    credTittles = ['API key', 'API secret key', 'Access token', 'Access token secret']
    credential = txtR.split('Cred:')
    credential1 = credential[1]
    credential2 = credential[2]
    print('Please insert wich credential you want to update.')
    print('1- ' + '*' * 21 + creds1[-4:])
    print('2- ' + '*' * 21 + creds2[-4:])
    loop = True
    while loop:
        choice = input('Cred: ')
        if choice == '1':
            print('Cred to update: ' + '*' * 21 + creds1[-4:])
            arrCred = credential1.split('\n')
            arrCred = arrCred[1:-1]
            #print(arrCred)
            tCont = 0
            print('Please enter the new value, if you want to keep the same value please insert "0"')
            for arr in arrCred:
                value = input(credTittles[tCont] + ': ')
                if value != '0':
                    arrCred[tCont] = value
                elif value == '0':
                    arrCred[tCont] = arr
                tCont += 1
            stringDB = 'Cred:' + credential2
            arrDB = ''
            for arr in arrCred:
                arrDB = arrDB + arr + '\n'
            stringDB = 'Cred:\n' + arrDB + stringDB
            print(stringDB)
            txt = open("docs/credentials.txt", 'wt')
            txt.write(stringDB)
            txt.close()
            loop = False
        elif choice == '2':
            print('Cred to update: ' + '*' * 21 + creds2[-4:])
            arrCred = credential2.split('\n')
            arrCred = arrCred[1:]
            tCont = 0
            print('Please enter the new value, if you want to keep the same value please insert "0"')
            for arr in arrCred:
                value = input(credTittles[tCont] + ': ')
                if value != '0':
                    arrCred[tCont] = value
                elif value == '0':
                    arrCred[tCont] = arr
                tCont += 1
            stringDB = 'Cred:' + credential1 + 'Cred:\n'
            for arr in arrCred:
                stringDB = stringDB + arr + '\n'
            print(stringDB)
            print(stringDB[:-1])
            txt = open("docs/credentials.txt", 'wt')
            txt.write(stringDB[:-1])
            txt.close()
            loop = False
        else:
            print('Invalid option')
