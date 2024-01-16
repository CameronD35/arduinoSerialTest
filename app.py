import serial
import time


ser = serial.Serial('COM3', 9600, timeout=1)

print("Reading data from serial port...")
time.sleep(2)
ser.reset_input_buffer()

for i in range (0, 7):
    line = ser.readline()
    print(line)
    time.sleep(0.5)

print("Exit")