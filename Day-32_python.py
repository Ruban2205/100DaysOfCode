# Check if a string is a valid IP address.
print("\nRuban Gino Singh - Day 32 of #100DaysOfCode\n")

print("Python program to check if a string is a valid IP address.\n")

import socket

def is_valid_ip(ip_str):
    try:
        socket.inet_pton(socket.AF_INET, ip_str)
        return True
    except socket.error:
        try:
            socket.inet_pton(socket.AF_INET6, ip_str)
            return True
        except socket.error:
            return False

ip_address = input("Enter an IP address: ")
if is_valid_ip(ip_address):
    print(f"{ip_address} is a valid IP address.")
else:
    print(f"{ip_address} is not a valid IP address.")

# --------------------------------------------------------- #