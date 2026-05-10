# Importa bibliotecas e funções usadas no sistema
import os


# Função responsável por: inicializar_dados
def inicializar_dados():

    # CRIA PASTA
    os.makedirs(
        "dados",
        exist_ok=True
    )

    arquivos = {

        "dados/id.txt": "1000",

        "dados/usuarios.txt": "",

        "dados/logs.txt": ""
    }

    for caminho, conteudo in arquivos.items():

        if not os.path.exists(caminho):

            with open(
                caminho,
                "w",
                encoding="utf-8"
            ) as f:

                f.write(conteudo)