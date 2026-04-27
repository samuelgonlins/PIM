import re

def email_valido(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


def escolher_plano():
    while True:
        plano = input("Plano [B/P/O/S]: ").upper()
        if plano in ["B", "P", "O", "S"]:
            return plano
        print("Opção inválida.")


def confirmar_pagamento():
    while True:
        op = input("Mensalidade paga? [s/n]: ").lower()
        if op in ["s", "n"]:
            return op == "s"
        print("Digite apenas s ou n.")


def escolher_clube():
    clubes = {
        "SP": "São Paulo",
        "FLA": "Flamengo",
        "PAL": "Palmeiras",
        "COR": "Corinthians",
        "VA": "Vasco",
        "SAN": "Santos",
        "INT": "Internacional",
        "GRE": "Grêmio",
        "O": "Outro"
    }

    while True:
        print("""
Escolha seu clube:
SP ⟶ São Paulo
FLA ⟶ Flamengo
PAL ⟶ Palmeiras
COR ⟶ Corinthians
VA  ⟶ Vasco
SAN ⟶ Santos
INT ⟶ Internacional
GRE ⟶ Grêmio
O   ⟶ Outro
""")

        escolha = input("Digite a opção: ").upper()

        if escolha in clubes:
            if escolha == "O":
                return input("Digite o nome do clube: ")
            return clubes[escolha]

        print("Opção inválida.")