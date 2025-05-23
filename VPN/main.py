import socket
import subprocess
import sys

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 1194))  # פורט רגיל של VPN
    s.listen(1)
    print("VPN server is running...")

    conn, addr = s.accept()
    print(f"Connection from {addr}")
    while True:
        data = conn.recv(4096)
        if not data:
            break
        print(f"[{addr}] {data.decode()}")  # הדמיה של תעבורה
        conn.sendall(data)
    conn.close()

def start_client(server_ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, 1194))
    print("Connected to VPN server")
    while True:
        msg = input("Send: ")
        if msg == "exit":
            break
        s.sendall(msg.encode())
        data = s.recv(4096)
        print(f"Received: {data.decode()}")
    s.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python vpn.py <mode: server/client> [server_ip]")
        sys.exit(1)
    mode = sys.argv[1]
    if mode == "server":
        start_server()
    elif mode == "client" and len(sys.argv) == 3:
        start_client(sys.argv[2])
    else:
        print("Invalid arguments.")
