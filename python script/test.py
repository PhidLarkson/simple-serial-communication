# Description: This script is used to test the communication between your local machine and the Arduino.
import serial
import time

def main():
    ser = serial.Serial('/dev/ttyACM0', 9600)  # Change '/dev/ttyACM0' to your Arduino's port
    time.sleep(2)  # Wait for the Arduino to initialize

    while True:
        character = input("Enter your character: ")
        if character == 'q':
            ser.close()
            break
        else:
            ser.write(character.encode())
            time.sleep(0.5)
            while ser.in_waiting:
                print(ser.readline().decode().strip())

if __name__ == "__main__":
    main()