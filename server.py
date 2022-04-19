import socket
import sys
import secrets

# definicao do host utilizado - localhost
HOST = "127.0.0.1"

# definicao das portas dos servidores - permitindo a execucao de multiplos servidores com o mesmo arquivo python
# definicao do nome e range de temperatura para o algoritmo aleatorio
servers = {
    "1": {"port": 42111, "name": "Antartida", "range_end": -10, "range_start": -60},
    "2": {"port": 42222, "name": "Deserto de Atacama", "range_end": 32, "range_start": -2},
    "3": {"port": 42333, "name": "Monte Everest", "range_end": -19, "range_start": -36}
}

# referencias:
# https://www.antarctica.gov.au/about-antarctica/weather-and-climate/weather/
# https://tierrahotels.com/atacama/atacama-chile-travel-tips/san-pedro-atacama-desert-weather-packing-list
# https://www.nzherald.co.nz/world/12-extreme-facts-about-mount-everest/CAX46UUCXLFBWBUVKLK7RHTHHU/

# instanciamento da classe de randomizacao
rng = secrets.SystemRandom()

# funcao para criacao da conexao com a cache, a cache ira se ligar a ela
def create_connection_cache(server_id):
    # criacao do socket a ser utilizado para cada servidor, ouvindo a cache em diferentes portas para cada servidor
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, servers[server_id]["port"]))
    s.listen()
    conn, addr = s.accept()
    print(f"Criada conexao para a cache por {addr}")
    return conn

# funcao para comunicacao com a cache - segue o padrao: recebe solicitacao entao responde
def receive_send_cache(conn, server_id):
    with conn:
        # escuta enquanto a conexao eh mantida pela cache
        while True:
            # recebe o dado da solicitacao da cache
            data = conn.recv(1024)
            if not data:
                break
            # se o conteudo for o esperado - para garantir que a conexao eh a correta - envia o dado de temperatura do servidor
            # de acordo com o range permitido, arredondando para o inteiro mais proximo
            elif (data.decode('utf-8') == "get_data"):
                print("Recebida solicitação de dado de temperatura pela cache")
                temperature = str(round(rng.uniform(servers[server_id]["range_start"], servers[server_id]["range_end"])))
                temperature = "Temperatura no(a) " + servers[server_id]["name"] + ": " + temperature + "°C"
                print("Dado enviado para a cache: " + temperature)
                conn.sendall(bytes(temperature, encoding = 'utf-8'))

# funcao principal
def main(server_id):
    print("Servidor " + server_id + " inicializado")
    # cria a conexao que sera utilizada pela cache, 
    # utilizando uma porta diferente para cada servidor (definido pelo id informado na linha de comando)
    conn = create_connection_cache(server_id)
    # escuta as solicitacoes da cache
    receive_send_cache(conn, server_id)
    print("Servidor " + server_id + " finalizado")

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Erro - Uso correto:")
        print(str(sys.argv[0]), "server.py <ID_SERVER>")
        sys.exit()

    main(str(sys.argv[1]))