import birdControl
import threading
import time

receptor = birdControl.Receptor()  # Instancie a classe Receptor
thread_recebe_dados = threading.Thread(target=receptor.recebe_dados)
thread_recebe_dados.start()

def obter_flexValue(self):
    return self.flexValue
    
    def obter_freqValue(self):
    return self.freqValue

# Função para inicializar o gráfico
def iniciar_grafico():
    buffer_size = 50
    tempo = np.arange(0, buffer_size)
    flex_values = deque([0] * buffer_size, maxlen=buffer_size)
    freq_values = deque([0] * buffer_size, maxlen=buffer_size)  # New deque for freq_values

    fig, ax = plt.subplots()
    line1, = ax.plot(tempo, flex_values, label='Flex Sensor Value')  # Line for flex_values
    line2, = ax.plot(tempo, freq_values, label='Freq Sensor Value')  # New line for freq_values

    ax.set_xlabel('Tempo')
    ax.set_ylabel('Sensor Values')
    ax.set_title('Gráfico em Tempo Real do Flex Sensor e Freq Sensor')
    ax.set_ylim(-10, 1024)  # Substitua 1024 pelo valor máximo desejado
    ax.legend()  # Add a legend to distinguish between the two lines

    return fig, ax, line1, line2, flex_values, freq_values  # Return the new line and deque

# Função de animação para atualizar o gráfico em tempo real
def atualizar_grafico(frame, receptor, line1, line2, flex_values, freq_values):  # Add line2 and freq_values as parameters
    flex_values.append(receptor.obter_flexValue())
    freq_values.append(receptor.obter_freqValue())  # Append the new freqValue to freq_values

    line1.set_ydata(flex_values)  # Update the y-data of line1
    line2.set_ydata(freq_values)  # Update the y-data of line2

    return line1, line2  # Return both lines

def main():
    receptor = Receptor()
    fig, ax, line1, line2, flex_values, freq_values = iniciar_grafico()

    # Iniciar thread para receber dados
    thread_receber = threading.Thread(target=receptor.recebe_dados)
    thread_receber.daemon = True
    thread_receber.start()

    # Iniciar animação
    animacao = FuncAnimation(fig, atualizar_grafico, fargs=(receptor,  line1, line2, flex_values, freq_values), interval=100)

    plt.show()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()
