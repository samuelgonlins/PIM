def titulo(texto):
    print("\n" + "=" * 40)
    print(texto.center(40))
    print("=" * 40)

def descricao(texto):
    print("\n" + texto)

def input_label(texto):
    print(texto)
    return input("⟶ ")

def sucesso(msg):
    print(f"\n✓ {msg}")

def erro(msg):
    print(f"\n✕ {msg}")

def aviso(msg):
    print(f"\n⚠ {msg}")