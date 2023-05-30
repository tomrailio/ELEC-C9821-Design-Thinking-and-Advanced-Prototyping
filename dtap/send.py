import socket

def send_warning(ip_address, port):
    warning_on = True   # Set this to true when a warning needs to be sent
    if warning_on:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_address, port))
        s.sendall(b'Warning!')
        s.close()

#send_warning('10.100.42.109', 8001)