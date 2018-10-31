# 5-om.py
import time
import board
import neopixel

pixel_pin = board.A0 # På vilken pinne sitter pixeln
num_pixels = 1 # Hur många pixlar

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

red = (255, 0, 0) # Rött
blue = (0, 0, 255) # Blått
black = (0, 0, 0) # Svart

def lysa(color):
    pixels.fill(color) # Fyll pixeln med färg
    pixels.show() # Tänd pixeln

number = 0 # number är samma som 0

while True: # Loopa medans sant är sant (alltså för alltid)
    lysa(red) # Lys röd
    number = number + 1 # Addera 1 på number
    time.sleep(0.5) # Sov i en halv sekund
    lysa(black) # lys svart
    time.sleep(0.5) # Sov i en halv sekund
    if number == 5:
        lysa(blue) # Lys blå
        number = 0 # Sätt number åter till 0
        time.sleep(0.5) # Sov i en halv sekund
        lysa(black)
        time.sleep(0.5) # Sov i en halv sekund