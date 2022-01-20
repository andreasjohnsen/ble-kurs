import time
import board
import random
from digitalio import DigitalInOut, Direction, Pull

import morse

UNIT_DURATION = 0.3

led = DigitalInOut(board.LED2_G)
led.direction = Direction.OUTPUT

hello = morse.english_to_morse("HALLO VERDEN")
print(hello) 

led.value = True 

for char in hello:
    if char == " ":
        print(" letterspace ")
        time.sleep(3*UNIT_DURATION)
    elif char == ".":
        print(" . ")        
        led.value = False
        time.sleep(1*UNIT_DURATION)
        led.value = True
        time.sleep(1*UNIT_DURATION)
    elif char == "-":
        print(" - ")
        led.value = False    
        time.sleep(3*UNIT_DURATION)
        led.value = True
        time.sleep(1*UNIT_DURATION)
    elif char == "_":
        print(" letterspace ")
        time.sleep(7*UNIT_DURATION)
    else:
        print( "ERROR ")
        # not valid, just ignore
        pass

while True:
    led.value = False
    time.sleep(0.1)
    led.value = True
    # print((random.randint(0, 100), random.randint(-100, 0), random.randint(-50, 50))) # to demonstrate Plotter in mu-editor
    time.sleep(0.5)
