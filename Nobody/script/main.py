#!/bin/python3
#import

from API import *
from functions import *
#def
#start
#load config
conf=get_conf()
#if first start
if not conf["nobody"]["set-up"]:
    say("hi my name is Nobody and you haven't set me up yet.", "en")
    say("whats your name?", "en")
    #xxxx
    conf["usr"]["name"] = input(": ")
    say("what is your favorite language", "en")
    #xxxx
    conf["usr"]["lang"] = input(": ")
    conf["nobody"]["set-up"]=True
    say("set up completed.", "en")
    f = open("config.json", "w+")
    f.write(json.dumps(conf))
    f.flush()
    f.close()
    print("set-up completed")
#do
trigert()
