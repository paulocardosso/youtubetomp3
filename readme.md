# Projeto Converter Youtube Para Mp3 Usando Python, Pytube

## Introdução

A procura por sites de conversões é alta, entretanto, vários deles possuem popups indesejaveis e até perigosos/maliciosos.
Sendo assim, desenvolvi um pequeno projeto desktop capaz de realizar essa conversão, de forma legivel para todos, pois está
com uma interface gráfica amigavel. 

## Objetivo do Projeto

1. Realizar uma conversão de um vídeo qualquer no Youtube para um arquivo .mp3
    1. Usar uma interface gráfica para deixar o programa légivel para todos
        1. Foi usada a biblioteca PysimpleGui para a interface gráfica
    1. Usar uma biblioteca do python capaz de baixar videos do Youtube em diversos formatos e qualidades diferentes
        1. Foi utilizado a biblioteca Pytube para essa finalidade
    1. Fazer a integração das duas bibliotecas
    1. Pedir ao usuário os dados de entrada: o link do vídeo e a pasta de destino
    1. Fazer a conversão
1. Salvar esse arquivo no diretorio escolhido pelo usuário