#-- TODO: fix word wrap so that words larger than max screen size work correctly when placed in a sentence

import helpers
import serial
import time

arduino = serial.Serial(port = 'COM3', baudrate = 115200, timeout = .1)

def write_read(communication):
    """Handles reading and writing to the Arduino over serial communication."""
    arduino.write(bytes(communication, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

if __name__ == "__main__":
    while True:
        quote = helpers.Text(input("What text would you like to send to the screen? ")) # Taking input from user
        value = str(write_read(quote))
        print(value) # printing the value
