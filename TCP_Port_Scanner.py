import argparse
import socket

parser = argparse.ArgumentParser(description="Port Scanner tcp")
parser.add_argument("-i", "--ip", help="Target IPv4", required=True)
parser.add_argument("-s", "--start", help="Starting port", type=int, required=True)
parser.add_argument("-e", "--end", help="Ending port", type=int, required=True)
args = parser.parse_args()

target = args.ip
start_port = args.start
end_port = args.end

for port in range(start_port, end_port+1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

try:
    s.connect((target, port))
    print(f"The port {port} is open!")
    banner = s.recv(1024)
    if banner:
        print(f"Service: {banner.decode().strip()}")
        s.close()
except:
    print("No port was found!")
    pass