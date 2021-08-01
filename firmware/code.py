import board
import time
from digitalio import DigitalInOut, Direction
import neopixel
import pulseio
from adafruit_motor import servo

from adafruit_esp32spi import adafruit_esp32spi
from adafruit_esp32spi import adafruit_esp32spi_wifimanager
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
import busio

from adafruit_minimqtt import MQTT

# Get wifi details and more from a secrets.py file
from secrets import secrets

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
PURPLE = (180, 0, 255)
ORANGE = (155, 50, 0)
OFF = (0,0,0)
PINK = (231,84,128)

# Create a Adafruit IO Status light
io_led = neopixel.NeoPixel(board.D7, 1, brightness=0.5, pixel_order=neopixel.RGB)
io_led.fill(OFF)

### WiFi setup ###
esp32_cs = DigitalInOut(board.ESP_CS)
esp32_ready = DigitalInOut(board.ESP_BUSY)
esp32_reset = DigitalInOut(board.ESP_RESET)
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)
status_light = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.2)
wifi = adafruit_esp32spi_wifimanager.ESPSPI_WiFiManager(
    esp, secrets, status_light)

### Servo setup ###

# create a PWMOut object on Pin A2.
pwm1 = pulseio.PWMOut(board.D9, frequency=50)
pwm2 = pulseio.PWMOut(board.D8, frequency=50)

# Create a servo object, my_servo.
my_servo1 = servo.Servo(pwm1)
my_servo2 = servo.Servo(pwm2)
servo_pause = .3

# Initial positions
my_servo1.angle = 90
my_servo2.angle = 0

def move_both():
    my_servo1.angle = 0
    my_servo2.angle = 90
    time.sleep(servo_pause)

    my_servo1.angle = 90
    my_servo2.angle = 0
    time.sleep(servo_pause)

    my_servo1.angle = 0
    my_servo2.angle = 90
    time.sleep(servo_pause)

    my_servo1.angle = 90
    my_servo2.angle = 0
    time.sleep(servo_pause)

def move_left():
    my_servo1.angle = 0
    time.sleep(servo_pause)

    my_servo1.angle = 90
    time.sleep(servo_pause)

    my_servo1.angle = 0
    time.sleep(servo_pause)

    my_servo1.angle = 90
    time.sleep(servo_pause)

def move_right():
    my_servo2.angle = 90
    time.sleep(servo_pause)

    my_servo2.angle = 0
    time.sleep(servo_pause)

    my_servo2.angle = 90
    time.sleep(servo_pause)

    my_servo2.angle = 0
    time.sleep(servo_pause)

def message_received_blink():
    blink_pause = .2
    io_led.fill(PINK)
    time.sleep(blink_pause)
    io_led.fill(PURPLE)
    time.sleep(blink_pause)
    io_led.fill(GREEN)
    time.sleep(blink_pause)
    io_led.fill(PINK)

# Listen to robot-cat feed
robot_cat_feed = secrets['aio_username'] + '/feeds/robot-cat-tweets'

# This method will be called when the client is connected
# successfully to the broker.
def connected(client, userdata, flags, rc):
    print('Connected to Adafruit IO! Listening for topic changes on %s' % robot_cat_feed)
    # Subscribe to all changes on the robot_cat_feed.
    client.subscribe(robot_cat_feed)
    io_led.fill(CYAN)

# This method is called when the client is disconnected
def disconnected(client, userdata, rc):
    print('Disconnected from Adafruit IO!')
    io_led.fill(RED)

# This method is called when a topic the client is subscribed to
# has a new message.
def message(client, topic, message):
    message_received_blink()
    print('New message on topic {0}: {1}'.format(topic, message))

    if "left" in message:
        move_left()
    elif "right" in message:
        move_right()
    else:
        move_both()

    io_led.fill(CYAN)

# Connect to WiFi
wifi.connect()
io_led.fill(YELLOW)

# Set up a MiniMQTT Client
mqtt_client = MQTT(socket,
                   broker='io.adafruit.com',
                   username=secrets['aio_username'],
                   password=secrets['aio_key'],
                   network_manager=wifi)

# Setup the callback methods above
mqtt_client.on_connect = connected
mqtt_client.on_disconnect = disconnected
mqtt_client.on_message = message

# Connect the client to the MQTT broker.
print('Connecting to Adafruit IO...')
mqtt_client.connect()

while True:
    # Poll the message queue once a second
    mqtt_client.loop()
    time.sleep(1)