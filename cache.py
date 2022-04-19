import socket
import time

# definicao do host utilizado - localhost
HOST = "127.0.0.1"

# definicao da porta para conexao com o cliente
CLIENT_PORT = 42342

# tempo de expiracao dos dados da cache - padrao 30 segundos
CACHE_EXPIRATION = 30

# definicao dos servidores para a cache fazer acesso, com a porta e o socket definido para cada um
servers = {
    "1": {"server_port": 42111, "server_socket": None},
    "2": {"server_port": 42222, "server_socket": None},
    "3": {"server_port": 42333, "server_socket": None}
}

# definicao da cache contendo o segundo do ultimo acesso e o dado registrado no ultimo acesso
# se o segundo atual menos o segundo do ultimo acesso for maior que o tempo de expiracao,
# a cache ira solicitar a atualizacao do dado para o servidor
cache = {
    "1": {"access_time": 0, "data": "1000"},
    "2": {"access_time": 0, "data": "1000"},
    "3": {"access_time": 0, "data": "1000"}
}

# funcao de acesso a cache
def get_cache_data(server_id):
    # teste de expiracao do dado
    if (time.time() - cache[server_id]["access_time"] > CACHE_EXPIRATION):
        print("Dado expirado, solicitando a atualizacao pelo servidor")
        # registra o novo segundo de acesso e solicita a atualizacao do dado
        cache[server_id]["access_time"] = time.time()
        cache[server_id]["data"] = send_receive_server(server_id)
        print("Dado recebido: " + cache[server_id]["data"])
    else:
        print("Dado ainda nao expirou, acessando a cache")
    cache_data = cache[server_id]["data"]
    return str(cache_data)

# client

# funcao de criacao da conexao com o cliente - o cliente ira se conectar a ela
def create_connection_client():
    # criacao do socket a ser utilizado para a cache, ouvindo o cliente na porta especificada
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, CLIENT_PORT))
    s.listen()
    conn, addr = s.accept()
    print(f"Criada conexao para o cliente por {addr}")
    return conn

# funcao para comunicacao com o cliente - segue o padrao: recebe solicitacao entao responde
def receive_send_client(conn):
    with conn:
        # escuta enquanto a conexao eh mantida pelo cliente
        while True:
            # recebe o dado da solicitacao da cliente contendo o id do servidor
            data = conn.recv(1024)
            if not data:
                break
            elif (1 <= int(data) <= 3):
                print("Recebida solicitação de dado de temperatura pelo cliente")
                # acessa o dado e envia a resposta ao cliente
                cache_data = get_cache_data(data.decode("utf-8"))
                conn.sendall(bytes(cache_data, encoding = 'utf-8'))
                print("Dado enviado para o cliente: " + cache_data)

# servers

# funcao para conexao com o servidor
def connect_server(server_id):
    # definicao do socket a ser utilizado, realizando a conexao com a porta pre-definida
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, servers[server_id]["server_port"]))
    # registro do socket no dicionario de servidores
    servers[server_id]["server_socket"] = s
    print(f"Realizada a conexao com o servidor " + server_id)

# funcao para comunicacao com o servidor - segue o padrao: envia solicitacao e recebe dado
def send_receive_server(server_id):
    # envio da solicitacao de dados para o servidor especificado - utilizando uma flag para confirmar a conexao correta
    servers[server_id]["server_socket"].sendall(bytes("get_data", encoding = 'utf-8'))
    received = servers[server_id]["server_socket"].recv(1024)
    return received.decode("utf-8")

# main

# funcao principal
def main():
    print("Cache inicializada")
    # criacao da conexao com o cliente
    client_conn = create_connection_client()
    # conexao com os servidores
    connect_server("1")
    connect_server("2")
    connect_server("3")
    # escuta as solicitacoes do cliente
    receive_send_client(client_conn)
    print("Cache finalizada")


if __name__ == "__main__":
    main()