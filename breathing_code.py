import time
import board
import pwmio

from math import sqrt

pwm = pwmio.PWMOut(board.LED2_B)

# Fritt etter https://makersportal.com/blog/2020/3/27/simple-breathing-led-in-arduino

smoothness = 600
while True:
    for i in range(smoothness):
        value = 65535 * sqrt(1 - pow(abs((2*(i/smoothness))-1),2))
        pwm.duty_cycle = int(value)
        time.sleep(0.004)
