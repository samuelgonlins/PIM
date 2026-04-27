def calcular_desconto(plano, valor):
    if plano == "O":
        return 0
    elif plano == "S":
        return valor * 0.2
    elif plano == "P":
        return valor * 0.5
    elif plano == "B":
        return valor * 0.8
    return valor


def ingresso(usuario):
    if not usuario:
        print("Faça login primeiro.")
        return

    if not usuario["pago"]:
        print("Acesso Negado. Mensalidade pendente.")
        return

    valor = 100
    final = calcular_desconto(usuario["plano"], valor)

    print("\n=== INGRESSO ===")
    print("Email:", usuario["email"])
    print("Clube:", usuario["clube"])
    print("Plano:", usuario["plano"])
    print("Valor final:", final)