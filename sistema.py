# Importa bibliotecas e funções usadas no sistema
from cadastro import cadastro, carregar_usuarios, garantir_admin
# Importa bibliotecas e funções usadas no sistema
from login import login
# Importa bibliotecas e funções usadas no sistema
from ingresso import ingresso
# Importa bibliotecas e funções usadas no sistema
from admin import painel_admin
# Importa bibliotecas e funções usadas no sistema
from perfil import ver_perfil

# Importa bibliotecas e funções usadas no sistema
from layout import titulo

# Importa bibliotecas e funções usadas no sistema
from sessao import (
    usuario_logado,
    fazer_logout
)

# Função responsável por: sistema
def sistema():

    carregar_usuarios()
    garantir_admin()

    while True:

        usuario = usuario_logado()

        titulo("SISTEMA SÓCIO TORCEDOR")

        # MENU SEM LOGIN
        if usuario is None:

            print("""
1 ⟶ Cadastro
2 ⟶ Login
0 ⟶ Sair
""")

            op = input("Escolha ⟶ ")

            if op == "1":
                cadastro()

            elif op == "2":
                login()

            elif op == "0":
                print("Saindo...")
                break

            else:
                print("Opção inválida.")

        # MENU COM LOGIN
        else:

            print(f"""
Bem-vindo, {usuario['nome']}!
""")

            print("""
1 ⟶ Ver Perfil
2 ⟶ Comprar Ingresso
3 ⟶ Logout
""")

            # MENU ADMIN
            if usuario["admin"]:
                print("4 ⟶ Painel admin")

            op = input("Escolha ⟶ ")

            if op == "1":
                ver_perfil(usuario)

            elif op == "2":
                ingresso(usuario)

            elif op == "3":

                fazer_logout()

                print("""
Logout realizado com sucesso.
""")

            elif op == "4" and usuario["admin"]:
                painel_admin()

            else:
                print("Opção inválida.")