# 8-svep-upp-ner-rgb.py
import time
import board
import neopixel

pixel_pin = board.A1 # På vilken pinne sitter pixeln
num_pixels = 1 # Hur många pixlar

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

def lysa(color):
    pixels.fill(color) # Fyll pixeln med färg
    pixels.show() # Tänd pixeln

r = 0 # r är samma som 0
g = 0 # g är samma som 0
b = 0 # b är samma som 0

color_max = 255 # color_max är samma som 255
color_min = 0 # color_min är samma som 0
go_up = True

color_select = 0

while True: # Loopa medans sant är sant (alltså för alltid)
    current_color = (r, g, b)
    lysa(current_color) # Lys färg

    if go_up == True: # Om go_up är sant addera
        if color_select == 0:
            r += 1
        elif color_select == 1:
            g += 1
        elif color_select == 2:
            b += 1
    else: # Om go_up är falskt subtrahera
        if color_select == 0:
            r -= 1
        elif color_select == 1:
            g -= 1
        elif color_select == 2:
            b -= 1

    if r == color_max and color_select == 0: # Om r är samma som color_max
        go_up = False # Sätt go_up till False
    elif r == color_min and color_select == 0: # Om r är samma som color_min
        go_up = True # Sätt go_up till True
        color_select += 1
    elif g == color_max and color_select == 1: # Om g är samma som color_max
        go_up = False # Sätt go_up till False
    elif g == color_min and color_select == 1: # Om g är samma som color_min
        go_up = True # Sätt go_up till True
        color_select += 1
    elif b == color_max and color_select == 2: # Om b är samma som color_max
        go_up = False # Sätt go_up till False
    elif b == color_min and color_select == 2: # Om b är samma som color_min
        go_up = True # Sätt go_up till True
        color_select = 0