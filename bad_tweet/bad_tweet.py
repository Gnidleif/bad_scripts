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

    count = 1
    msg = str(args[1])
    buf = []
    for c in msg:
        buf.append(c)
        if len(buf) == 100:
            try:
                api.update_status(handle + ' ' + ''.join(buf))
                count += 1
                buf = []
            except tweepy.error.TweepError:
                buf = []
                continue

    api.update_status(handle + ' ' + ''.join(buf))
    print(str(count) + " tweet(s) sent to " + handle)

if __name__ == "__main__":
    import sys
    run(sys.argv[1:])
