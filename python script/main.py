# a simple function to send a command to the arduino
# it sends a character via the serial port
# we need to import the serial module to communicate with the arduino
import serial
from .config import *            # import the variables from the config file
import time

# a list of characters that the arduino can understand
open_char = CHARACTERS

# open the serial port
port = serial.Serial(PORT, BAUD, TIMEOUT)
time.sleep(1)
print('Port opened')

# a function to send a command to the arduino
def send(character):
    if character in open_char:
        port.write(character.encode())
    else:
        print('Invalid')
try:
    while port:
        character = input('Enter a character: ')
        send(character)
        if character == 'X':
            break

except KeyboardInterrupt | Exception:
    print('Keyboard Interrupt or Exception')
    port.close()
    print('Port closed')

# close the serial port
port.close()

# run the script
if __name__ == '__main__':
    pass