import socket
import threading

class Receptor:
    def __init__(self):
        self.UDP_IP = "0.0.0.0"
        self.UDP_PORT = 1665
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.UDP_IP, self.UDP_PORT))
        self.flexValue = 0 
        self.MPUValue = 0
        self.freqValue = 1
        self.buttonValue = 0

    def recebe_dados(self):
        while True:
            data, addr = self.sock.recvfrom(1024)
            payload = data.decode()
            self.flexValue = float(payload.split(";")[0])
            self.buttonValue = int(payload.split(";")[1])
            self.freqValue = float(payload.split(";")[2])
            self.MPUValue = float(payload.split(";")[3])
            print(payload)
            

    def obter_flexValue(self):
        return self.flexValue
    
    def obter_freqValue(self):
        return self.freqValue
    
if __name__ == '__main__':
    receptor = Receptor()  # Instancie a classe Receptor
    thread_recebe_dados = threading.Thread(target=receptor.recebe_dados)
    thread_recebe_dados.start()