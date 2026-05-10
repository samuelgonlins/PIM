# Importa bibliotecas e funções usadas no sistema
from cadastro import usuarios

# Importa bibliotecas e funções usadas no sistema
from layout import titulo, erro, sucesso

# Importa bibliotecas e funções usadas no sistema
from utils import salvar_log


# Função responsável por: painel_admin
def painel_admin():

    while True:

        titulo("PAINEL ADMIN")

        print("1 - Listar usuários")
        print("2 - Procurar usuário")
        print("3 - Remover usuário")
        print("4 - Ver total de usuários")
        print("5 - Ver admins")
        print("6 - Ver total por clube")
        print("7 - Ver pagamentos pendentes")
        print("8 - Ver usuários por plano")
        print("9 - Tornar usuário admin")
        print("0 - Voltar")

        op = input("\nEscolha: ")

        # LISTAR USUÁRIOS
        if op == "1":

            if not usuarios:

                erro("Nenhum usuário cadastrado.")
                continue

            for i, u in enumerate(usuarios, start=1):

                print(f"""
========== USUÁRIO {i} ==========

ID: {u['id']}

Nome: {u['nome']}
Email: {u['email']}
Plano: {u['plano']}
Clube: {u['clube']}
Pago: {u['pago']}
Admin: {u['admin']}

================================
""")

        # PROCURAR USUÁRIO
        elif op == "2":

            email = input(
                "Digite o email: "
            ).strip().lower()

            encontrado = False

            for u in usuarios:

                if u["email"].lower() == email:

                    encontrado = True

                    print(f"""
===== USUÁRIO ENCONTRADO =====

ID: {u['id']}

Nome: {u['nome']}
Email: {u['email']}
Plano: {u['plano']}
Clube: {u['clube']}
Pago: {u['pago']}
Admin: {u['admin']}

==============================
""")

            if not encontrado:

                erro("Usuário não encontrado.")

        # REMOVER USUÁRIO
        elif op == "3":

            email = input(
                "Email do usuário: "
            ).strip().lower()

            for u in usuarios:

                if u["email"].lower() == email:

                    confirmar = input(
                        "Tem certeza? [s/n]: "
                    ).lower()

                    if confirmar == "s":

                        usuarios.remove(u)

                        salvar_log(
                            f"Usuário removido: {email}"
                        )

                        sucesso("Usuário removido.")

                        break

            else:

                erro("Usuário não encontrado.")

        # TOTAL DE USUÁRIOS
        elif op == "4":

            print(f"""
================================

Total de usuários:
{len(usuarios)}

================================
""")

        # LISTAR ADMINS
        elif op == "5":

            encontrou_admin = False

            print("""
========== ADMINS ==========
""")

            for u in usuarios:

                if u["admin"]:

                    encontrou_admin = True

                    print(f"""
Nome: {u['nome']}
Email: {u['email']}
""")

            if not encontrou_admin:

                erro("Nenhum admin encontrado.")

        # TOTAL DE MEMBROS POR CLUBE
        elif op == "6":

            clubes = {}

            for u in usuarios:

                clube = u["clube"]

                if clube in clubes:

                    clubes[clube] += 1

                else:

                    clubes[clube] = 1

            print("""
===== TOTAL POR CLUBE =====
""")

            for clube, total in clubes.items():

                print(
                    f"{clube}: {total} membro(s)"
                )

        # PAGAMENTOS PENDENTES
        elif op == "7":

            encontrou = False

            print("""
===== PAGAMENTOS PENDENTES =====
""")

            for u in usuarios:

                if not u["pago"]:

                    encontrou = True

                    print(f"""
Nome: {u['nome']}
Email: {u['email']}
Plano: {u['plano']}
""")

            if not encontrou:

                sucesso(
                    "Todos os usuários estão com pagamento em dia."
                )

        # USUÁRIOS POR PLANO
        elif op == "8":

            planos_total = {}

            for u in usuarios:

                plano = u["plano"]

                if plano in planos_total:

                    planos_total[plano] += 1

                else:

                    planos_total[plano] = 1

            print("""
===== USUÁRIOS POR PLANO =====
""")

            for plano, total in planos_total.items():

                print(
                    f"Plano {plano}: {total} usuário(s)"
                )

        # PROMOVER USUÁRIO PARA ADMIN
        elif op == "9":

            email = input(
                "Digite o email do usuário: "
            ).lower().strip()

            encontrado = False

            for u in usuarios:

                if u["email"].lower() == email:

                    encontrado = True

                    u["admin"] = True

                    salvar_log(
                        f"Novo admin: {email}"
                    )

                    sucesso(
                        "Usuário promovido para admin."
                    )

            if not encontrado:

                erro("Usuário não encontrado.")

        # VOLTAR
        elif op == "0":

            break

        # OPÇÃO INVÁLIDA
        else:

            erro("Opção inválida.")