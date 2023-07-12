# enviando email com python

import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

load_dotenv()

remetente = os.getenv("FROM_EMAIL", "")
destinatario = os.getenv("FROM_EMAIL", "")

# configurações do SMTP

smtp_server = "smpt.gmail.com"
smtp_port = 587
smtp_user = os.getenv("FROM_EMAIL", "")
smtp_passwd = os.getenv("EMAIL_PASSWORD", "")

mensagem = """
TESTE |TESTE |TESTE |TESTE |TESTE |TESTE |TESTE |TESTE |TESTE |TESTE |TESTE
TESTE |TESTE |TESTE |TESTE |TESTE |TESTE |TESTE |TESTE |TESTE |TESTE |TESTE
TESTE |TESTE |TESTE |TESTE |TESTE |TESTE |TESTE |TESTE |TESTE |TESTE |TESTE
TESTE |TESTE |TESTE |TESTE |TESTE |TESTE |TESTE |TESTE |TESTE |TESTE |TESTE
TESTE |TESTE |TESTE |TESTE |TESTE |TESTE |TESTE |TESTE |TESTE |TESTE |TESTE
"""

mime_multiepart = MIMEMultipart()
mime_multiepart["from"] = remetente
mime_multiepart["to"] = destinatario
mime_multiepart["subject"] = "assunto do email"

corpo_email = MIMEText(mensagem, "plain", "utf-8")
mime_multiepart.attach(corpo_email)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_user, smtp_passwd)
    server.send_message(mime_multiepart)
    print("email enviado com sucesso.")
