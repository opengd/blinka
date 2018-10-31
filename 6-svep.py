# 6-svep.py
import time
import board
import neopixel

pixel_pin = board.A0 # På vilken pinne sitter pixeln
num_pixels = 1 # Hur många pixlar

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

def lysa(color):
    pixels.fill(color) # Fyll pixeln med färg
    pixels.show() # Tänd pixeln

color = 0 # color är samma som 0
color_max = 255 # color_max är samma som 255
color_min = 0 # color_min är samma som 0

while True: # Loopa medans sant är sant (alltså för alltid)
    current_color = (color, color, color)
    lysa(current_color) # Lys färg
    if(color == color_max):
       color = color_min
    color = color + 1 # Addera 1 till color