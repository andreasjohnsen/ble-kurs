import time
import board
import random
from digitalio import DigitalInOut, Direction, Pull

led = DigitalInOut(board.LED2_R)
led.direction = Direction.OUTPUT

while True:
    led.value = False
    time.sleep(0.1)
    led.value = True
    # print((random.randint(0, 100), random.randint(-100, 0), random.randint(-50, 50)))
    time.sleep(0.5)