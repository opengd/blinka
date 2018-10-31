# 10-string.py
import time
import board
import neopixel

pixel_pin = board.A0 # På vilken pinne sitter pixeln
num_pixels = 1 # Hur många pixlar

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

lista = ["ellen", "pelle", "lena"] # skapa en lista med tre strängar på tre positioner

def lysa(color):
    pixels.fill(color) # Fyll pixeln med färg
    pixels.show() # Tänd pixeln

raknare = 0
while True:
    namn = lista[raknare]
    if namn == "ellen": # Om namn är samma som ellen
        lysa((255, 0, 0))
    elif namn == "pelle": # Om namn är samma som pelle
        lysa((0, 255, 0))
    else: # Vilket annat namn som helst
        lysa((0, 0, 255))
    
    time.sleep(1)

    raknare += 1
    if raknare == len(lista):
        raknare = 0