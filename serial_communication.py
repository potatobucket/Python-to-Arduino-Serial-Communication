import serial
import time

arduino = serial.Serial(port = 'COM3', baudrate = 115200, timeout = .1) 

def write_read(x): 
    arduino.write(bytes(x, 'utf-8')) 
    time.sleep(0.05) 
    data = arduino.readline() 
    return data 

if __name__ == "__main__":
    while True: 
        quote = input("When is the winter of our discontent and by whom was it made glorious? ") # Taking input from user 
        value = str(write_read(quote))
        print(value) # printing the value 
