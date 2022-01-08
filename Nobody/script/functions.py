# import
from datetime import datetime
import API, json, os
from os import listdir
from os.path import isfile, join
#start
def get_action(input):
    input=input.lower()
    # init
    # time
    for i in ["time", "zeit", "uhr", "spät"]:
        if i in input:
            time()
    # interestet
    for i in ["interestet", "interessiert"]:
        if i in input:
            interested()
    # extern
    # get extern.json
    f = open("extern/extern.json", "r")
    extern = json.load(f)
    f.flush()
    f.close()
    # get all add on names
    files = [f for f in listdir("extern/") if isfile(join("extern/", f))]
    files.remove("_Nobody_API_.py")
    files.remove("extern.json")
    for f in files:
        triger = extern["extern"][f].split()
        for t in triger:
            if t in input:
                os.system("python3 extern/" + f)
                break

# functions
# time
def time():
    now = datetime.now()
    API.say(now.strftime("%H:%M"))

# interestet
def interested():
    conf = API.get_conf()
    if conf["usr"]["lang"]=="de":
        API.say("das interesiert niemand")
    else:
        API.say("nobody is interestet")