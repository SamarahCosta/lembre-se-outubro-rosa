#!/usr/bin/python3

import csv

def ler(caminho_csv):
    mensagens = [] 
    
    with open(caminho_csv, newline='', encoding='latin-1') as arquivo:
        
        #Lendo como dicionario
        leitor = csv.DictReader(arquivo)
        
        for i in leitor:
            
            #Pegando o valor de uma linha da coluna mensagem e adiciona na lista
            mensagens.append(i['mensagem'])
            
    return mensagens