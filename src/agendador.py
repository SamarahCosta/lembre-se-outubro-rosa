#!/usr/bin/python3
import schedule
import time
from datetime import datetime
import random
from utilitario import ler
from envio import enviar_email

# Caminho do arquivo de mensagens
mensagens = ler("Caminho/completo/para/o/arquivo/mensagens.txt")

def executar():

    DATA_LIMITE = datetime(2025, 10, 31)
    hoje = datetime.now()

    if hoje.date() > DATA_LIMITE.date():
        print("⏹️ Prazo final 31/10/2025 atingido. Encerrando agendamentos.")
        return
    
    msg = random.choice(mensagens)
    
    # A Senha deve ser jerado em:
    
    # Gmail: https://myaccount.google.com/apppasswords
        # Selecione: Outro > nome personalizado.
        # Vai gerar uma senha de 16 caracteres. Use essa senha no lugar da sua senha normal.
        
    # Outlook: https://mysignins.microsoft.com/security-info 
        # Selecione: Adicionar método > Senha de aplicativo.
        # Vai gerar uma senha longa. Use essa senha no lugar da sua senha normal.
        
    enviar_email(
        mensagem=msg,
        assunto="Lembre-se, Outubro Rosa 🎀",
        remetente="email@quemVaiEnviar.com",
        senha="senhaGeradaNoPassoAcima",
        destinatario="email@quemVaiReceber.com"
    )

# Agendamento diário às 10h (apenas uma vez por dia)
schedule.every().day.at("10:00").do(executar)

print("🕙 Agendador iniciado! Os envios ocorrem todos os dias às 10h até 31/10/2025.")

# Verifica a cada 5 minutos se há tarefas agendadas para serem executadas
while True:
    schedule.run_pending()
    print("⏳ Aguardando horário do próximo envio...")
    time.sleep(300)