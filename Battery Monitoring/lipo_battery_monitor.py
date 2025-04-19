# Script is called lipo_battery_monitor.py

# Library imports
from machine import ADC, Pin, Timer
from time import sleep

# Pin definitions
battery_monitor_gpio = Pin(35)

# ADC and attenuation for battery monitoring
# https://docs.espressif.com/projects/esp-idf/en/v4.4/esp32/api-reference/peripherals/adc.html 
batt_monitor = ADC(battery_monitor_gpio)

# Set attenuation for full voltage range (ATTN_11DB), converter uses range of 0V to 3.3V
batt_monitor.atten(ADC.ATTN_11DB)

''' - - - - - Callback Functions - - - - - '''
def read_battery_voltage(timer):
    raw_value = batt_monitor.read()
    voltage = (raw_value / 4095) * 3.3 * 2  # Adjust scaling based on voltage divider
    print(f"Battery Voltage: {voltage} V")

# Timers for Timer Callbacks
batt_timer = Timer(0)

# period is how often the callback is called (ex: period = 500 is 500 ms)
batt_timer.init(period=1000, mode=batt_timer.PERIODIC, callback=read_battery_voltage)

# sleep() takes inputs in seconds
sleep(30)

batt_timer.deinit()
