import time
import os
import urllib.request
import json
from aip import AipSpeech
import speech_recognition as sr
import urllib3

# Baidu Speech API，填写自己的ID与KEY
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 录音
def rec(rate=16000):
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=rate) as source:
        print("please say something")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    with open("recording.wav", "wb") as f:
        f.write(audio.get_wav_data())


# 百度语音转文字
def listen(pid1):
    with open('recording.wav', 'rb') as f:
        audio_data = f.read()

    result = client.asr(audio_data, 'wav', 16000, {
        'dev_pid': pid1,
    })

    text_input = result["result"][0]

    print("我说: " + text_input)


pid = 0
language = input('选择你的语言：1.普通话 2.英语 3.粤语 4. 四川话 5.远距离普通话 \n')
if language == '1':
    pid = 1536
elif language == '2':
    pid = 1737
elif language == '3':
    pid = 1637
elif language == '4':
    pid = 1837
elif language == '5':
    pid = 1936
else:
    print("请按照规定输入！")

while True:
    rec()
    listen(pid)
