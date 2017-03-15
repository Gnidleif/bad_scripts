#!/usr/bin/env python2.7
import tweepy, json, os, re

def run(args):
    if type(args) is not list or len(args) < 3:
        print("usage: {} <bot name> <text> <reply>".format(__file__))
        exit(1337)

    path = os.path.abspath(__file__)
    scr_name = os.path.basename(__file__)
    with open(path.replace(scr_name, "credentials.json"), 'r') as f:
        creds = json.load(f)
    
    name = args[0]
    if not creds[name]:
        print("Invalid username specified")
        exit(1337)

    auth = tweepy.OAuthHandler(creds[name]["consumer"]["key"], creds[name]["consumer"]["secret"])
    auth.set_access_token(creds[name]["access"]["key"], creds[name]["access"]["secret"])
    api = tweepy.API(auth)

    split = str(args[1]).split(' ')
    status_id = None
    reply_id = int(args[2])
    try:
        reply_status = api.get_status(reply_id)
        if reply_status.id == reply_id:
            status_id = reply_status.id
    except:
        args[2] = "-1"

    count = 1
    buf = []
    for i in range(len(split)):
        buf.append(split[i])
        if i < len(split) - 1 and len(' '.join(buf) + ' ' + split[i+1]) > 140:
            try:
                tweet = ' '.join(buf)
                status = api.update_status(tweet) if status_id is None else api.update_status(tweet, status_id)
                status_id = status.id
                count += 1
                buf = []

            except tweepy.error.TweepError:
                buf = []

    tweet = ' '.join(buf)
    status = api.update_status(tweet) if status_id is None else api.update_status(tweet, status_id)
    status_id = status.id
    url = "https://www.twitter.com/" + creds[name]["handle"] + "/status/" + str(status_id)
    print(str(count) + " tweet(s) sent. URL: " + url)

if __name__ == "__main__":
    import sys
    run(sys.argv[1:])
