# Projeto Converter Youtube Para Mp3 Usando Python, Pytube

## Introdução

Nos dias atuais, é bastante comum realizar conversões de arquivos, dentro os quais destaco:
a conversão de vídeos do Youtube para um arquivo .mp3. Hoje em dia, existem diversos sites
que realizam esse tipo de conversão, porém os mesmos apresentam centenas de pop-ups indesejáveis
e que podem ser maliciosos (por conter vírus/malware). Sendo assim, foi criado um pequeno software
capaz de realizar essa conversão de forma amigável (com interface gráfica) e sem correr o risco de
causar danos ao sistema.

## Objetivo do Projeto

1. Realizar uma conversão simples de um vídeo qualquer no Youtube para um arquivo de áudio no formato: .mp3
    1. Criar uma interface gráfica para deixar o programa legível para todos
        1. Utilizar a biblioteca PysimpleGui para criação da interface gráfica
    1. Criar um método de conversão de vídeos em arquivos .mp3
        1. Utilizar a biblioteca Pytube para essa finalidade
    1. Integrar as duas bibliotecas utilizadas
    1. Pedir ao usuário os dados de entrada: o nome do arquivo, o link do vídeo e a pasta de destino
    1. Realizar a conversão e informar onde foi salvo o arquivo
    
## Metodologia

O projeto foi baseado em uma programação orientada a objetos (POO) utilizando a linguagem Python
e suas bibliotecas (Pytube e PysimpleGUI). Inicialmente foi criada uma classe Tela para exibir ao
usuário uma interface gráfica, essa classe possui dois métodos: o construtor (_init_) e o Iniciar.
O construtor apenas vai instanciar uma tela, com os atributos (inputs) necessários para realizar uma
conversão. Enquanto o método Iniciar, além de gerar a tela, vai realizar ações/interações com o usuário
final, usando a integração das duas bibliotecas (Pytube e PysimpleGUI). Além da classe Tela, existe
um método converter, que utiliza a biblioteca Pytube para realizar o download do vídeo, mas no formato
de áudio: .mp3.

## Resultados

Foram realizados vários testes antes de publicar este mini projeto no Github, os testes estão logo abaixo:

> 1º Teste: Ao executar o arquivo “converter.py” e clicarmos apenas em ‘Converter’, obtemos a seguinte saída
>>**Entradas:**\
>>`name=None`\
>>`link=None`\
>>`pasta=None`
>
>>**Saída:**\
>>`Por favor, preenche os campos obrigatórios para realizar a conversão!`

> 2º Teste: Ao executar o arquivo “converter.py”, preencher a entrada link e name com uma string qualquer e clicarmos apenas em ‘Converter’, obtemos a seguinte saída
>>**Entradas:**\
>>`name=aaaa`\
>>`link=bbbb`\
>>`pasta=None`
>
>>**Saída:**\
>>`Link/URL Invalído! Por favor, tente novamente!`

> 3º Teste: Ao executar o arquivo “converter.py”, preencher todas as entradas e clicarmos apenas em ‘Converter’, obtemos a seguinte saída
>>**Entradas:**\
>>`name=aaaa`\
>>`link=https://www.youtube.com/watch?v=ZYgifSfojG8`\
>>`pasta=C:/Users/Paulo/Desktop`
>
>>**Saída:**\
>>`Conversão Concluída!`\
>>`Local: C:\Users\Paulo\Desktop\aaaa.mp3`

> 4º Teste: Ao executar o arquivo “converter.py”, preencher todas as entradas, exceto a entrada pasta e clicarmos apenas em ‘Converter’, obtemos a seguinte saída
>>**Entradas:**\
>>`name=aaaa`\
>>`link=https://www.youtube.com/watch?v=ZYgifSfojG8`\
>>`pasta=None`
>
>>**Saída:**\
>>`Conversão Concluída!`\
>>`Local: DiretórioDoArquivoPython\aaaa.mp3`

## Discussão

O presente trabalho apresentou um resultado satisfatório. Porém, diversas melhorias podem ser
implementadas, dentro as quais destaco: uma implementação para realizar conversões de playlist do
Youtube e ainda permitir outros formatos diferentes, não apenas o arquivo .mp3, mas também o próprio
vídeo, .mp4

## Referências

1. Python
    1. https://www.python.org/
1. Pytube
    1. https://pytube.io/
1. PysimpleGui
    1. https://pysimplegui.readthedocs.io/