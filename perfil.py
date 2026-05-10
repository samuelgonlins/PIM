# Importa bibliotecas e funções usadas no sistema
from layout import titulo

# Importa os planos cadastrados
from planos import planos


# Função responsável por: ver_perfil
def ver_perfil(usuario):

    # Mostra título da tela
    titulo("PERFIL")

    # Pega informações do plano do usuário
    plano = planos[usuario["plano"]]

    # Exibe dados do usuário
    print(f"""
Nome: {usuario['nome']}

Email: {usuario['email']}

Plano: {plano['nome']}

Clube: {usuario['clube']}

Mensalidade paga:
{usuario['pago']}

Admin:
{usuario['admin']}

======== BENEFÍCIOS ========
""")

    # Mostra benefícios do plano
    for beneficio in plano["detalhes"]:

        print(f"✔ {beneficio}")

    print("""
============================
""")