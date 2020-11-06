# Write your code here :-)

import board
import time
import digitalio
led = digitalio.DigitalInOut(board.A1)
led.direction = digitalio.Direction.OUTPUT
while True:

    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)