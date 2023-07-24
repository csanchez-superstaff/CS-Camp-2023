import RPi.GPIO as GPIO
from RPLCD import CharLCD

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

lcd = CharLCD(cols = 16, rows = 2, pin_rs = 37, pin_e = 35, pins_data = [], numbering_mode = GPIO.BOARD)