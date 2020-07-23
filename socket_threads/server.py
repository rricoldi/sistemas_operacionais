#Trabalho desenvolvido por Lucas Antonio Jaques da Costa e Renan Ricoldi Frois Pedro

import socket
from threading import Thread

PORTA = 1433      # Porta a ser escutada 

conexoes = []

def fibonacci_sequence(number, connection):
    a, b = 0, 1
    counter = 0
    while a <= number:
        a, b = b, a+b
        counter = counter+1
   
    response = str(number) + ' => ' + str(counter)
    connection.send(bytes(response, "utf8"))


def conexao():  # Função para lidar com conexão de novos clientes
    connections = 0
    while True:
        if(connections >= 1000):
            break
        connection, address = server.accept()   # Aceitando um novo cliente e recebendo as informações deste
        lista_de_clientes.append(connection)    # Introdução do cliente à lista de clientes
        connections = connections + 1

        Thread(target=chat, args = (connection, address, connections)).start()   # Nova thread para lidar com as mensagens do cliente conectado

def chat(connection, address, connections):
    number = int(connection.recv(1024).decode("utf8"))    # Recebimento de uma mensagem
    t = Thread(target=fibonacci_sequence, args=(number, connection))
    t.start()
    t.join()
    
    lista_de_clientes.remove(connection)
    connection.close()

    return

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria o socket

# socket.gethostname()

server.bind(('', PORTA))    # Atribui o ip e porta definidos ao socket
server.listen(100)    # Socket começa a ouvir o endereço

lista_de_clientes = []

t = Thread(target=conexao())    # Thread principal
t.start()
t.join()


server.close()  # Finaliza o socket