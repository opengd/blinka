# 11-morse.py
# https://en.wikipedia.org/wiki/Morse_code
import time
import board
import neopixel

pixel_pin = board.A0 # På vilken pinne sitter pixeln
num_pixels = 1 # Hur många pixlar

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

unit_long = 0.1 # The base time unit

mark_short = unit_long # A short is blink 1 base time unit
mark_long = unit_long * 3 # A long blink is 3 base time units

gap_marks = unit_long # A gap between blinks in a letter is 1 base time unit
gap_letters = unit_long * 3 # A gap between letters is 3 base time units
gap_words = unit_long * 7 # A gap between words is 7 base time units

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

def blink_short(): # Blink the pixel short
    lysa((255, 0, 0))
    time.sleep(mark_short)

def blink_long(): # Blinkt the pixel long
    lysa((0, 255, 0))
    time.sleep(mark_long)

def pause(pause_time): # Pause, turn off the pixel for set of time
    lysa((0, 0, 0))
    time.sleep(pause_time)

while True:
    for letter in message.lower(): # For all letters in the string
        if letter in morse_code: # If the letter exist in the morse code array do
            for mark in morse_code[letter]: # For all * and - as the letter
                if mark == "*": # If the mark is a dot
                    blink_short() # Blinks short
                else: # If the mark is a dash
                    blink_long() # Blinkt long
                pause(gap_marks) # Pause 1 time unit between mark
            # Pause gap letter time unit subtracted by gap mark unit as we did a pause before
            pause(gap_letters-gap_marks)
        else:
            # If the letter do not exist in morse code list 
            # do a word pause minus gap_letters minus gap_marks as when have done thoose pauses before
            pause(gap_words-gap_letters-gap_marks)
    # If there is no more letters do a
    # word pause minus gap_letters minus gap_marks as when have done thoose pauses before
    pause(gap_words-gap_letters-gap_marks)