Operações de arquivo em Python

Visão geral

Este programa demonstra operações básicas de arquivo em Python, incluindo:

Gravação de dados em um arquivo

Leitura de dados de um arquivo

Manipulação de erros de entrada/saída de arquivo

Solicitação de entrada de arquivo ao usuário

Enumeração de linhas de um arquivo e armazenamento do conteúdo do arquivo como uma lista.

Como funciona

Gravação em um arquivo

O código cria um arquivo temp.txt e grava 100 linhas nele com cada número formatado como um valor de três dígitos (por exemplo, 000, 001, ..., 099).

A instrução with open('temp.txt', 'w') as temp: garante o fechamento adequado do arquivo após a gravação.

Leitura de um arquivo

O programa lê e imprime cada linha de temp.txt usando with open('temp.txt', 'r') as temp:.

Se a leitura falhar, uma mensagem de erro será exibida via sys.stderr.write.

Entrada de arquivo do usuário

O programa solicita que o usuário insira um nome de arquivo. Se nenhum for fornecido, o padrão é temp.txt.

Se o arquivo não existir, o programa sai com uma mensagem.

Enumeração de linha

As linhas do arquivo são enumeradas, começando em 1, e impressas junto com o conteúdo.

Armazenando conteúdo do arquivo

O programa lê todas as linhas do arquivo em uma lista usando file.readlines() e imprime a lista resultante.

Tratamento de erro

Todas as operações de arquivo são incluídas em blocos try-except para lidar com possíveis exceções IOError.

Saída de exemplo

000
001
002
...
099
Digite o nome do arquivo (o padrão é temp.txt): temp.txt
1 000
2 001
...
100 099
['000\n', '001\n', ..., '099\n']

Dependências

Nenhuma biblioteca externa é necessária.

Como executar

Certifique-se de ter o Python instalado.

Salve o código em um arquivo, por exemplo, file_operations.py.

Execute o script usando:

python file_operations.py

Siga as instruções na tela.

Melhorias

Validação de entrada de arquivo: Melhore a validação de entrada verificando os tipos de arquivo.

Tratamento de exceção: Forneça mensagens de erro mais específicas.

Registro: Implemente o registro em vez de imprimir erros.

Interface do usuário: Considere adicionar uma interface orientada a menu.
