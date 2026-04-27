from cadastro import usuarios
from layout import titulo

def painel_admin():
    titulo("PAINEL ADMIN")

    for u in usuarios:
        print(f"""
Email: {u['email']}
Plano: {u['plano']}
Clube: {u['clube']}
Pago: {u['pago']}
Admin: {u['admin']}
-------------------------
""")