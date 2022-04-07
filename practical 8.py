import tweepy 
from tkinter import * 
from time import sleep
from datetime import datetime
from textblob import TextBlob 
import matplotlib.pyplot as plt 

consumer_key = 'AU8Ym4iZoM3deqTn3i6AWDRme' 
consumer_secret = 'h1aT9QPHdtWvjLbPx57di9hnspYFnFT34eG6kTylbC5Tv2C0Nm'
access_token = '700594962556014592-9NIgRPd60o4YySxlrgQda4uzO97iozW'
access_token_secret = 'rPaSPPgEWQZpVS0zVjePj8dhlvkBmvbHZQ0FvswEYygXh'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#user = api.me()   # Works on tweeter version below 4.0
user= api.verify_credentials()
#print (user.name)
#GUI
root = Tk()

label1 = Label(root, text="Search")
E1 = Entry(root, bd =5)

label2 = Label(root, text="Sample Size")
E2 = Entry(root, bd =5)

def getE1():
    return E1.get()

def getE2():
    return E2.get()

def getData():
    getE1()
    keyword = getE1()

    getE2()
    numberOfTweets = getE2()
    numberOfTweets = int(numberOfTweets)

    #Where the tweets are stored to be plotted
    polarity_list = []
    numbers_list = []
    number = 1

    positive=0
    negative=0
    neutral=0
    
    #for tweet in tweepy.Cursor(api.search, keyword, lang="en").items(numberOfTweets):   #Works on tweeter version below 4.0
    for tweet in tweepy.Cursor(api.search_tweets, keyword, lang="en").items(numberOfTweets):
        try:
            analysis = TextBlob(tweet.text)
            analysis = analysis.sentiment
            polarity = analysis.polarity
            if polarity>0:
                positive+=1
            elif polarity <0:
                negative+=1
            else:
                neutral+=1
            polarity_list.append(polarity)
            numbers_list.append(number)
            number = number + 1

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break

    print(polarity)
    print(numbers_list)
    print(polarity_list)
    print(f'Amount of positive tweets : {positive}')
    print(f'Amount of negative tweets : {negative}')
    print(f'Amount of neutral tweets : {neutral}')
    
    #Plotting
    axes = plt.gca()
    axes.set_ylim([-1, 1])

    plt.scatter(numbers_list, polarity_list)

    averagePolarity = (sum(polarity_list))/(len(polarity_list))
    averagePolarity = "{0:.0f}%".format(averagePolarity * 100)
    time  = datetime.now().strftime("At: %H:%M\nOn: %m-%d-%y")

    plt.text(1, 0.92, "Average Sentiment:  " + str(averagePolarity) + "\n" + time, fontsize=12,
             bbox = dict(facecolor='none', edgecolor='black', boxstyle='square, pad = 1'))

    plt.title("Sentiment of " + keyword + " on Twitter")
    plt.xlabel("Number of Tweets")
    plt.ylabel("Sentiment")
    plt.show()

submit = Button(root, text ="Submit", command = getData)

label1.pack()
E1.pack()
label2.pack()
E2.pack()
submit.pack(side =BOTTOM)

root.mainloop()
