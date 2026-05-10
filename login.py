# Importa bibliotecas e funções usadas no sistema
from cadastro import usuarios
# Importa bibliotecas e funções usadas no sistema
from seguranca import criptografar_senha
# Importa bibliotecas e funções usadas no sistema
from layout import titulo, erro, sucesso
# Importa bibliotecas e funções usadas no sistema
from sessao import fazer_login
# Importa bibliotecas e funções usadas no sistema
from utils import salvar_log

# Função responsável por: login
def login():
    titulo("LOGIN")

    email = input("Digite seu email: ").strip().lower()
    senha = criptografar_senha(input("Digite sua senha: ").strip())

    for u in usuarios:

        if (
            u["email"].lower() == email
            and u["senha"] == senha
        ):

            sucesso("Login realizado com sucesso!")

            salvar_log(f"Login realizado: {email}")

            fazer_login(u)

            return u

    salvar_log(f"Tentativa inválida: {email}")

    erro("Credenciais inválidas.")

    return None