#!/usr/bin/env python2.7
import tweepy, os, json, re
from random import randint
from time import sleep

def beautify(words):
    rgx = re.compile(r'\w')
    i = randint(0, 1)
    res = ''

    for c in words:
        m = re.match(rgx, c)
        if m is not None:
            i += 1
            c = c.upper() if i % 2 == 0 else c.lower()
        res += str(c)

    return res

def run(args):
    if len(args) < 2:
        print("usage: {} <bot name> <handle>".format(__file__))
        exit(1337)

    path = os.path.abspath(__file__)
    scr_name = os.path.basename(__file__)
    with open(path.replace(scr_name, "credentials.json"), 'r') as f:
        creds = json.load(f)

    name = args[0]
    if not creds[name]:
        print("invalid username specified")
        exit(1337)

    auth = tweepy.OAuthHandler(creds[name]["consumer"]["key"], creds[name]["consumer"]["secret"])
    auth.set_access_token(creds[name]["access"]["key"], creds[name]["access"]["secret"])
    api = tweepy.API(auth)
    user = api.get_user(args[1])

    print("Spongebobbing started on {} from {}...".format(user.screen_name, name))
    last_tweet = old_tweet = api.user_timeline(screen_name = user.screen_name, count = 1)[0]
    while(True):
        last_tweet = api.user_timeline(screen_name = user.screen_name, count = 1)[0]
        if old_tweet.text != last_tweet.text:
            old_tweet = last_tweet
            spongebobbed = beautify(last_tweet.text.encode('utf-8'))
            api.update_status('@{} {}'.format(user.screen_name, spongebobbed), last_tweet.id)
            print("Tweeted:\n\'{}\'".format(spongebobbed))
        sleep(10)

if __name__ == "__main__":
    import sys
    run(sys.argv[1:])
