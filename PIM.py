usuarios = []

def cadastro():
    
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    plano = input("Escolha: Bronze(B)/Prata(P)/Ouro(O)/Social(S): ").upper()
    clube = input("Digite o nome do clube: São Paulo(SP)/Flamengo(F)/Vasco(V)/Outro(O): ")
    pago = input("Mensalidade paga? (s/n): ").lower() == "s"

    usuario = {
        "nome": nome,
        "senha": senha,
        "plano": plano,
        "clube": clube,
        "pago": pago,
    }

    usuarios.append(usuario)

    print("Cadastro realizado com sucesso!")

    # gerar ID
    try:
        with open("id.txt", "r") as f:
            acm = int(f.read())
    except:
        acm = 1000

    acm += 1

    with open("id.txt", "w") as f:
        f.write(str(acm))

    #salvar usuário
    with open("usuarios.txt", "a") as f:
        usuario = usuarios[-1]
        f.write(f"{acm}, {usuario['nome']}, {usuario['senha']}, {usuario['plano']}, {usuario['clube']}, {usuario['pago']}\n")

    print("Usuário cadastrado com ID:", acm)
    try:
        with open("id.txt", "r") as f:
            acm = int(f.read())
    except:
        acm = 1000

    acm += 1

    with open("id.txt", "w") as f:
        f.write(str(acm))

def calcular_desconto(plano, valor):
    if plano == "O":
        return valor * 0
    elif plano == "S":
        return valor * 0.2
    elif plano == "P":
        return valor * 0.5
    elif plano == "B":
        return valor * 0.8
    else:
        return valor

def ingresso():
    nome = input("Digite seu nome: ")

    for usuario in usuarios:
        if usuario["nome"] == nome:

            if not usuario["pago"]:
                print("Acesso negado! Mensalidade em atraso.")
                return

            valor_base = 100

            valor_final = calcular_desconto(usuario["plano"], valor_base)
            desconto = valor_base - valor_final

            print("\n=== INGRESSO ===")
            print("Nome:", usuario["nome"])
            print("Clube:", usuario["clube"])
            print("Plano:", usuario["plano"])
            print("Valor original:", valor_base)
            print("Desconto:", desconto)
            print("Valor final:", valor_final)

            return

    print("Usuário não encontrado.")



def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for u in usuarios:
            print(u)

def sistema():
    while True:
        print("\n ==================================")
        print("Sistema de Sócio Torcedor")
        print("1 - Cadastro")
        print("2 - Comprar Ingresso")
        print("3 - Lista de usuários")
        print("4 - Sair")
        print("==================================")

        ops = input("Escolha uma opção: ")

        if ops == "1":
            cadastro()
        elif ops == "2":
            ingresso()
        elif ops == "3":
            listar_usuarios()
        elif ops == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

sistema()