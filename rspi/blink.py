import socket
import RPi.GPIO as GPIO
import time

def setup_led():
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(8, GPIO.OUT)

def blink_led():
    for _ in range(10):  # Blink 10 times
        GPIO.output(8, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(8, GPIO.LOW)
        time.sleep(5)

def receive_warning(ip_address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip_address, port))
    s.listen(1)
    connection, client_address = s.accept()
    try:
        while True:
            data = connection.recv(16)
            if data:
                print('received {!r}'.format(data))
                if data == b'Warning!':
                    blink_led()
            else:
                break
    finally:
        connection.close()

# Setup the LED and start listening for the warning
setup_led()
receive_warning('0.0.0.0', 8001)  # replace with the Raspberry Pi's IP address and port number