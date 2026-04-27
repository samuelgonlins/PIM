# ⚽ Sistema Sócio Torcedor

Projeto desenvolvido em Python com o objetivo de gerenciar sócios torcedores de clubes de futebol, permitindo cadastro, autenticação, controle de planos e compra de ingressos com desconto.

---

## 📌 Funcionalidades

* Cadastro de usuários com validação de dados
* Login com email e senha
* Criptografia de senha para maior segurança
* Sistema de planos:

  * Bronze
  * Prata
  * Ouro
  * Social
* Cálculo automático de descontos em ingressos
* Verificação de pagamento da mensalidade
* Sistema de administrador para visualização de usuários
* Geração automática de ID único para cada usuário

---

## 🧠 Regras do Sistema

* Apenas usuários com mensalidade em dia podem comprar ingressos
* O desconto varia conforme o plano escolhido
* Cada usuário possui um ID único gerado automaticamente
* Emails inválidos ou opções incorretas são rejeitados pelo sistema

---

## 🗂️ Estrutura do Projeto

```
pim_v2/
│
├── main.py            # Arquivo principal (inicia o sistema)
├── sistema.py         # Menu principal e navegação
├── cadastro.py        # Cadastro de usuários
├── login.py           # Autenticação de usuários
├── ingresso.py        # Compra de ingressos
├── admin.py           # Funções administrativas
├── seguranca.py       # Criptografia de senha
├── validacoes.py      # Validação de dados
├── utils.py           # Funções auxiliares
├── dados.py           # Manipulação de arquivos
│
└── dados/
    ├── usuarios.txt   # Armazena os usuários
    └── id.txt         # Controle de IDs
```

---

## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/samuelgonlins/PIM.git
```

2. Acesse a branch correta:

```bash
git checkout pim_v2
```

3. Entre na pasta do projeto:

```bash
cd pim_v2
```

4. Execute o sistema:

```bash
python main.py
```

---

## 🔐 Segurança

* As senhas são armazenadas de forma criptografada utilizando SHA-256
* O sistema evita entradas inválidas através de validações
* Dados sensíveis não são exibidos diretamente

---

## 👤 Sistema de Administrador

Usuários administradores possuem acesso a:

* Visualização de todos os usuários cadastrados
* Informações gerais do sistema

---

## 🛠️ Tecnologias Utilizadas

* Python
* Manipulação de arquivos `.txt`
* Biblioteca `hashlib` (criptografia)
* Expressões regulares (`re`) para validação

---

## 🚀 Possíveis Melhorias Futuras

* Uso de banco de dados (SQLite ou MySQL)
* Interface gráfica (Tkinter ou Web)
* Sistema de recuperação de senha
* Integração com envio de emails
* Uso de JSON para armazenamento de dados

---

## 📄 Autor(es)

Projeto desenvolvido por:

* Arthur Loss Karst
* Samuel Gonçalves
* Richard Willian Anadão de Assis
* Antonio Henrique totoli da silva

## 📌 Observação

Este projeto foi desenvolvido para fins acadêmicos (PIM), com foco em organização de código, boas práticas e aplicação de conceitos de programação em Python.
