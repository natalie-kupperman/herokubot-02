# Dependencies
import tweepy
import time
import os


# Twitter API Keys
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")


# Twitter credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    
# Quotes to Tweet
quote_list = ["We Will Do What Is Hard. We Will Achieve What Is Great. This Is A Time For American Heroes And We Reach For The Stars. — President Bartlet",
              "I'm The Press Secretary, Boo-Boo. I Don't Have That Kind Of Time. — C.J. Cregg",
              "He Doesn't [Call Us The Batman And Robin Of Speech-Writing], But He Should, 
              'Cause Thats What We Are. — Toby Zeigler",
              "Never Doubt That A Small Group Of Thoughtful Committed Citizens Can Change The World. — President Bartlet",
              "I Have Wit, I Have Charm, I Have Brains, I Have Legs That Go All The Way Down To The Floor, My Friend. — Amy Gardener",
              "Some [Schoolchildren] Don't... Raise Their Hand 'Cause They Think They're Going To Be Wrong. I Think You Should Say To These Kids, 'You Think You Get It Wrong Sometimes, You Should Come... See How The Big Boys Do It. — C.J. Cregg"
              ]


# Create function for tweeting
def quote_it_up():

    # Tweet the next quote
    api.update_status(quote)

    # Print success message
    print("Tweeted successfully")


# Create a loop that tweets one quote per minute until
# all of the quotes have been tweeted
for quote in quote_list:
    quote_it_up()
    time.sleep(60)
