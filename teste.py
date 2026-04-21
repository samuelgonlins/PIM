# gerar ID
try:
    with open("id.txt", "r") as f:
        acm = int(f.read())
except:
    acm = 1000

acm += 1

with open("id.txt", "w") as f:
    f.write(str(acm))

# dados do usuário
nome = input("Nome: ")
senha = input("Senha: ")

# salvar no arquivo
with open("usuarios.txt", "a") as f:
    f.write(f"{acm},{nome},{senha}\n")

print("Usuário cadastrado com ID:", acm)# gerar ID
try:
    with open("id.txt", "r") as f:
        acm = int(f.read())
except:
    acm = 1000

acm += 1

with open("id.txt", "w") as f:
    f.write(str(acm))

# dados do usuário
nome = input("Nome: ")
senha = input("Senha: ")

# salvar no arquivo
with open("usuarios.txt", "a") as f:
    f.write(f"{acm},{nome},{senha}\n")

print("Usuário cadastrado com ID:", acm)