import board
import time
from digitalio import DigitalInOut, Direction

import pulseio
from adafruit_motor import servo

from adafruit_esp32spi import adafruit_esp32spi_wifimanager
from adafruit_esp32spi import adafruit_esp32spi
import busio
from secrets import secrets

from adafruit_esp32spi import adafruit_esp32spi_socket as socket
from adafruit_minimqtt import adafruit_minimqtt as mqtt
import neopixel

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
PURPLE = (180, 0, 255)
ORANGE = (155, 50, 0)
OFF = (0,0,0)
PINK = (231,84,128)

io_led = neopixel.NeoPixel(board.D7, 1, brightness=0.5, pixel_order=neopixel.RGB)
io_led.fill(OFF)

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

def connected(client, userdata, flags, rc):
    print("connected!")
    robot_cat_topic = secrets["aio_username"] + "/feeds/robot-cat-topic"
    client.subscribe(robot_cat_topic)
    io_led.fill(CYAN)
    
def disconnected(client, userdata, rc):
    print("disconnected :(")
    io_led.fill(RED)
    
def message(client, topic, message):
    print("message: %s", message)
    io_led.fill(PINK)
    
    if "left" in message:
        move_left()
    elif "right" in message:
        move_right()
    else:
        move_both()
    
    io_led.fill(CYAN)

wifi.connect()

mqtt.set_socket(socket, esp)
mqtt_client = mqtt.MQTT(broker="io.adafruit.com",
                        username = secrets["aio_username"],
                        password = secrets["aio_key"])

mqtt_client.on_connect = connected
mqtt_client.on_disconnect = disconnected
mqtt_client.on_message = message 

mqtt_client.connect()

while True:
    mqtt_client.loop()
    time.sleep(1)