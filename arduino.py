# USEFUL (Mac) COMMANDS TO RUN

# ls /dev/*  <-- Finds the port of the arduino (it's likely to change between cycles of plugging it into computer)
from robot import *
import pyfirmata
import time

def move(direction):
    return None

def rotate(direction):
    return None

def get_gyroscope_value():
    return None

if __name__ == '__main__':
    # Initiate communication with Arduino
    board = pyfirmata.Arduino('ENTER PORT')
    print("Communication Successfully started")
    
    # Start iterator to receive input data
    it = pyfirmata.util.Iterator(board)
    it.start()