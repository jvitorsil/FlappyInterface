import socket
import sys
import time
import threading
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque

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

    def obter_flexValue(self):
        return self.flexValue
    
    def obter_freqValue(self):
        return self.freqValue
# Função para inicializar o gráfico
def iniciar_grafico():
    buffer_size = 50
    tempo = np.arange(0, buffer_size)
    flex_values = deque([0] * buffer_size, maxlen=buffer_size)
    freq_values = deque([0] * buffer_size, maxlen=buffer_size)  

    fig, ax = plt.subplots()
    line1, = ax.plot(tempo, flex_values, label='Flex Sensor Value') 
    line2, = ax.plot(tempo, freq_values, label='Freq Sensor Value')  

    ax.set_xlabel('Tempo')
    ax.set_ylabel('Sensor Values')
    ax.set_title('Gráfico em Tempo Real do Flex Sensor e Freq Sensor')
    ax.set_ylim(-10, 1024)  # Substitua 1024 pelo valor máximo desejado
    ax.legend()  

    return fig, ax, line1, line2, flex_values, freq_values  

# Função de animação para atualizar o gráfico em tempo real
def atualizar_grafico(frame, receptor, line1, line2, flex_values, freq_values):  
    flex_values.append(receptor.obter_flexValue())
    freq_values.append(receptor.obter_freqValue()) 

    line1.set_ydata(flex_values)  
    line2.set_ydata(freq_values)  
    
    return line1, line2  

def main():
    receptor = Receptor()
    fig, ax, line1, line2, flex_values, freq_values = iniciar_grafico()

    # Iniciar thread para receber dados
    thread_receber = threading.Thread(target=receptor.recebe_dados)
    thread_receber.daemon = True
    thread_receber.start()

    # Iniciar animação
    animacao = FuncAnimation(fig, atualizar_grafico, fargs=(receptor,  line1, line2, flex_values, freq_values), interval=50)

    plt.show()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()
