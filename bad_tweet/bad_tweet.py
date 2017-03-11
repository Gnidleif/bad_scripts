#!/usr/bin/env python2.7
import tweepy, json, os, re

def run(args):
    if type(args) is not list or len(args) < 2:
        print("usage: {} <handle> <text>".format(__file__))
        exit(1337)

    path = os.path.abspath(__file__)
    scr_name = os.path.basename(__file__)
    with open(path.replace(scr_name, "credentials.json"), 'r') as f:
        creds = json.load(f)
    
    auth = tweepy.OAuthHandler(creds["consumer"]["key"], creds["consumer"]["secret"])
    auth.set_access_token(creds["access"]["key"], creds["access"]["secret"])
    api = tweepy.API(auth)

    rgx = re.compile(r'^@')
    handle = str(args[0])
    if re.search(rgx, handle) is None:
        print("Handle needs to start with @")
        exit(1337)

    url = None
    status_id = None
    count = 1
    msg = str(args[1])
    buf = []
    for c in msg:
        buf.append(c)
        if len(buf) == 110:
            try:
                status = None
                tweet = handle + ' ' + ''.join(buf)
                if status_id is None:
                    status = api.update_status(tweet)
                else:
                    status = api.update_status(tweet, status_id)
                status_id = status.id

                count += 1
                buf = []
            except tweepy.error.TweepError:
                buf = []
                continue

    tweet = handle + ' ' + ''.join(buf)
    if status_id is None:
        api.update_status(tweet)
    else:
        status = api.update_status(tweet, status_id)
    status_id = status.id

    url = "https://www.twitter.com/" + creds["name"] + "/status/" + str(status_id)
    print(str(count) + " tweet(s) sent to " + handle + ". Find it here: " + url)

if __name__ == "__main__":
    import sys
    run(sys.argv[1:])
