import serial
import time

arduino = serial.Serial(port = 'COM3', baudrate = 115200, timeout = .1)
maxOLEDCharacters = 21

def write_read(communication):
    arduino.write(bytes(communication, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

if __name__ == "__main__":
    while True:
        quote = input("What would you like the screen to say? ") # Taking input from user
        value = str(write_read(quote))
        print(value) # printing the value
