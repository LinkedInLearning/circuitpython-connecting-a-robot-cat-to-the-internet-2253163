import board
import time
from digitalio import DigitalInOut, Direction

led = DigitalInOut(board.D11)
led.direction = Direction.OUTPUT 

while True:
    print("blink!")
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)
