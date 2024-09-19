from helpers import Text, Picture
import serial
import time

arduinoPort: str = "COM3"
arduinoBaudRate: int = 1_000_000
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
        # unneeded = input("Press enter to send picture")
        # value = str(write_read(Picture("C:\\Users\\potat\\Desktop\\Old\\Chris Cutout small.png").convert_to_bitmap))
        # print(value)

        # bitmap = Picture("C:\\Users\\potat\\Desktop\\Old\\Chris Cutout small.png").convert_to_bitmap
        # arduino.write(bitmap)
        # time.sleep(3)
        # data = arduino.readline()
        # for i in bitmap:
        #     print(i)
        # arduino.flush()

        quote = Text(input("What text would you like to send to the screen? "))
        for line in quote.word_wrap:
            value = str(write_read(line))
            print(value)
