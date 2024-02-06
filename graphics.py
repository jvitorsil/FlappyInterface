import birdControl
import threading
import time

receptor = birdControl.Receptor()  # Instancie a classe Receptor
thread_recebe_dados = threading.Thread(target=receptor.recebe_dados)
thread_recebe_dados.start()

print(receptor.obter_flexValue())