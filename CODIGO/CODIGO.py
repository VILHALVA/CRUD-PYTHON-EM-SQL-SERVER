import pyodbc
from time import sleep

class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class GerenciadorUsuarios:
    def __init__(self):
        try:
            self.conexao = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};'
                'SERVER=DESKTOP-PK3RLSU;'  
                'DATABASE=Cadastro;'  
                'Trusted_Connection=yes;'  
            )
            self.cursor = self.conexao.cursor()
            print("Conexão ao banco de dados estabelecida.")
        except pyodbc.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def adicionar_usuario(self, nome, idade):
        try:
            sql = "INSERT INTO Usuarios (Nome, Idade) VALUES (?, ?)"
            val = (nome, idade)
            self.cursor.execute(sql, val)
            self.conexao.commit()
            print("😎 USUÁRIO ADICIONADO COM SUCESSO!")
        except pyodbc.Error as e:
            print(f"Erro ao adicionar usuário: {e}")

    def listar_usuarios(self):
        try:
            self.cursor.execute("SELECT * FROM Usuarios")
            usuarios = self.cursor.fetchall()

            if usuarios:
                print("=" * 100)
                print("LISTA DE USUÁRIOS:")
                print("-" * 100)
                for usuario in usuarios:
                    print("*" * 100)
                    print(f"NOME: {usuario.Nome}, IDADE: {usuario.Idade}")
                    print("*" * 100)
                print("=" * 100)
            else:
                print("😒 NENHUM USUÁRIO CADASTRADO.")
        except pyodbc.Error as e:
            print(f"Erro ao listar usuários: {e}")

    def atualizar_usuario(self, nome_antigo, novo_nome, nova_idade):
        try:
            sql = "UPDATE Usuarios SET Nome = ?, Idade = ? WHERE Nome = ?"
            val = (novo_nome, nova_idade, nome_antigo)
            self.cursor.execute(sql, val)
            self.conexao.commit()
            print("😙 USUÁRIO ATUALIZADO COM SUCESSO!")
        except pyodbc.Error as e:
            print(f"Erro ao atualizar usuário: {e}")

    def excluir_usuario(self, nome):
        try:
            sql = "DELETE FROM Usuarios WHERE Nome = ?"
            val = (nome,)
            self.cursor.execute(sql, val)
            self.conexao.commit()
            print("🗑 USUÁRIO EXCLUÍDO COM SUCESSO!")
        except pyodbc.Error as e:
            print(f"Erro ao excluir usuário: {e}")

def exibir_menu():
    print("\nMENU:")
    print("1. ADICIONAR USUÁRIO")
    print("2. LISTAR USUÁRIOS")
    print("3. ATUALIZAR USUÁRIO")
    print("4. EXCLUIR USUÁRIO")
    print("5. SAIR")

def main():
    gerenciador = GerenciadorUsuarios()

    while True:
        exibir_menu()
        opcao = input("😎 ESCOLHA UMA OPÇÃO:\n>>>")

        if opcao == "1":
            nome = input("😎 DIGITE O NOME:\n>>>")
            idade = int(input("😎 DIGITE A IDADE:\n>>>"))
            gerenciador.adicionar_usuario(nome, idade)
        elif opcao == "2":
            gerenciador.listar_usuarios()
        elif opcao == "3":
            nome_antigo = input("😎 DIGITE O NOME A SER ATUALIZADO:\n>>>")
            novo_nome = input("😎 DIGITE O NOVO NOME:\n>>>")
            nova_idade = int(input("😎 DIGITE A NOVA IDADE:\n>>>"))
            gerenciador.atualizar_usuario(nome_antigo, novo_nome, nova_idade)
        elif opcao == "4":
            nome = input("😎 DIGITE O NOME DO USUÁRIO A SER EXCLUÍDO:\n>>>")
            gerenciador.excluir_usuario(nome)
        elif opcao == "5":
            print("🚀 SAINDO...")
            sleep(3)
            break
        else:
            print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

if __name__ == "__main__":
    main()
