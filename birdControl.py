import socket
import threading

class Receiver:
    def __init__(self):
        self.UDP_IP = "0.0.0.0"
        self.UDP_PORT = 1665
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.UDP_IP, self.UDP_PORT))
        self.flexValue = []
        self.freqValue = []

    def readData(self):
        while True:

            data, addr = self.sock.recvfrom(1024)
            payload = data.decode()
            allData = payload.split("/")
            
            self.flexValue = list(map(int, [i.split(';')[0] for i in allData]))
            self.freqValue = list(map(int, [i.split(';')[1] for i in allData]))
            
            print("Flex: " + str(self.flexValue) + " : Freq: " + str(self.freqValue))

    def obter_flexValue(self):
        return self.flexValue
    
    def obter_freqValue(self):
        return self.freqValue
    
if __name__ == '__main__':
    receiver = Receiver() 
    threadReceiveData = threading.Thread(target=receiver.readData)
    threadReceiveData.start()