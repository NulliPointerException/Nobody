#!/bin/python3
# import
import nobody
from do import *
import set_up
# start
# First start
conf = nobody.get_conf()
if not conf["nobody"]["set-up"]:
    conf = nobody.get_conf()
    print("whats your name?")
    conf["usr"]["name"] = input(": ")
    print("what is your favorite language?")
    conf["usr"]["lang"] = input(": ")
    print("what is your path of the script folder?")
    # path
    with open("extern/path.json", "r") as f2:
        c = json.load(f2)
    p = input(": ")
    conf["nobody"]["path"] = p
    c["path"] = p
    # save
    conf["nobody"]["set-up"] = True
    f2 = open("extern/path.json", "w+")
    f2.write(json.dumps(c))
    f2.flush()
    f2.close()
    f = open("config.json", "w+")
    f.write(json.dumps(conf))
    f.flush()
    f.close()
    print("set-up completed")
# do
nobody.input_processing()