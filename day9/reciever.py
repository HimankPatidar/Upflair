import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
ip = "10.1.0.94" 
port  = 9999

complete_address = (ip,port)
s.bind(complete_address)

while True :
    data = s.recvfrom(120)
    message = data[0]   
    message = message.decode("ascii")
    message = message + "\n"
    sender_ip = data[1][0]
    filename = sender_ip + "txt"
    with open(filename, "a+") as file :
        file.write(message)
    reply_msg = "Your message has been recieved"
    reply = reply_msg.encode("ascii")
    s.sendto(reply, data[1])
    print("Message sent to ", sender_ip)