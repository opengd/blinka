# 11-morse.py
import time
import board
import neopixel

pixel_pin = board.A1 # På vilken pinne sitter pixeln
num_pixels = 1 # Hur många pixlar

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

unit_long = 0.1

mark_short = unit_long
mark_long = unit_long * 3

gap_marks = unit_long
gap_letters = unit_long * 3
gap_words = unit_long * 7

message = "Hello World" # Message to send as morse code

# Morse code "*" = short, "-" = long
morse_code = {"a": "*-",
"b": "-***",
"c": "-*-*",
"d": "-**",
"e": "*",
"f": "**-*",
"g": "--*",
"h": "****",
"i": "**",
"j": "*---",
"k": "-*-",
"l": "*-**",
"m": "--",
"n": "-*",
"o": "---",
"p": "*--*",
"q": "--*-",
"r": "-*-",
"s": "***",
"t": "-",
"u": "**-",
"v": "***-",
"w": "*--",
"x": "-**-",
"y": "-*--",
"z": "--**",
"1": "*----",
"2": "**---",
"3": "***--",
"4": "****-",
"5": "*****",
"6": "-****",
"7": "--***",
"8": "---**",
"9": "----*",
"0": "-----",
}

def lysa(color):
    pixels.fill(color) # Fyll pixeln med färg
    pixels.show() # Tänd pixeln

def blink_short():
    lysa((255, 0, 0))
    time.sleep(mark_short)

def blink_long():
    lysa((0, 255, 0))
    time.sleep(mark_long)

def pause(pause_time):
    lysa((0, 0, 0))
    time.sleep(pause_time)

while True:
    for letter in message.lower():
        if letter in morse_code:
            for mark in morse_code[letter]:
                if mark == "*":
                    blink_short()
                else:
                    blink_long()
                pause(gap_marks)
            pause(gap_letters-gap_marks)
        else:
            pause(gap_words-gap_letters-gap_marks)
    pause(gap_words-gap_letters-gap_marks)