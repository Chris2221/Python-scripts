import socket

# Target IP address
target_ip = '149.56.41.48'

# Set a range of ports to check
start_port = 1
end_port = 1024

# Loop through the range of ports and check if they are open
for port in range(start_port, end_port+1):
    # Create a TCP socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set a timeout of 1 second for the connection attempt
    sock.settimeout(1)
    
    try:
        # Connect to the target IP and port
        result = sock.connect_ex((target_ip, port))
        
        # Check if the connection was successful
        if result == 0:
            print(f"Port {port} is open on {target_ip}")
    except:
        pass
    
    # Close the socket connection
    sock.close()
