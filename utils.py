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

def mostrar_plano():
    print("""
PLANOS DISPONÍVEIS:

B - Bronze ⟶ paga 80% do valor
P - Prata ⟶ paga 50% do valor
S - Social ⟶ paga 20% do valor
O - Ouro ⟶ não paga (VIP)
""")