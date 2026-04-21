# ================================================
#   SISTEMA DE SÓCIO TORCEDOR - Versão Corrigida
#   Clubes: Flamengo, Corinthians e Palmeiras
# ================================================

usuarios = []

# ====================== FUNÇÕES ======================

def calcular_valor_final(plano, valor_base):
    """Calcula o valor final com desconto baseado no plano"""
    descontos = {
        "ouro": 1.00,    # Sem desconto
        "prata": 0.80,   # 20% de desconto
        "bronze": 0.60,  # 40% de desconto
        "social": 0.40   # 60% de desconto
    }
    return round(valor_base * descontos.get(plano, 1.0), 2)


def cadastrar():
    """Função para cadastrar novo sócio torcedor"""
    print("\n" + "="*50)
    print("           CADASTRO DE NOVO SÓCIO")
    print("="*50)

    nome = input("Nome completo: ").strip()
    if not nome:
        print("❌ Erro: O nome não pode estar vazio!")
        return

    clube = input("Clube (Flamengo/Corinthians/Palmeiras): ").lower().strip()
    if clube not in ["flamengo", "corinthians", "palmeiras"]:
        print("❌ Erro: Clube inválido! Use apenas Flamengo, Corinthians ou Palmeiras.")
        return

    plano = input("Plano (ouro/prata/bronze/social): ").lower().strip()
    if plano not in ["ouro", "prata", "bronze", "social"]:
        print("❌ Erro: Plano inválido! Escolha entre ouro, prata, bronze ou social.")
        return

    pago = input("Mensalidade paga? (s/n): ").lower().strip()
    if pago not in ["s", "n"]:
        print("❌ Erro: Responda apenas com 's' ou 'n'.")
        return

    # Cria o usuário
    usuario = {
        "nome": nome,
        "clube": clube,
        "plano": plano,
        "pago": pago
    }

    usuarios.append(usuario)

    # Mostra o resumo do cadastro (correção principal)
    print("\n" + "="*50)
    print("✅ CADASTRO REALIZADO COM SUCESSO!")
    print("="*50)
    print(f"Nome           : {nome}")
    print(f"Clube          : {clube.capitalize()}")
    print(f"Plano          : {plano.capitalize()}")
    print(f"Mensalidade    : {'✅ Paga' if pago == 's' else '❌ Atrasada'}")
    print("="*50)
    print()


def comprar_ingresso():
    """Função para comprar ingresso com verificação de pagamento"""
    if not usuarios:
        print("❌ Nenhum sócio cadastrado ainda!")
        return

    nome = input("\nDigite seu nome completo: ").strip()

    for usuario in usuarios:
        if usuario["nome"].lower() == nome.lower():
            
            # Verifica se a mensalidade está paga
            if usuario["pago"] != "s":
                print("❌ Acesso negado! Sua mensalidade está atrasada.")
                return

            # Define valor base por clube
            valores_clube = {
                "flamengo": 120,
                "corinthians": 100,
                "palmeiras": 110
            }
            valor_base = valores_clube.get(usuario["clube"], 100)

            # Calcula valor final com desconto
            valor_final = calcular_valor_final(usuario["plano"], valor_base)

            print("\n" + "="*50)
            print("🎟️  INGRESSO LIBERADO!")
            print("="*50)
            print(f"Clube     : {usuario['clube'].capitalize()}")
            print(f"Plano     : {usuario['plano'].capitalize()}")
            print(f"Valor base: R$ {valor_base:.2f}")
            print(f"Desconto  : {usuario['plano'].capitalize()}")
            print(f"Valor final: R$ {valor_final:.2f}")
            print("="*50)
            print("✅ Bom jogo!")
            return

    print("❌ Usuário não encontrado!")


def listar_usuarios():
    """Lista todos os sócios cadastrados de forma organizada"""
    if not usuarios:
        print("\nNenhum sócio cadastrado ainda.")
        return

    print("\n" + "="*70)
    print(f"{'NOME':<30} {'CLUBE':<15} {'PLANO':<10} {'MENSALIDADE'}")
    print("="*70)

    for u in usuarios:
        status = "✅ Paga" if u["pago"] == "s" else "❌ Atrasada"
        print(f"{u['nome']:<30} {u['clube'].capitalize():<15} {u['plano'].capitalize():<10} {status}")

    print("="*70)
    print(f"Total de sócios: {len(usuarios)}")
    print()


# ====================== MENU PRINCIPAL ======================

def sistema():
    while True:
        print("\n" + "═"*55)
        print("       SISTEMA DE SÓCIO TORCEDOR")
        print("═"*55)
        print("1 - Cadastrar novo sócio")
        print("2 - Comprar ingresso")
        print("3 - Listar todos os sócios")
        print("0 - Sair")
        print("═"*55)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            comprar_ingresso()
        elif opcao == "3":
            listar_usuarios()
        elif opcao == "0":
            print("\n👋 Encerrando o sistema... Até a próxima!")
            break
        else:
            print("❌ Opção inválida! Digite um número entre 0 e 3.")


# ====================== EXECUÇÃO ======================
if __name__ == "__main__":
    print("Bem-vindo ao Sistema de Sócio Torcedor!")
    sistema()