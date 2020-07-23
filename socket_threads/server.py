import socket
from threading import Thread
import time
import matplotlib.pyplot

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
    start = time.time()
    while True:
        if(connections >= 1000):
            break
        connection, address = server.accept()   # Aceitando um novo cliente e recebendo as informações deste
        lista_de_clientes.append(connection)    # Introdução do cliente à lista de clientes
        connections = connections + 1

        Thread(target=chat, args = (connection, address, start, connections)).start()   # Nova thread para lidar com as mensagens do cliente conectado
        # print('conexoes: ' + str(connections) + ' X  tempo: ' + str(time.time() - start))

def chat(connection, address, start, connections):
    number = int(connection.recv(1024).decode("utf8"))    # Recebimento de uma mensagem
    t = Thread(target=fibonacci_sequence, args=(number, connection))
    t.start()
    t.join()
    conexoes.append((str(time.time() - start), connections))
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

x = []
y = []

for (tempo, conn) in conexoes:
    y.append(round(float(tempo), 3))
    x.append(conn)

matplotlib.pyplot.plot(x, y)
matplotlib.pyplot.xlabel('Numero de conexoes')
matplotlib.pyplot.ylabel('Tempo')
matplotlib.pyplot.show()

server.close()  # Finaliza o socket