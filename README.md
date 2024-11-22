Os arquivos no Python são representados por objetos do tipo file18, que
oferecem métodos para diversas operações de arquivos. Arquivos podem ser
abertos para leitura ('r', que é o default), gravação ('w') ou adição ('a'), em
modo texto ou binário('b').
Em Python:
▪ sys.stdin representa a entrada padrão.
▪ sys.stdout representa a saída padrão.
▪ sys.stderr representa a saída de erro padrão.
A entrada, saída e erro padrões são tratados pelo Python como arquivos


abertos. A entrada em modo de leitura e os outros em modo de gravação.
Exemplo de escrita:


A cada iteração no segundo laço, o objeto retorna uma linha do arquivo de
cada vez.
Exemplo de leitura:

É possível ler todas as linhas com o método readlines()

Os objetos do tipo arquivo também possuem um método seek(), que permite
ir para qualquer posição no arquivo.
Na versão 2.6, está disponível o módulo io, que implementa de forma
separada as operações de arquivo e as rotinas de manipulação de texto.
