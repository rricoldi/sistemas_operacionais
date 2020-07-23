import socket
import sys
from threading import Thread

HOST = ''  # Endereço IP que tentará conectar
PORTA = 1433      # Porta a ser conectada

def receber(server):  # Função que recebe as mensagens do servidor e mostra ao cliente
    mensagem = ''
    while mensagem == '':
        try:
            mensagem = server.recv(1024).decode("utf8")
            print(mensagem)
            break
        except OSError:
            break


def enviar(number): # Função que recebe mensagens do cliente e as envia ao servidor
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria o socket
    server.connect((HOST, PORTA))  # Conecta ao servidor
    counter = 0
    mensagem = str(number)

    server.send(bytes(mensagem, "utf8"))

    t = Thread(target=receber, args=[server])
    t.start()  # Threads para receber e enviar ao mesmo tempo
    t.join()
    
    server.close()
    # if "sair()" in mensagem:  # Caso a mensagem seja "sair()" fecha a conexão
    #   server.close()
    #   break
      


for i in range(1000):
    question = (i+1)*300
    Thread(target=enviar, args=[question]).start()
