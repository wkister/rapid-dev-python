import psycopg2
from psycopg2 import Error
from faker import Faker

class AppBD:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.connect_to_db()

    def connect_to_db(self):
        try:
            self.conn = psycopg2.connect(
                database="meu-banco",
                user="meu-usuario",
                password="minha-senha-segura",
                host="127.0.0.1",
                port="5432"
            )

            self.cur = self.conn.cursor()

            print("Conexão com o Banco de Dados aberta com sucesso!")
        except (Exception, Error) as error:
            print("Falha ao se conectar ao Banco de Dados", error)

    def selecionar_dados(self):
        try:
            self.cur.execute("SELECT * FROM PRODUTO")
            registros = self.cur.fetchall()
            return registros
        except (Exception, Error) as error:
            print("Erro ao selecionar dados", error)
            return []

    def inserir_dados(self, nome, preco):
        try:
            self.cur.execute(
                '''INSERT INTO PRODUTO (NOME, PRECO) VALUES (%s, %s)''',
                (nome, preco)
            )
            self.conn.commit()
            print("Inserção realizada com sucesso!")
        except (Exception, Error) as error:
            print("Erro ao inserir dados", error)

    def atualizar_dados(self, codigo, nome, preco):
        try:
            self.cur.execute(
                '''UPDATE PRODUTO SET NOME = %s, PRECO = %s WHERE CODIGO = %s''',
                (nome, preco, codigo)
            )
            self.conn.commit()
            print("Atualização realizada com sucesso!")
        except (Exception, Error) as error:
            print("Erro ao atualizar dados", error)

    def excluir_dados(self, codigo):
        try:
            self.cur.execute(
                '''DELETE FROM PRODUTO WHERE CODIGO = %s''',
                (codigo,)
            )
            self.conn.commit()
            print("Exclusão realizada com sucesso!")
        except (Exception, Error) as error:
            print("Erro ao excluir dados", error)

if __name__ == "__main__":
    # Criando uma instância da classe e inserindo dados aleatórios
    app_bd = AppBD()
    fake = Faker('pt_BR')

    for _ in range(10):
        nome = fake.word()
        preco = round(fake.random_number(digits=5) / 100, 2)
        app_bd.inserir_dados(nome, preco)