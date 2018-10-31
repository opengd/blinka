# 4-blinka-farger.py
import time
import board
import neopixel

pixel_pin = board.A0 # På vilken pinne sitter pixeln
num_pixels = 1 # Hur många pixlar

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

white = (255, 255, 255) # Vitt
red = (255, 0, 0) # Rött
green = (0, 255, 0) # Grönt
blue = (0, 0, 255) # Blått

def lysa(color):
    pixels.fill(color) # Fyll pixeln med färg
    pixels.show() # Tänd pixeln

# En loop kör saker inom sig medans ett antagande är sant
# Om 1 = 1 eller Namn är samma som Lena
#  
while True: # Loopa medans sant är sant (alltså för alltid)
    lysa(white) # Kör lysa vitt
    time.sleep(0.5) # Sov i en halv sekund
    lysa(red) # Kör slack rött
    time.sleep(0.5) # Sov i en halv sekund
    lysa(green) # Kör lysa grönt
    time.sleep(0.5) # Sov i en halv sekund
    lysa(blue) # Kör lysa rött
    time.sleep(0.5) # Sov i en halv sekund