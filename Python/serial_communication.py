from helpers import Text
import serial
import time

arduinoPort: str = "COM3"
arduinoBaudRate: int = 1000000
serialTimeOut: float = 0.1

arduino = serial.Serial(port = arduinoPort, baudrate = arduinoBaudRate, timeout = serialTimeOut)

def write_read(communication):
    """Handles reading and writing to the Arduino over serial communication."""
    arduino.write(bytes(communication, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

if __name__ == "__main__":
    while True:
        quote = Text(input("What text would you like to send to the screen? "))
        for line in quote.word_wrap:
            value = str(write_read(line))
            print(value)
