from machine import Pin
from time import sleep_us, sleep

# Define STEP and DIR pins
step_pin = Pin(15, Pin.OUT)
dir_pin = Pin(32, Pin.OUT)
enable_pin = Pin(14, Pin.OUT)

# Enable motor driver
enable_pin.value(0)		# LOW = enabled

def step_movement(steps, direction=1, delay_us=350):
    # direction=1 results in clockwise rotation
    dir_pin.value(direction)
    for _ in range(steps):
        step_pin.on()
        sleep_us(delay_us)
        step_pin.off()
        sleep_us(delay_us)
        
# Stepper Motor control
while True:
    print("Forward")
    step_movement(1600, direction=1)
    sleep(1)
    print("Reverse")
    step_movement(1600, direction=0)
    sleep(1)