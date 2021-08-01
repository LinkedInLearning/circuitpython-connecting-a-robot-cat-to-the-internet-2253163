import board
import time
from digitalio import DigitalInOut, Direction

import pulseio
from adafruit_motor import servo

from adafruit_esp32spi import adafruit_esp32spi_wifimanager
from adafruit_esp32spi import adafruit_esp32spi
import busio
from secrets import secrets

cs = DigitalInOut(board.ESP_CS)
busy = DigitalInOut(board.ESP_BUSY)
reset = DigitalInOut(board.ESP_RESET)
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, cs, busy, reset)
wifi = adafruit_esp32spi_wifimanager.ESPSPI_WiFiManager(esp, secrets)

pwm1 = pulseio.PWMOut(board.D8, frequency=50)
pwm2 = pulseio.PWMOut(board.D9, frequency=50)

servo1 = servo.Servo(pwm1)
servo2 = servo.Servo(pwm2)
servo_pause = 0.5

def move_both():
    servo1.angle = 90
    servo2.angle = 0
    time.sleep(servo_pause)
    
    servo1.angle = 0
    servo2.angle = 90
    time.sleep(servo_pause)
    
    servo1.angle = 90
    servo2.angle = 0
    time.sleep(servo_pause)
    
    servo1.angle = 0
    servo2.angle = 90
    time.sleep(servo_pause)
    
def move_left():
    servo1.angle = 90
    time.sleep(servo_pause)
    
    servo1.angle = 0
    time.sleep(servo_pause)
    
    servo1.angle = 90
    time.sleep(servo_pause)
    
    servo1.angle = 0
    time.sleep(servo_pause)
    
def move_right():
    servo2.angle = 0
    time.sleep(servo_pause)
    
    servo2.angle = 90
    time.sleep(servo_pause)
    
    servo2.angle = 0
    time.sleep(servo_pause)
    
    servo2.angle = 90
    time.sleep(servo_pause)

wifi.connect()
move_both()
