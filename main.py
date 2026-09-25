import sqlite3

conexao = sqlite3.connect("usuarios.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
)
""")

conexao.commit()


while True:
    print("\n===== SISTEMA DE LOGIN =====")
    print("1 - Criar conta")
    print("2 - Fazer login")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        usuario = input("Digite seu usuário: ")
        senha = input("Digite sua senha: ")

        try:
            cursor.execute(
                "INSERT INTO usuarios (usuario, senha) VALUES (?, ?)",
                (usuario, senha)
            )

            conexao.commit()

            print("Conta criada com sucesso!")

        except sqlite3.IntegrityError:
            print("Esse usuário já existe!")

    elif opcao == "2":
        usuario = input("Digite seu usuário: ")
        senha = input("Digite sua senha: ")

        cursor.execute(
            "SELECT * FROM usuarios WHERE usuario = ? AND senha = ?",
            (usuario, senha)
        )

        resultado = cursor.fetchone()

        if resultado:
            print("Login realizado com sucesso!")
        else:
            print("Usuário ou senha incorretos!")

    elif opcao == "3":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")



conexao.close()