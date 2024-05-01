import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "10.1.0.94"
port = 9999
target_ip = (ip, port)
message = input("Enter your message: ")
encypted_message = message.encode("ascii")
s.sendto(encypted_message, target_ip)

print("Message sent to ", ip)

