from machine import Pin, PWM
import time

# Pin initialization for the FS90 Servo Motor's Signal Line with PWM
# Set servo signal line to GPIO pin 32
servo_pin = Pin(32)
# Setting the frequency to 50Hz, which is standard for most servo motors
servo_pwm = PWM(servo_pin, freq=50)


# Function to set servo position based on microsecond input
def set_servo_duty(pwm_object, pulse_micro_sec):
    # Using a 10-bit resolution for the PWM signal from the ESP32 Feather V2
    max_duty = 1023
    min_duty = 0
    
    period = 1 / 50
    period_micro_sec = int(period * (1000000))
    
    duty_output = int((pulse_micro_sec / period_micro_sec) * max_duty)
    
    pwm_object.duty(duty_output)
    

# Example usage:
# I recommend attaching one of the servo horns to see these affects

# Setting servo to minimum position for 2 seconds
pwm_signal = 900
print("Setting PWM signal to {} micro-seconds".format(pwm_signal))
set_servo_duty(servo_pwm, pwm_signal)
time.sleep(2) 

# Setting servo to middle position for 2 seconds
pwm_signal = 1500
print("Setting PWM signal to {} micro-seconds".format(pwm_signal))
set_servo_duty(servo_pwm, pwm_signal)
time.sleep(2)

# Setting servo to maximum position for 2 seconds
pwm_signal = 2100
print("Setting PWM signal to {} micro-seconds".format(pwm_signal))
set_servo_duty(servo_pwm, pwm_signal)
time.sleep(2) 

# Deinitialize the PWM when done
servo_pwm.deinit()
print("Servo PWM signal is deinitialized")