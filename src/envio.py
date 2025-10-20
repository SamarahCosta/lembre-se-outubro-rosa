#!/usr/bin/python3

import time
import smtplib
from email.mime.text import MIMEText

def enviar_email(remetente, senha, destinatario, assunto, mensagem):
    msg = MIMEText(mensagem, "plain", "utf-8")
    msg["Subject"] = assunto
    msg["From"] = remetente
    msg["To"] = destinatario

    # Conexão com servidor de email
    # Para contar com o Outlook use smtp.office365.com
    # Para contar com o Gmail use smtp.gmail.com
    with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.starttls()
        server.login(remetente, senha)
        server.send_message(msg)

    print(f"✅ O Email foi enviado para {destinatario}")