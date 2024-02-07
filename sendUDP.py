import socket
import time

UDP_IP = "172.20.10.5"
UDP_PORT = 1665

flexValue = 0.0
buttonValue = 0
freqValue = 50.0
MPUValue = 0.0

while True:

    if flexValue >= 100:
        flexValue = 0.0
        freqValue += 1
        if freqValue >= 100:
            freqValue = 50.0

    if MPUValue >= 100:
        MPUValue = 0.0
    

    payload = str(flexValue) + ";" + str(buttonValue) + ";" + str(freqValue) + ";" + str(MPUValue)
    payloadEncode = str.encode(payload)

    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) 
    UDPClientSocket.sendto(payloadEncode, (UDP_IP, UDP_PORT))

    print(payloadEncode)

    flexValue += 1.0
    MPUValue += 2.0

    time.sleep(1/freqValue)
