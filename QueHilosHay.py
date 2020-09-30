import follow, unfollow, confirmation, tweet, compare, verification, currentStatus, credentials
import os
import time
import tweepy

clear = lambda: os.system('cls')  # on Windows System
account = 'HayHilos'
loop = True

while loop:
    clear()
    print('#' * 37)
    print('# WELCOME TO "BTS BOTI" THE TWITTER APP #')
    print('#'*37)
    print("\nEnter '1' to retweet threats.")
    print("Enter '2' to follow functions.") #someone's followers.")
    print("Enter '3' to unfollow functions.")
    print("Enter '4' to see your non-followers.")
    print("Enter '5' to verify your credentials.")
    print("Enter '6' to view the current status of your account.")
    print("Enter '7' to compare followers to anyone.")
    print("Enter '8' to end this program.", '\n')
    action = input("Action: ")
    print('')

    if action == '1':
        tweet.tweet()

    elif action == '2':
        print("\nEnter '1' to follow someone's followers.")
        print("Enter '2' to define followers limit to follow someone new.")
        action = input("\nAction: ")
        if action == '1':
            follow.follow()
        if action == '2':
            follow.setF2F()

    elif action == '3':
        print("\nEnter '1' to unfollow all the followings.")
        print("Enter '2' to unfollow all non-followers.")
        action = input("\nAction: ")
        if action == '1':
            unfollow.unfollow()
        elif action == '2':
            unfollow.unfollowNon()

    elif action == '4':
        compare.compareOwnFollows()

    elif action == '5':
        print("\nEnter '1' to verify your credential's status.")
        print("Enter '2' to update your credentials.")
        action = input("\nAction: ")
        if action == '1':
            verification.verify()
        if action == '2':
            credentials.setCredentials()

    elif action == '6':
        currentStatus.status(account)

    elif action == '7':
        user = input("\nPlease enter the screen name of the user you want to compare: ")
        compare.compareFollowers(user)

    elif action == '8':
        print('\n', 'Finishing program....')
        time.sleep(2)
        loop = False

    else:
        print('')
        print('Sorry it isn\'t a valid option')
        time.sleep(2)
        clear()
