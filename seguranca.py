# Importa bibliotecas e funções usadas no sistema
import hashlib


# Função responsável por: criptografar_senha
def criptografar_senha(senha):

    senha_bytes = senha.encode()

    hash_senha = hashlib.sha256(
        senha_bytes
    ).hexdigest()

    return hash_senha