# Importa bibliotecas e funções usadas no sistema
from seguranca import criptografar_senha

# Importa bibliotecas e funções usadas no sistema
from validacoes import (
    email_valido,
    escolher_plano,
    confirmar_pagamento,
    escolher_clube
)

# Importa bibliotecas e funções usadas no sistema
from utils import (
    mostrar_planos,
    salvar_log
)

# Importa bibliotecas e funções usadas no sistema
from layout import (
    titulo,
    descricao,
    input_label,
    sucesso,
    erro
)

usuarios = []


# Função responsável por: gerar_id
def gerar_id():

    try:

        with open("dados/id.txt", "r") as f:

            acm = int(f.read())

    except:

        acm = 1000

    acm += 1

    with open("dados/id.txt", "w") as f:

        f.write(str(acm))

    return acm


# Função responsável por: salvar_usuario
def salvar_usuario(usuario):

    with open(
        "dados/usuarios.txt",
        "a",
        encoding="utf-8"
    ) as f:

        f.write(
            f"{usuario['id']},"
            f"{usuario['nome']},"
            f"{usuario['email']},"
            f"{usuario['senha']},"
            f"{usuario['plano']},"
            f"{usuario['clube']},"
            f"{usuario['pago']},"
            f"{usuario['admin']}\n"
        )


# Função responsável por: carregar_usuarios
def carregar_usuarios():

    usuarios.clear()

    try:

        with open(
            "dados/usuarios.txt",
            "r",
            encoding="utf-8"
        ) as f:

            for linha in f:

                dados = [
                    d.strip()
                    for d in linha.strip().split(",")
                ]

                usuarios.append({

                    "id": int(dados[0]),

                    "nome": dados[1],

                    "email": dados[2],

                    "senha": dados[3],

                    "plano": dados[4],

                    "clube": dados[5],

                    "pago":
                        dados[6].lower() == "true",

                    "admin":
                        dados[7].lower() == "true"
                })

    except:

        pass


# Função responsável por: email_existente
def email_existente(email):

    for u in usuarios:

        if u["email"].lower() == email.lower():

            return True

    return False


# Função responsável por: garantir_admin
def garantir_admin():

    for u in usuarios:

        if u.get("admin"):

            return

    admin = {

        "id": 0,

        "nome": "Administrador",

        "email": "admin@admin.com",

        "senha":
            criptografar_senha("admin123"),

        "plano": "O",

        "clube": "Sistema",

        "pago": True,

        "admin": True
    }

    usuarios.append(admin)


# Função responsável por: cadastro
def cadastro():

    titulo("CADASTRO")

    descricao(
        "Crie sua conta preenchendo os dados abaixo."
    )

    nome = input_label(
        "Digite seu nome: ex: Matheus Kotaki"
    ).title().strip()

    # EMAIL
    while True:

        email = input_label(
            "Digite seu email: ex: matheus.kotaki@email.com"
        ).lower().strip()

        if not email_valido(email):

            erro("Email inválido.")
            continue

        if email_existente(email):

            erro("Email já cadastrado.")
            continue

        break

    # SENHA
    while True:

        senha = input_label(
            "Crie uma senha: mínimo 6 caracteres"
        )

        if len(senha) < 6:

            erro(
                "Senha muito curta."
            )

        else:

            senha = criptografar_senha(senha)

            break

    # PLANOS
    descricao("Escolha um plano:")

    mostrar_planos()

    plano = escolher_plano()

    # CLUBE
    descricao("Escolha seu clube:")

    clube = escolher_clube()

    # PAGAMENTO
    pago = confirmar_pagamento()

    # ID
    user_id = gerar_id()

    usuario = {

        "id": user_id,

        "nome": nome,

        "email": email,

        "senha": senha,

        "plano": plano,

        "clube": clube,

        "pago": pago,

        "admin": False
    }

    usuarios.append(usuario)

    salvar_usuario(usuario)

    salvar_log(
        f"Novo cadastro: {email}"
    )

    sucesso(
        f"Cadastro realizado! ID: {user_id}"
    )