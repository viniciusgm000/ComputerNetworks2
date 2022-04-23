# Descrição do Trabalho da disciplina de Redes de Computadores 2:

1 - Você tem 3 servidores de temperatura em lugares extremos do mundo: ou normalmente muito frios ou normalmente muito quentes. Cada um destes servidores recebem uma resposta e simplemente mandam uma resposta com um número inteiro que mais se aproxima da temperatura medida.

2 - Um cliente não acessa os servidores individualmente, e sim uma cache que mantém os últimos valores recebidos dos 3 servidores. Assim evitamos que o cliente tenha que fazer 3 acessos muito distantes, para fazer 1 acesso mais próximo.

3 - A cache mantém uma tabela cache com os dados, com um prazo de validade para cada entrada de 30 segundos. Implemente o cliente. Implemente também a tabela cache da maneira eficiente que foi apresentada em sala de aula. Quando chega uma requisição e algum valor expirou, deve ser feita nova consulta ao servidor original.

4 - Para os 3 servidores, a dupla pode tanto implementá-los como servidores do trabalho, utilizando número aleatórios dentro de uma faixa razoável para os valores de temperatura ou, alternativamente, obter as informações adequadamente na Web.

5 - Devem ser apresentados logs para múltiplas execuções. Mostre com clareza situações em que uma requisição de usuário encontra/não encontra a cache com informações válidas.


# Diário de implementação

criada conexao client e cache de teste para a manipulacao do socket, com operacao de envio e recebimento de um unico dado

organizacao do codigo em funcoes e metodos

definicao de uma cache com os campos: segundo de acesso, dado e porta do servidor que contem o dado para quando for feita a consulta (ainda nao foi feito os servidores)

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

adicao de timestamps para os logs

# Relatório:

https://www.inf.ufpr.br/vgm18/trabalhos_disciplinas/cachehash/cachehash.html