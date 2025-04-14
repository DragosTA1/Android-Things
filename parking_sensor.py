from gpiozero import DistanceSensor, LED
from time import sleep
import signal # To catch Ctrl+C gracefully

# Define GPIO pin numbers (using BCM numbering)
# Ordered from closest range LED (index 0) to farthest (index 3)
# We map LED index 0 (closest) to GPIO 25, index 3 (farthest) to GPIO 22
LED_PINS = [25, 24, 23, 22]

TRIG_PIN = 17
ECHO_PIN = 27

# Define distance thresholds in centimeters
THRESH_10_CM = 10.0
THRESH_15_CM = 15.0
THRESH_30_CM = 30.0
THRESH_50_CM = 50.0

# Set up devices using gpiozero
sensor = DistanceSensor(echo=ECHO_PIN, trigger=TRIG_PIN)
# Create a list of LED objects corresponding to the pins
leds = [LED(pin) for pin in LED_PINS]

# Helper function to control the LEDs
def set_leds(num_on):
    """Turns on the first 'num_on' LEDs and turns off the rest."""
    for i, led in enumerate(leds):
        if i < num_on:
            # Turn on LEDs representing closer ranges
            led.on()
        else:
            # Turn off LEDs representing farther ranges
            led.off()

print("Waiting for sensor to settle...")
sleep(2) # Allow sensor to settle

print("Starting measurements...")
print("Ranges (cm): <=10 (4 LEDs), <=15 (3 LEDs), <=30 (2 LEDs), <=50 (1 LED)")

try:
    while True:
        # Get distance in meters and convert to cm
        dist_m = sensor.distance
        dist_cm = dist_m * 100

        print(f"Measured Distance = {dist_cm:.2f} cm")

        # Determine how many LEDs to light up
        if dist_cm <= THRESH_10_CM:
            num_leds_to_light = 4
            print("Status: <= 10 cm")
        elif dist_cm <= THRESH_15_CM:
            num_leds_to_light = 3
            print("Status: >10 cm and <= 15 cm")
        elif dist_cm <= THRESH_30_CM:
            num_leds_to_light = 2
            print("Status: >15 cm and <= 30 cm")
        elif dist_cm <= THRESH_50_CM:
            num_leds_to_light = 1
            print("Status: >30 cm and <= 50 cm")
        else:
            num_leds_to_light = 0
            print("Status: > 50 cm")

        # Set the LEDs based on the distance
        set_leds(num_leds_to_light)

        sleep(0.2) # Wait a short time between measurements (adjust as needed)

except KeyboardInterrupt:
    print("\nMeasurement stopped by User")

finally:
    print("Cleaning up...")
    # Turn off all LEDs on exit
    set_leds(0)
    # Close sensor resources
    sensor.close()
    # Close LED resources (optional for basic LEDs but good practice)
    for led in leds:
        led.close()
    print("GPIO cleanup done.")