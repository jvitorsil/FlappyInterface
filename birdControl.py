import socket
import threading

class Receiver:
    def __init__(self):
        self.UDP_IP = "0.0.0.0"
        self.UDP_PORT = 1665
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.UDP_IP, self.UDP_PORT))
        self.flexValue = []
        self.MPUValue = 0
        self.freqValue = 1
        self.buttonValue = 0

    def readData(self):
        while True:

            data, addr = self.sock.recvfrom(1024)
            payload = data.decode()
            allData = payload.split("/")

            # self.flexValue = float(payload.split(";")[0])
            
            # self.flexValue = [i.split(';')[0] for i in allData]
            # self.freqValue = float(payload.split(";")[1])
            
            print(payload)
            

    def obter_flexValue(self):
        return self.flexValue
    
    def obter_freqValue(self):
        return self.freqValue
    
if __name__ == '__main__':
    receiver = Receiver() 
    threadReceiveData = threading.Thread(target=receiver.readData)
    threadReceiveData.start()