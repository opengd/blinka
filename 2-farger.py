# 2-farger.py
import board
import neopixel

pixel_pin = board.A1 # På vilken pinne sitter pixeln
num_pixels = 1 # Hur många pixlar

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

white = (255, 255, 255) # Vitt
red = (255, 0, 0) # Rött
green = (0, 255, 0) # Grönt
blue = (0, 0, 255) # Blått
black = (0, 0, 0) # Svart

def lysa(color):
    pixels.fill(color) # Fyll pixeln med färg
    pixels.show() # Tänd pixeln

lysa(white) # Kör lysa med vit färg
#lysa(red) # Kör lysa med röd färg
#lysa(green) # Kör lysa med grön färg
#lysa(blue) # Kör lysa med blå färg
#lysa(black) # Kör lysa med svart färg