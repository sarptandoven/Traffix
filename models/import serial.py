
"""Send randomized LED durations to an Arduino over serial.

This helper is interactive and is not used by the YOLO inference pipeline.
"""

import random
import time

import serial

def get_serial_port():
    ports = [] # serial.tools.listports.comports()
    portsList = [str(one) for one in ports]

    for one in ports:
        print(str(one))

    com = input("Select COM Port for Arduino #: ")

    for port in portsList:
        if port.startswith("COM" + str(com)):
            return "COM" + str(com)

    # print("Port not found.")
    return "/dev/cu.usbmodem2101"

def send_led_duration_to_arduino(serialInst):
    # Generate random duration for each LED in seconds
    red_duration = random.randint(1, 10)
    green_duration = random.randint(1, 10)
    blue_duration = random.randint(1, 10)

    print(f"Red LED: {red_duration} seconds")
    print(f"Green LED: {green_duration} seconds")
    print(f"Blue LED: {blue_duration} seconds")

    # Send the duration to Arduino as "R3\n", "G4\n", "B5\n" for example
    serialInst.write(f"R{red_duration}\n".encode('utf-8'))
    time.sleep(5)  # Small delay between messages

    serialInst.write(f"G{green_duration}\n".encode('utf-8'))
    time.sleep(5)

    serialInst.write(f"B{blue_duration}\n".encode('utf-8'))
    time.sleep(5)

def main():
    port = get_serial_port()
    if port is None:
        return

    serialInst = serial.Serial()
    serialInst.baudrate = 9600
    serialInst.port = port
    serialInst.timeout = 2  # Timeout to handle slow responses
    serialInst.open()

    while True:
        send_led_duration_to_arduino(serialInst)
        # Wait for Arduino to process and finish before sending new data
        while True:
            if serialInst.in_waiting > 0:
                response = serialInst.readline().decode('utf-8').strip()
                if response == "DONE":
                    break
            time.sleep(0.1)

if __name__ == "__main__":
    main()
    ##