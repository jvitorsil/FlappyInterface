import socket
import sys
import time

class Receptor:
    def __init__(self):
        self.UDP_IP = "0.0.0.0"
        self.UDP_PORT = 1665
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.UDP_IP, self.UDP_PORT))
        self.flexValue = 0 
        self.MPUValue = 0
        self.freqValue = 1


    def recebe_dados(self):
        while True:
            data, addr = self.sock.recvfrom(1024)
            payload = data.decode()
            self.flexValue = payload.split(";")[0]
            self.buttonValue = payload.split(";")[1]
            self.freqValue = payload.split(";")[2]
            self.MPUValue = payload.split(";")[3]

            print(self.flexValue)
            
    # def obter_flexValue(self):
    #     return self.MPUValue

    # def obter_freqValue(self):
    #     return int(self.freqValue)