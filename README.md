Journal

criada conexao client e cache de teste para a manipulacao do socket, com operacao de envio e recebimento de um unico dado
organizacao do codigo em funcoes e metodos
definicao de uma cache com os campos: segundo de acesso, dado e porta do servidor que contem o dado para quando for feita a consulta
(ainda nao foi feito os servidores)
implementacao de uma interface para o cliente solicitar dado do servidor que for de interesse (utilizando apenas o client)
realizacao da conexao com a cache, solicitando o dado de acordo com a entrada do usuario
teste de leitura, armazenando valores aleatorios na cache (sem conectar com os servidores ainda) com tempo de validade
implementacao dos servidores com uma porta diferente para cada (com o mesmo arquivo python diferenciando na linha de comando os servidores)
conexao dos servidores com a cache
alteracao do metodo de acesso aos dados, usando agora os servidores conectados
criacao de um dicionario proprio para os dados dos servidores (porta e conexao), removendo da cache
adicao de comentarios no codigo
adaptacao do codigo de geracao de numeros aleatorios, usando um range definido para cada servidor
criacao de mensagens de log