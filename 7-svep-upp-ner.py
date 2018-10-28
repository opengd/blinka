# 7-svep-upp-ner.py
import time
import board
import neopixel

pixel_pin = board.A1 # På vilken pinne sitter pixeln
num_pixels = 1 # Hur många pixlar

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

def lysa(color):
    pixels.fill(color) # Fyll pixeln med färg
    pixels.show() # Tänd pixeln

number = 0 # number är samma som 0

color = 0 # red är samma som 0
color_max = 255 # color_max är samma som 255
color_min = 0 # color_min är samma som 0
go_up = True

while True: # Loopa medans sant är sant (alltså för alltid)
    current_color = (color, color, color)
    lysa(current_color) # Lys färg

    if go_up == True: # Om go_up är sant addera
        color = color + 1 
    else: # Om go_up är falskt subtrahera
        color = color - 1

    if color == color_max: # Om color är samma som color_max
        go_up = False # Sätt go_up till False
    elif color == color_min: # Om color är samma som color_min
        go_up = True # Sätt go_up till True