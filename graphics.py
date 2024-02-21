import sys
import time
import threading
import numpy as np
import matplotlib.pyplot as plt
import birdControl
from matplotlib.animation import FuncAnimation
from collections import deque

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
    ax.set_ylim(0, 4095)  # Substitua 1024 pelo valor máximo desejado
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
    receptor = birdControl.Receiver()
    fig, ax, line1, line2, flex_values, freq_values = iniciar_grafico()

    thread_receber = threading.Thread(target=receptor.readData)
    thread_receber.daemon = True
    thread_receber.start()

    # Iniciar animação
    animacao = FuncAnimation(fig, atualizar_grafico, fargs=(receptor,  line1, line2, flex_values, freq_values), interval=1000/receptor.obter_flexValue())

    plt.show()

if __name__ == "__main__":
    main()
