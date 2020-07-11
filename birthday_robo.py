
import smtplib  # Email
import getpass  # password
from datetime import datetime as dt  # to get date


def manda_email(destino, assunto, mensagem):
    endereco_email = "vandroots86@gmail.com"
    senha_email = getpass.getpass("Digite sua senha para continuar> ")

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(endereco_email, senha_email)

    assunto = "Curso Python Fundamentos"
    conteudo = "Email enviado com Python <3"

    mensagem = f"Subject: {assunto}\n\n{conteudo}"

    smtp.sendmail(endereco_email, endereco_email, mensagem)


aniversarios = [
    {"nome": "Barbara", "data": "20/11/1988",
        "email": "babiclegama@gmail.com"},
    {"nome": "Sendy", "data": "22/01/2009",
        "email": "vandroots@icloud.com.br"},
]

for aniversario in aniversarios:
    data_atual = dt.today().date()
    data_aniversario = dt.strptime(aniversario["data"], "%d/%m/%Y").date()

    if(data_atual == data_aniversario):
        assunto = "Feliz aniversário!"
        mensagem = "Feliz aniversário " + \
            aniversario["nome"] + \
            "! Que todos seus sonhos se realize, Muitos anos de vida!"

        manda_email(aniversario["email"], assunto, mensagem)
