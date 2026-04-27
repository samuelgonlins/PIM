from cadastro import usuarios
from seguranca import criptografar_senha
from layout import titulo, erro, sucesso

def login():
    titulo("LOGIN")

    email = input("Digite seu email: ")
    senha = criptografar_senha(input("Digite sua senha: "))

    for u in usuarios:
        if u["email"] == email and u["senha"] == senha:
            sucesso("Login realizado com sucesso!")
            return u

    erro("Credenciais inválidas.")
    return None