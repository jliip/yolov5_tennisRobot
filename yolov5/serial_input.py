import serial
import time

from serial import Serial

ser_input: Serial | Serial = serial.Serial(
    port='COM7',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)


def read_data(ser_input):
    if ser_input.in_waiting > 0:
        data = ser_input.readline().decode('utf-8').strip()
        print("Received data:", data)
    else:
        print("No data received.")


try:
    while True:
        read_data(ser_input)
        time.sleep(1)
except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    ser_input.close()