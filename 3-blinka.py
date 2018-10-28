# 3-blinka.py
import time
import board
import neopixel

pixel_pin = board.A1 # På vilken pinne sitter pixeln
num_pixels = 1 # Hur många pixlar

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

color = (255, 255, 255) # Vitt ljus
black = (0, 0, 0) # Svart färg, ingen färg

def lysa():
    pixels.fill(color) # Fyll pixeln med färg
    pixels.show() # Tänd pixeln

def slack():
    pixels.fill(black) # Fyll pixeln med svart färg
    pixels.show() # Tänd pixeln med färgen

while True: # Loopa medans sant är sant (alltså för alltid)
    lysa() # Kör lysa
    time.sleep(0.5) # Sov i en halv sekund
    slack() # Kör slack
    time.sleep(0.5) # Sov i en halv sekund