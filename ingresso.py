# Importa bibliotecas e funções usadas no sistema
from utils import (
    calcular_desconto,
    formatar_dinheiro,
    salvar_log
)

# Importa bibliotecas e funções usadas no sistema
from planos import planos

# Importa bibliotecas e funções usadas no sistema
from layout import (
    titulo,
    sucesso,
    erro
)


# Função responsável por: ingresso
def ingresso(usuario):

    titulo("INGRESSO")

    # SEM LOGIN
    if not usuario:

        erro("Faça login primeiro.")

        return

    # MENSALIDADE
    if not usuario["pago"]:

        erro(
            "Acesso negado. Mensalidade pendente."
        )

        return

    valor = 100

    valor_final = calcular_desconto(
        usuario["plano"],
        valor
    )

    plano_usuario = planos[
        usuario["plano"]
    ]

    sucesso("Ingresso liberado!")

    print(f"""
========== INGRESSO ==========

Nome: {usuario['nome']}

Email: {usuario['email']}

Clube: {usuario['clube']}

Plano: {plano_usuario['nome']}

Valor original:
{formatar_dinheiro(valor)}

Valor final:
{formatar_dinheiro(valor_final)}

==============================
""")

    salvar_log(
        f"Ingresso emitido para "
        f"{usuario['email']}"
    )