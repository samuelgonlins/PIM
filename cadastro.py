from seguranca import criptografar_senha
from validacoes import email_valido, escolher_plano, confirmar_pagamento, escolher_clube
from utils import mostrar_plano
from layout import titulo, descricao, input_label, sucesso, erro

usuarios = []

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


def salvar_usuario(usuario, user_id):
    with open("dados/usuarios.txt", "a") as f:
        f.write(f"{user_id},{usuario['email']},{usuario['senha']},{usuario['plano']},{usuario['clube']},{str(usuario['pago'])},{str(usuario['admin'])}\n")


def carregar_usuarios():
    try:
        with open("dados/usuarios.txt", "r") as f:
            for linha in f:
                dados = [d.strip() for d in linha.strip().split(",")]

                usuarios.append({
                    "id": int(dados[0]),
                    "email": dados[1],
                    "senha": dados[2],
                    "plano": dados[3],
                    "clube": dados[4],
                    "pago": dados[5].lower() == "true",
                    "admin": dados[6].lower() == "true"
                })
    except:
        pass


def garantir_admin():
    for u in usuarios:
        if u.get("admin"):
            return

    admin = {
        "id": 0,
        "email": "admin@admin.com",
        "senha": criptografar_senha("admin123"),
        "plano": "O",
        "clube": "Sistema",
        "pago": True,
        "admin": True
    }

    usuarios.append(admin)


def cadastro():
    titulo("CADASTRO")
    descricao("Crie sua conta preenchendo os dados abaixo.")

    while True:
        email = input_label("Digite seu email:")
        if email_valido(email):
            break
        erro("Email inválido.")

    senha = criptografar_senha(input_label("Crie uma senha:"))

    descricao("Escolha um plano:")
    mostrar_plano()
    plano = escolher_plano()

    descricao("Escolha seu clube:")
    clube = escolher_clube()

    pago = confirmar_pagamento()

    usuario = {
        "email": email,
        "senha": senha,
        "plano": plano,
        "clube": clube,
        "pago": pago,
        "admin": False
    }

    usuarios.append(usuario)

    user_id = gerar_id()
    salvar_usuario(usuario, user_id)

    sucesso(f"Cadastro realizado! ID: {user_id}")