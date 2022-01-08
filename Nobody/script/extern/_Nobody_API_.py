#!/bin/python3
#import
from gtts import gTTS
from playsound import playsound
import os
import json
#utils
#def
#say
def say(txt, lang = "conf"):
    if not lang=="conf":
        tts = gTTS(text=txt, lang=lang, slow=False)
    else:
        f = open("config.json", "r")
        conf = json.load(f)
        f.flush()
        f.close()
        tts = gTTS(text=txt, lang=conf["usr"]["lang"], slow=False)
    tts.save("TTS.mp3")
    playsound("TTS.mp3")
    os.remove("TTS.mp3")

def get_conf():
    with open("config.json", "r") as f:
        config = json.load(f)
    return config

def lang():
    conf = get_conf()
    return conf["usr"]["lang"]
