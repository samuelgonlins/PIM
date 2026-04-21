usuarios = []

def escolher_plano():
    while True:
        print("""
=== ESCOLHA UM PLANO ===

Um plano é como um tipo de assinatura que te dá desconto no ingresso.

B - Plano Bronze → você ganha 20% de desconto
P - Plano Prata → você ganha 50% de desconto
O - Plano Ouro → você não paga nada (100% de desconto)
S - Plano Social → você ganha 80% de desconto
""")
        plano = input("Digite a letra do plano desejado: ").upper()
        if plano in ["B", "P", "O", "S"]:
            return plano
        else:
            print("Não entendi sua escolha. Vamos tentar de novo 🙂")


def cadastro():
    print("\n=== CADASTRO DE USUÁRIO ===")
    print("Cadastro é o processo de criar sua conta no sistema.\n")

    nome = input("Digite seu nome: ").strip().lower()
    senha = input("Crie uma senha (guarde ela, você vai precisar depois): ")

    plano = escolher_plano()

    clube = input("\nDigite o nome do seu clube de futebol: ")

    pago = input("\nVocê já pagou a mensalidade? (s para sim / n para não): ").lower() == "s"

    try:
        with open("id.txt", "r") as f:
            acm = int(f.read())
    except:
        acm = 1000

    acm += 1

    with open("id.txt", "w") as f:
        f.write(str(acm))

    usuario = {
        "id": acm,
        "nome": nome,
        "senha": senha,
        "plano": plano,
        "clube": clube,
        "pago": pago,
    }

    usuarios.append(usuario)

    with open("usuarios.txt", "a") as f:
        u = usuarios[-1]
        f.write(f"{u['id']}, {u['nome']}, {u['senha']}, {u['plano']}, {u['clube']}, {u['pago']}\n")

    print("\nCadastro concluído com sucesso!")
    print(f"Seu número de identificação é: {acm}")
    print("Guarde esse número caso precise no futuro.\n")


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
    print("\n=== COMPRA DE INGRESSO ===")
    print("Aqui você pode comprar um ingresso para o jogo.\n")

    print("Para continuar, precisamos confirmar quem você é (isso se chama login).\n")

    nome = input("Digite seu nome: ").strip().lower()
    senha = input("Digite sua senha: ")

    for usuario in usuarios:
        if usuario["nome"] == nome and usuario["senha"] == senha:

            if not usuario["pago"]:
                print("\nVocê não pode comprar ingresso porque a mensalidade não foi paga.")
                return

            valor_base = 100
            valor_final = calcular_desconto(usuario["plano"], valor_base)
            desconto = valor_base - valor_final

            print("\n=== INGRESSO GERADO ===")
            print("Esse é o resumo da sua compra:\n")
            print("Seu ID:", usuario["id"])
            print("Nome:", usuario["nome"])
            print("Clube:", usuario["clube"])
            print("Plano escolhido:", usuario["plano"])
            print("Preço original do ingresso: R$", valor_base)
            print("Desconto aplicado: R$", desconto)
            print("Valor final a pagar: R$", valor_final)
            print("\nCompra realizada com sucesso! Bom jogo! ⚽")

            return

    print("\nNão encontramos seus dados. Verifique nome e senha.\n")


def listar_usuarios():
    print("\n=== LISTA DE USUÁRIOS CADASTRADOS ===")
    print("Aqui estão todas as pessoas que já criaram conta:\n")

    if not usuarios:
        print("Ainda não há usuários cadastrados.")
    else:
        for u in usuarios:
            print(f"ID: {u['id']} | Nome: {u['nome']} | Plano: {u['plano']} | Pago: {u['pago']}")


def sistema():
    while True:
        print("\n" + "="*50)
        print("BEM-VINDO AO SISTEMA DE SÓCIO TORCEDOR")
        print("="*50)

        print("""
Este sistema permite que você:
1 - Criar uma conta (cadastro)
2 - Comprar um ingresso
3 - Ver pessoas cadastradas
4 - Sair do sistema
""")

        ops = input("Digite o número da opção que você deseja: ")

        if ops == "1":
            cadastro()
        elif ops == "2":
            ingresso()
        elif ops == "3":
            listar_usuarios()
        elif ops == "4":
            print("\nVocê saiu do sistema. Até a próxima!")
            break
        else:
            print("\nNão entendi essa opção. Vamos tentar novamente.\n")


sistema()