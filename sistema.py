from cadastro import cadastro, carregar_usuarios, garantir_admin
from login import login
from ingresso import ingresso
from admin import painel_admin
from layout import titulo

def sistema():
    carregar_usuarios()
    garantir_admin()

    usuario_logado = None

    while True:
        titulo("SISTEMA SÓCIO TORCEDOR")

        print("""
1 ⟶ Cadastro
2 ⟶ Login
3 ⟶ Comprar Ingresso
4 ⟶ Painel admin
5 ⟶ Sair
""")

        op = input("Escolha ⟶ ")

        if op == "1":
            cadastro()

        elif op == "2":
            usuario_logado = login()

        elif op == "3":
            ingresso(usuario_logado)

        elif op == "4":
            if usuario_logado and usuario_logado["admin"]:
                painel_admin()
            else:
                print("Acesso Negado.")

        elif op == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")