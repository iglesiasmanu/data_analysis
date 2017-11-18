import json
from tweepy import OAuthHandler, Stream, API
from tweepy.streaming import StreamListener


consumer_key = "0qFf4T2xPWVIycLmAwk3rDQ55"
consumer_secret = "LcHpujASn4fIIrQ8sikbCTQ3oyU6T6opchFVWBBqwICahzSE64"
access_token = "4271002872-XLo7TNnE3qvYevqLmT1RBuiJ5CJ3o0DCr3WReAT"
acces_token_secret = "ulZ3dA25zuC6BGJgaFowCSTIm6gKVtOa4x9y7tO0IUDIx"

auth = OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token, acces_token_secret)
class PrintListener(StreamListener):
    def on_status(self,status):
        if not status.text[:3] == "RT ":
            print(status.text)
            print(status.author.screen_name, status.created_at, status.source, "\n")

    def on_error(self, status_code):
        print("Error code: {}".format(status_code))
        return True #keep stream alive

    def on_timeour(self):
        print("Listener time out!")
        return True #keep stream alive


def print_to_terminal():
    listener = PrintListener()
    stream = Stream(auth, listener)
    languages = ("en",)
    stream.sample(languages = languages)

if __name__ == "__main__":
    print_to_terminal()

#def pull_down_tweets(screen_name):
#    api = API(auth)
#    tweets = api.user_timeline(screen_name = screen_name, count = 200)
#    for tweet in tweets:
#        print(json.dumps(tweet._json, indent = 4))

#if __name__ == "__main__":
#pull_down_tweets(auth.username)
