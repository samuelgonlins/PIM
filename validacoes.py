# Importa bibliotecas e funções usadas no sistema
import re

# Importa bibliotecas e funções usadas no sistema
from planos import planos


# Função responsável por: email_valido
def email_valido(email):

    return re.match(
        r"[^@]+@[^@]+\.[^@]+",
        email
    )


# Função responsável por: escolher_plano
def escolher_plano():

    while True:

        print("\nPlanos disponíveis:")

        for codigo, p in planos.items():

            print(f"""
[{codigo}] {p['nome']}
{p['titulo']}
""")

        plano = input(
            "\nEscolha o plano: "
        ).upper().strip()

        if plano in planos:
            return plano

        print("Opção inválida.")


# Função responsável por: confirmar_pagamento
def confirmar_pagamento():

    while True:

        print("""
========================================
        CONFIRMAÇÃO DE PAGAMENTO
========================================
""")

        op = input(
            "Pagamento realizado com sucesso? [s/n]: "
        ).lower().strip()

        if op in ["s", "n"]:

            return op == "s"

        print("""
Opção inválida.
Digite apenas s ou n.
""")


# Função responsável por: escolher_clube
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
========== CLUBES DISPONÍVEIS ==========

SP  ⟶ São Paulo
FLA ⟶ Flamengo
PAL ⟶ Palmeiras
COR ⟶ Corinthians
VA  ⟶ Vasco
SAN ⟶ Santos
INT ⟶ Internacional
GRE ⟶ Grêmio
O   ⟶ Outro

========================================
""")

        escolha = input(
            "Digite a opção: "
        ).upper().strip()

        if escolha in clubes:

            if escolha == "O":

                clube = input(
                    "Digite o nome do clube: "
                )

                return clube.title()

            return clubes[escolha]

        print("Opção inválida.")