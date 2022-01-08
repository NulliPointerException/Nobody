#!/bin/python3
#import
from gtts import gTTS
from playsound import playsound
import os, json
import speech_recognition as sr
import threading
from array import array
from queue import Queue, Full
from datetime import datetime
import pyaudio
import wave
#utils
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

#get_conf
def get_conf():
    with open("config.json", "r") as f:
        config = json.load(f)
    return config

#get_lang
def get_lang():
    conf = get_conf()
    return conf["usr"]["lang"]

#trigert

def trigert():
    # 110% of the recording code written by Whitespace (https://github.com/Whitespace-code)
    #rec
    TOLERANCE = 1  # seconds
    MAX_TIME = 10  # seconds
    CHUNK_SIZE = 1024
    MIN_VOLUME = 1000
    # if the recording thread can't consume fast enough, the listener will start discarding
    BUF_MAX_SIZE = CHUNK_SIZE * 10

    RATE = 44100
    CHANNEL_COUNT = 2
    BITRATE = 44100
    FORMAT = pyaudio.paInt16

    def save_chunks(chunks):
        wf = wave.open("user_input.wav", 'wb')
        wf.setnchannels(CHANNEL_COUNT)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(chunks))
        wf.close()

    def get_user_input():
        global p
        p = pyaudio.PyAudio()
        stopped = threading.Event()
        q = Queue(maxsize=int(round(BUF_MAX_SIZE / CHUNK_SIZE)))

        record_t = threading.Thread(daemon=True, target=record, args=(stopped, q))
        record_t.start()  # Records and sends microphone data in chunks to other thread
        analyze_t = threading.Thread(target=analyze, args=(stopped, q))
        analyze_t.start()  # Analyzes chunks to determine if chunk should be saved

        try:
            while True:
                if not analyze_t.is_alive():
                    stopped.set()
                    break
        except KeyboardInterrupt:
            stopped.set()

        record_t.join()
        analyze_t.join()

    def analyze(stopped, q):
        chunks = []
        temp_chunks = []
        recording = False
        running = True
        while running:
            if stopped.wait(timeout=0):
                print("stopped")
                running = False
            chunk = q.get()
            vol = max(chunk)

            if vol >= MIN_VOLUME:
                silent_timestamp = datetime.now()
                if not recording:  # Start recording
                    start_time = datetime.now()
                    recording = True
                    [chunks.append(item) for item in temp_chunks]
                    chunks.append(chunk)
                    temp_chunks.clear()
                    print("Detected; Started recording...")
                else:  # Continue Recording
                    print("recording...")
                    chunks.append(chunk)
                    if (datetime.now() - start_time).total_seconds() >= MAX_TIME:
                        save_chunks(chunks)
                        temp_chunks.clear()
                        print("Max time exceeded; stopped recording")
                        running = False
            else:
                if recording:  # If not recording, don't do anything
                    if (datetime.now() - silent_timestamp).total_seconds() >= TOLERANCE:  # Stop recording
                        recording = False
                        save_chunks(chunks)
                        temp_chunks.clear()
                        print("No sound; stopped recording")
                        break
                    else:  # Record until tolerance is met
                        temp_chunks.append(chunk)

    def record(stopped, q):
        stream = p.open(
            format=pyaudio.paInt16,
            channels=CHANNEL_COUNT,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK_SIZE,
        )

        while True:
            if stopped.wait(timeout=0):
                break
            try:
                q.put(array('h', stream.read(CHUNK_SIZE)))
            except Full:
                pass  # discard
    get_user_input()

    print("stop-rec")
    sr
    f_name="user_input.wav"
    se=sr.Recognizer()
    with sr.AudioFile(f_name) as f:
        data = se.record(f)
        text = se.recognize_google(data, language="de-DE", )
        print(text)
        # do
        functions.get_action(text)
        os.remove("user_input.wav")