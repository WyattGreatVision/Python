#reads a pulse width modulated (PWM) piezo signal
#from an input pin on a Raspberry Pi Pico using the RPi.GPIO library

import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time


# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set the input pin number
input_pin = 18

# Set the output pin numbers for RGB (Red, Green, Blue)
red_pin = 19
green_pin = 20
blue_pin = 21

# Set the PWM frequency
pwm_frequency = 1000

# Configure the output pins as PWM
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

# Create PWM objects for each color
red_pwm = GPIO.PWM(red_pin, pwm_frequency)
green_pwm = GPIO.PWM(green_pin, pwm_frequency)
blue_pwm = GPIO.PWM(blue_pin, pwm_frequency)

# Define frequency ranges for musical notes
note_ranges = {
    'A': (27.5, 55),
    'B': (55, 110),
    'C': (110, 220),
    'D': (220, 440),
    'E': (440, 880),
    'F': (880, 1760),
    'G': (1760, 3520)
}

# Configure the  input pin as INPUT
GPIO.setup(input_pin, GPIO.IN)

def read_pulse_width():
    pulse_widths = []  # List to store pulse widths
    
    while True:
        # Wait for a rising edge on the input pin
        GPIO.wait_for_edge(input_pin, GPIO.RISING)
        
        # Start timing
        start_time = GPIO.input(input_pin)
        
        # Wait for a falling edge on the input pin
        GPIO.wait_for_edge(input_pin, GPIO.FALLING)
        
        # Stop timing and calculate the pulse width
        end_time = GPIO.input(input_pin)
        pulse_width = end_time - start_time
        
        #for music notes
        Nfrequency = 1 / pulse_width
        
        # Classify the note based on frequency
        note = classify_note_frequency(Nfrequency)
        
        # Print the note
        if note:
            print("Detected note:", note)

    
        # Print the pulse width
        print("Pulse width:", pulse_width)
        
        # Append pulse width to the list
        pulse_widths.append(pulse_width)
        
        # Plot the pulse width graph
        plt.plot(pulse_widths)
        plt.xlabel('Time')
        plt.ylabel('Pulse Width')
        plt.title('Pulse Width Signal')
        plt.pause(0.001)
        plt.clf()
        
        
        
def set_rgb_value(rgb_value):
    # Map the PWM value to the range 0-100
    pwm_value = int((rgb_value / 255.0) * 100)
    
    # Set the PWM duty cycle for each color
    red_pwm.ChangeDutyCycle(pwm_value)
    green_pwm.ChangeDutyCycle(pwm_value)
    blue_pwm.ChangeDutyCycle(pwm_value)
    
    
    
def classify_note_frequency(frequency):
    for note, (min_freq, max_freq) in note_ranges.items():
        if min_freq <= frequency < max_freq:
            return note
    
    return None
    
        
try:
    read_pulse_width()
    # Start the PWM signals
    red_pwm.start(0)
    green_pwm.start(0)
    blue_pwm.start(0)
    
    while True:
        # Read the PWM signal and set the RGB value
        pulse_width = input_pin  # Read the pulse width signal from input_pin
        set_rgb_value(pulse_width)
except KeyboardInterrupt:
    # Clean up the GPIO on exit
    red_pwm.stop()
    green_pwm.stop()
    blue_pwm.stop()
    GPIO.cleanup()
    
    
    
"""
Description for plotting PWM signal 

Make sure you have the RPi.GPIO library installed on your Raspberry Pi Pico.
You can install it using the command pip install RPi.GPIO.
In this script, we set the GPIO mode to BCM, define the input pin number as 18,
and configure it as an input pin using GPIO.setup(). The read_pulse_width()
function continuously waits for a rising edge on the input pin, starts timing,
waits for a falling edge, stops timing, and calculates the pulse width.
It then prints the pulse width.To run the script, save it with
a .py extension (e.g., pulse_width_reader.py), navigate to the directory
where the script is saved, and execute the command python pulse_width_reader.py.
The script will continuously read and print the pulse width until you interrupt it with Ctrl+C.
"""

"""
Desription of mapping PWM to RGB color output pins

To map the PWM signal to a value for RGB and control an LED, you can use the RPi.GPIO
library to generate the PWM signal on an output pin connected to the LED. Here's an example
Python script that demonstrates this:


In this script, we first set up the output pins for the RGB LED (red, green, and blue) and define the PWM frequency.
We then configure the pins as PWM outputs using GPIO.setup(). Next, we create PWM objects for each color using GPIO.PWM().

The set_rgb_value() function takes an rgb_value as input, which represents the pulse width signal.
We map the PWM value to the range 0-100 based on the input range (e.g., 0-255), and then set the
PWM duty cycle for each color using the ChangeDutyCycle() method of the PWM objects.

Inside the main loop, you need to read the pulse width signal from the input pin connected
to the piezo signal and assign it to the pulse_width variable. Then, you can call the
set_rgb_value() function with the pulse_width to control the RGB LED.

Make sure you connect the output pins to the corresponding RGB pins of the LED, and the input
pin to the piezo signal input. Adjust the pin numbers and other settings according to your specific setup.

When you run the script, the RGB LED will display colors based on the mapped pulse width signal.
You can modify the color mapping and other aspects to suit your specific requirements.





"""