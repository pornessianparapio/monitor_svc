import socket
import os
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
    finally:
        s.close()
    return ip_address

def get_username():
    username = os.getlogin()
    print(username)

    return username

if __name__ == "__main__":
    print(get_ip_address())
    print(get_username())