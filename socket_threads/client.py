#Trabalho desenvolvido por Lucas Antonio Jaques da Costa e Renan Ricoldi Frois Pedro

import socket
import sys
from threading import Thread
import time
import matplotlib.pyplot

HOST = ''  # Endereço IP que tentará conectar
PORTA = 1433      # Porta a ser conectada
NUMERO_DE_THREADS = 200 # Número de trheads que serão rodadas

conexoes = []

def receber(server, start, number):  # Função que recebe as mensagens do servidor e mostra ao cliente
    mensagem = ''
    while mensagem == '':
        try:
            mensagem = server.recv(1024).decode("utf8")
            conexoes.append(time.time() - start)
            print(mensagem)
            break
        except OSError:
            break


def enviar(number, start): # Função que recebe mensagens do cliente e as envia ao servidor
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria o socket
    server.connect((HOST, PORTA))  # Conecta ao servidor
    counter = 0
    mensagem = str(number)

    server.send(bytes(mensagem, "utf8"))

    t = Thread(target=receber, args=[server, start, number])
    t.start()  # Threads para receber e enviar ao mesmo tempo
    t.join()
    
    server.close()
    # if "sair()" in mensagem:  # Caso a mensagem seja "sair()" fecha a conexão
    #   server.close()
    #   break

def threads():
    start = time.time()
    for i in range(NUMERO_DE_THREADS):
        question = (i+1)*300
        Thread(target=enviar, args=[question, start]).start()

t = Thread(target=threads)
t.start()
t.join()

x = []
y = []
j = 0
for tempo in conexoes:
    j = j + 1
    y.append(round(float(tempo), 3))
    x.append(j)

matplotlib.pyplot.plot(x, y)
matplotlib.pyplot.xlabel('Numero de conexoes')
matplotlib.pyplot.ylabel('Tempo')
matplotlib.pyplot.show()
