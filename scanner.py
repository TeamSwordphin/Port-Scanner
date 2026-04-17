import sys # Comes with python so we can use CLI arguments. Src: https://docs.python.org/3/library/sys.html#sys.argv 
import datetime # Also comes with python, provides information about dates and times. Src: https://docs.python.org/3/library/datetime.html
import socket # Creates a socket https://docs.python.org/3/howto/sockets.html

# Create a list so we can keep track of which ports were opened
ports_opened = []
target_ip = sys.argv[1]

# Using f-string to format the starting output message, as indicated by boot.dev being much better than concatenation.
output_message = f"""
---------------------------------------
Scanning started at {target_ip}
Time {datetime.datetime.now()}
---------------------------------------
"""

print(output_message)

# Unclear if the task is to scan up to the max ports, or the most common ones.
for port in range(1, 65536):
    # Create a TCP INET, Streaming socket per connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)

    if sock.connect_ex((target_ip, port)) == 0: # Important to know if a port was successfully connected. https://docs.python.org/3/library/socket.html#socket.socket.connect_ex
        ports_opened.append(port)
        print(f"Checking port {port} - OPEN")
    else:
        print(f"Checking port {port}")

    sock.close()

print(f"Ports opened: {ports_opened}")