import socket
import sys

# definicao do host utilizado - localhost
HOST = "127.0.0.1"

# definicao da porta para conexao com a cache
CACHE_PORT = 42342

# funcao para se conectar com a cache
def connect_cache():
    # definicao do socket a ser utilizado, realizando a conexao com a porta pre-definida
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, CACHE_PORT))
    print(f"Realizada a conexao com a cache")
    return s

# funcao para comunicacao com a cache - segue o padrao: solicita entao recebe dado
def send_receive_cache(s, data):
    # envio do id do servidor para solicitacao de dados para a cache
    s.sendall(bytes(data, encoding = 'utf-8'))
    # recebimento da resposta da cache
    received = s.recv(1024)
    return received.decode("utf-8")

# funcao para leitura da entrada do usuario
def get_user_input(s):
    # leitura da entrada enquanto o usuario quiser
    print("Qual temperatura gostaria de consultar?")
    print("Opcoes:")
    print("1 - Antartida; 2 - Deserto de Atacama; 3 - Monte Everest; exit - termina a execucao")
    while True:
        user_input = input()
        # opcao para terminar a execucao do cliente, consequentemente, fecha todos os processos em cascata
        if (user_input == "exit"):
            print("Cliente finalizado")
            sys.exit()
        # entrada erronea
        elif (user_input == "" or not (1 <= int(user_input) <= 3)):
            print("Opção indisponível, digite novamente")
        # envio da solicitacao de dados para a cache, em caso de entrada correta
        else:
            print("Solicitando o dado do servidor " + user_input)
            received = send_receive_cache(s, user_input)
            print("Dado recebido: " + received)

# funcao principal
def main():
    print("Cliente inicializado")
    # conexao com a cache
    s = connect_cache()
    # leitura da entrada do usuario
    get_user_input(s)

if __name__ == "__main__":
    main()