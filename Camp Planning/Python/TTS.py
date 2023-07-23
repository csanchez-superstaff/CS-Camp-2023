# pip install pyttsx3
import pyttsx3

tts = pyttsx3.init()

answer = input()

while answer != "END":
    tts.say(answer)
    tts.runAndWait()
    answer = input()