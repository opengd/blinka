# 9-array.py
import board
import neopixel

pixel_pin = board.A0 # På vilken pinne sitter pixeln
num_pixels = 1 # Hur många pixlar

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

lista = [0, 0, 0] # skapa en lista med 3 värden på tre positioner

i_max = 256 # max färg värde

def lysa(color):
    pixels.fill(color) # Fyll pixeln med färg
    pixels.show() # Tänd pixeln

while True:
    for i in range(len(lista)): # loop på antalet positioner i arrayen
        for j in range(i_max): # loopa mellan 0 och 255
            lista[i] = j # låt position i i listan vara j
            color = (lista[0], lista[1], lista[2]) # sätt color till de nuvarande värdena i listan
            lysa(color) # tänd pixeln med färgen