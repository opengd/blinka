# 1-lysa.py
import board
import neopixel

pixel_pin = board.A0 # På vilken pinne sitter pixeln
num_pixels = 1 # Hur många pixlar

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

color = (255, 255, 255) # Vitt ljus

def lysa():
    pixels.fill(color) # Fyll pixeln med färg
    pixels.show() # Tänd pixeln

lysa() # Kör lysa