#!/usr/bin/python3
import schedule
import time
import random
from utilitario import ler
from envio import enviar_email

mensagens = ler("seu_arquivo_aqui.csv")

def executar():
    msg = random.choice(mensagens)
    enviar_email(
        mensagem=msg,
        assunto="Outubro Rosa",
        remetente="seuemail@aqui",
        senha="suasenha_aqui",
        destinatario="seuemail@aqui"
    )
    # Agenda para rodar a cada 2 minuto
    schedule.every(2).minutes.do(executar)

    while True:
      schedule.run_pending()
      time.sleep(1)
    