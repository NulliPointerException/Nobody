# import
from datetime import datetime
import nobody, json, os, time
from os import listdir
from os.path import isfile, join
#def
def contains(input_, list_):
    return True in ((word in list_) for word in input_.split(" "))

#start
def get_action(usr_input):
    print("get action")
    try:
        usr_input=usr_input.lower()
        # init
        # time
        if contains(usr_input, ["zeit", "uhr", "time", "clock", "spät"]):
            time()
        #timer
        if contains(usr_input, ["timer", "stop uhr"]):
            timer()
        # Hello
        if contains(usr_input, ["hi", "hallo", "hello"]):
            if contains(usr_input, ["geht's"]):
                nobody.say("mihr geht es guht danke der nachfrage")
            else:
                lan = nobody.get_lang()
                if str(lan)=="de":
                    nobody.say("hallo")
                else:
                    nobody.say("hello")

        # extern
        # get extern.json
        f = open("extern/extern.json", "r")
        extern = json.load(f)
        f.flush()
        f.close()
        # get all add on names
        files = [f for f in listdir("extern/") if isfile(join("extern/", f))]
        #files.remove("_Nobody_API_.py")
        files.remove("extern.json")
        for f in files:
            triger = extern["extern"][f].split()
            for t in triger:
                if t in usr_input:
                    os.system("python3 extern/" + f)
                    break
    except:
        nobody.say("sorry")

# functions
# time
def time():
    now = datetime.now()
    nobody.say(now.strftime("%H:%M"))

def timer():
    nobody.say("wie fiele minuten?")
    input("lol")
    user_input=nobody.stt()
    import re
    now=datetime.now()
    M=now.strftime("%M")
    wait=int(M+(int(re.search(r'\d+', user_input).group())))
    time.sleep(int(re.search(r'\d+', user_input).group()))
