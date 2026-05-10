# Importa bibliotecas e funções usadas no sistema
from planos import planos
# Importa bibliotecas e funções usadas no sistema
from datetime import datetime


# Função responsável por: calcular_desconto
def calcular_desconto(plano, valor):

    plano = plano.upper()

    if plano in planos:

        desconto = planos[plano]["desconto"]

        return valor * (1 - desconto)

    return valor

# Função responsável por: mostrar_planos
def mostrar_planos():

    print("""
========================================
        PLANOS DISPONÍVEIS
========================================
""")

    # Percorre todos os planos
    for codigo, p in planos.items():

        desconto = int(p["desconto"] * 100)

        print(f"""
[{codigo}] PLANO {p['nome'].upper()}

{p['titulo']}

----------------------------------------
RESUMO
----------------------------------------
{p['resumo']}

----------------------------------------
VALOR MENSAL
----------------------------------------
R$ {p['preco']:.2f}

----------------------------------------
DESCONTO NO INGRESSO
----------------------------------------
{desconto}%

----------------------------------------
BENEFÍCIOS
----------------------------------------
""")

        # Mostra benefícios do plano
        for detalhe in p["detalhes"]:

            print(f"✔ {detalhe}")

        print(f"""

----------------------------------------
IMPACTO DO PLANO
----------------------------------------
{p['impacto']}

========================================
""")
# Função responsável por: salvar_log
def salvar_log(mensagem):

    with open(
        "dados/logs.txt",
        "a",
        encoding="utf-8"
    ) as f:

        f.write(
            f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] {mensagem}\n"
        )


# Função responsável por: formatar_dinheiro
def formatar_dinheiro(valor):

    return f"R$ {valor:.2f}"


# Função responsável por: linha
def linha():

    print("=" * 40)


# Função responsável por: limpar_tela
def limpar_tela():

    print("\n" * 5)