import socket

UDP_IP = "0.0.0.0"  # Escutando em todos os endereços disponíveis
UDP_PORT = 1665

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)

    payload = data.decode()

    flexValue = payload.split(";")[0]
    buttonValue = payload.split(";")[1]
    freqValue = payload.split(";")[2]
    MPUValue = payload.split(";")[3]