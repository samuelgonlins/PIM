# Importa bibliotecas e funções usadas no sistema
from sistema import sistema
# Importa bibliotecas e funções usadas no sistema
from dados import inicializar_dados


# Função responsável por: main
def main():

    inicializar_dados()

    sistema()


# Inicia a execução principal do sistema
if __name__ == "__main__":

    main()