_usuario_logado = None

# Função responsável por: fazer_login
def fazer_login(usuario):
    global _usuario_logado
    _usuario_logado = usuario

# Função responsável por: fazer_logout
def fazer_logout():
    global _usuario_logado
    _usuario_logado = None

# Função responsável por: usuario_logado
def usuario_logado():
    return _usuario_logado