#!/bin/python3
# import
import nobody
from do import *
# start
# load config
conf=nobody.get_conf()
# First start
if not conf["nobody"]["set-up"]:
    nobody.say("hi my name is Nobody and you haven't set me up yet.", "en")
    nobody.say("whats your name?", "en")
    # xxxx
    conf["usr"]["name"] = input(": ")
    nobody.say("what is your favorite language", "en")
    # xxxx
    conf["usr"]["lang"] = input(": ")
    conf["nobody"]["set-up"]=True
    nobody.say("set up completed.", "en")
    f = open("config.json", "w+")
    f.write(json.dumps(conf))
    f.flush()
    f.close()
    print("set-up completed")
# do
print("bootet")
nobody.input_processing()