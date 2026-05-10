LARGURA = 50


# Função responsável por: linha
def linha():

    print("=" * LARGURA)


# Função responsável por: titulo
def titulo(texto):

    print()

    linha()

    print(texto.center(LARGURA))

    linha()


# Função responsável por: descricao
def descricao(texto):

    print(f"\n{texto}")


# Função responsável por: input_label
def input_label(texto):

    print(f"\n{texto}")

    return input("⟶ ")


# Função responsável por: sucesso
def sucesso(msg):

    print(f"\n✓ {msg}")


# Função responsável por: erro
def erro(msg):

    print(f"\n✕ {msg}")


# Função responsável por: aviso
def aviso(msg):

    print(f"\n⚠ {msg}")


# Função responsável por: separador
def separador():

    print("-" * LARGURA)