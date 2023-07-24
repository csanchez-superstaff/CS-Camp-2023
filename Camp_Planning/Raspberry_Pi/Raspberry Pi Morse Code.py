import RPi.GPIO as GPIO
from time import sleep

morseCode = {   'A':'.-', 'B':'-...',
'C':'-.-.', 'D':'-..', 'E':'.',
'F':'..-.', 'G':'--.', 'H':'....',
'I':'..', 'J':'.---', 'K':'-.-',
'L':'.-..', 'M':'--', 'N':'-.',
'O':'---', 'P':'.--.', 'Q':'--.-',
'R':'.-.', 'S':'...', 'T':'-',
'U':'..-', 'V':'...-', 'W':'.--',
'X':'-..-', 'Y':'-.--', 'Z':'--..',
'1':'.----', '2':'..---', '3':'...--',
'4':'....-', '5':'.....', '6':'-....',
'7':'--...', '8':'---..', '9':'----.',
'0':'-----', ', ':'--..--', '.':'.-.-.-',
'?':'..--..', '/':'-..-.', '-':'-....-',
'(':'-.--.', ')':'-.--.-'}

# separation
# letters = 3 dots
# words = 7 dots

def encrypt(message):
    cipher = ""
    for letter in message:
        if letter != " ":
            cipher += morseCode[letter.upper()]
        else:
            cipher += " / "
    return cipher

m = "sos send food"
encrypted = encrypt(m)
print(encrypted)

GPIO.setmode(G)

for letter in encrypted:
    if letter == '.':
        GPIO.output(4,GPIO.HIGH)
        sleep(0.5)
        GPIO.output(4,GPIO.LOW)
        sleep(0.5)
    if letter == '-':
        GPIO.output(4,GPIO.HIGH)
        sleep(1.5)
        GPIO.output(4,GPIO.LOW)
        sleep(0.5)
    if letter == " ":
        GPIO.output(4,GPIO.LOW)
        sleep(2)