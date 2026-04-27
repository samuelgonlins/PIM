import os

def inicializar_dados():
    # cria a pasta se não existir
    os.makedirs("dados", exist_ok=True)

    # cria id.txt se não existir
    if not os.path.exists("dados/id.txt"):
        with open("dados/id.txt", "w") as f:
            f.write("1000")

    # cria usuarios.txt se não existir
    if not os.path.exists("dados/usuarios.txt"):
        with open("dados/usuarios.txt", "w") as f:
            pass