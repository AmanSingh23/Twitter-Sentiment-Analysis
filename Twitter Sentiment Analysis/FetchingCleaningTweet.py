# importing the module
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import re

count=0
# personal details
consumer_key ="CoZxs4vEku2p4sYr1RZDqGc54"
consumer_secret ="JFIBgAwX6oQJvFsxX8NS93P9lqPgtbYVDeGh6xJ1jfKvgwcRgn"
access_token ="969230411128647680-I1hPeU3J7jk8MNapGEftKt2Z9mG3I60"
access_token_secret ="tWo8U9XwEfZBly0pM2xGRTbHkInVVdTsbugFYTGCQzO2h"

#cleaning of emojis
def handle_emojis(tweet):
    # Smile -- :), : ), :-), (:, ( :, (-:, :')
    tweet = re.sub(r'(:\s?\)|:-\)|\(\s?:|\(-:|:\'\))', ' ', tweet)
    # Laugh -- :D, : D, :-D, xD, x-D, XD, X-D
    tweet = re.sub(r'(:\s?D|:-D|x-?D|X-?D)', ' ', tweet)
    # Love -- <3, :*
    tweet = re.sub(r'(<3|:\*)', ' ', tweet)
    # Wink -- ;-), ;), ;-D, ;D, (;,  (-;
    tweet = re.sub(r'(;-?\)|;-?D|\(-?;)', ' ', tweet)
    # Sad -- :-(, : (, :(, ):, )-:
    tweet = re.sub(r'(:\s?\(|:-\(|\)\s?:|\)-:)', ' ', tweet)
    # Cry -- :,(, :'(, :"(
    tweet = re.sub(r'(:,\(|:\'\(|:"\()', ' ', tweet)
    return tweet

#cleaning the tweet
def processTweet2(tweet):
    # process the tweets
    #Convert to lower case
    tweet = tweet.lower()
    tweet = re.sub(r'\s?[0-9]+\.?[0-9]*','',tweet)
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','',tweet)
     #cleaning emojis function
    tweet = handle_emojis(tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
                       #remove rt
    tweet = re.sub("rt|RT",'', tweet) # remove Retweet
    
    #trim
    tweet = tweet.strip('\'"')
    tweet = re.sub('[^a-zA-Z0-9 \n\.]', '', tweet)
   
    
    
    return tweet    
 
class listener(StreamListener):
    def on_status(self,status):
        if hasattr(status,'retweeted_status'):
            try:
                tweet=status.retweeted_status.extended_tweet["full_text"]
            except:
                tweet = status.retweeted_status.text
        else:
            try:
                tweet = status.extended_tweet["full_text"]
            except AttributeError:
                tweet = status.text
        x=processTweet2(tweet)
        if n==0:
            print("SORRY NO TWEET EXTRACTED\nNUMBER OF TWEETS SHOULD BE GREATER THAN 0 !!!\n ")
            return False
        print(x)        
        savefile = open('C:\\Users\\Ritesh\\Desktop\\txt\\tweet_extracted.txt', 'a',encoding='utf-8')        
        savefile.write(x+'\n')
        savefile.close()
        global count
        count=count+1        
        if count==n:
           return False
        else :
            return True

    def on_error(self, status):
        print(status)

#connecting with Twitter API
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
savefile1 = open('C:\\Users\\Ritesh\\Desktop\\txt\\tweet_extracted.txt', 'w',encoding='utf-8')
savefile1.close()
twitterStream = Stream(auth, listener(count))
n=int(input("ENTER THE NUMBER OF TWEET\n"))
twitterStream.filter(track=[input("ENTER THE KEYWORD\n")],languages=['en'])