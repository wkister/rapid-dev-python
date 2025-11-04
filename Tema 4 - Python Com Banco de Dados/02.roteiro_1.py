import os
import sqlite3 as conector


def conectar_banco(nome_arquivo):
    """Conecta (ou cria) um arquivo SQLite no mesmo diretório do script.

    nome_arquivo: nome do arquivo do banco (ex.: 'ecommerce.db' ou './ecommerce.db').
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, os.path.basename(nome_arquivo))

    print(f"\nConectando ao banco: {db_path}\n")
    return conector.connect(db_path)


def criar_tabelas(conexao):
    cursor = conexao.cursor()
    try:
        # Criando a tabela Locais
        sql = """CREATE TABLE IF NOT EXISTS Locais (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nome TEXT NOT NULL,
                  endereco TEXT NOT NULL
              );
        """
        cursor.execute(sql)
        print("Tabela Locais criada\n")

        # Criando a tabela Eventos
        sql = """CREATE TABLE IF NOT EXISTS Eventos (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nome TEXT NOT NULL,
                  data TEXT NOT NULL,
                  local_id INTEGER NOT NULL,
                  FOREIGN KEY(local_id) REFERENCES Locais(id)
            );
        """
        cursor.execute(sql)
        print("Tabela Eventos criada.\n")

        # Criando a tabela Participantes
        sql = """CREATE TABLE IF NOT EXISTS Participantes (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nome TEXT NOT NULL,
                  email TEXT NOT NULL,
                  evento_id INTEGER NOT NULL,
                  FOREIGN KEY(evento_id) REFERENCES Eventos(id)
          );
        """
        cursor.execute(sql)
        print("Tabela Participantes criada\n")

        conexao.commit()

    except Exception as e:
        print("Erro ao criar as tabelas:", e)

    finally:
        cursor.close()


def popular_tabelas(conexao):
    cursor = conexao.cursor()
    try:
        locais = [
            ('Auditório A', 'Rua das Flores, 123'),
            ('Sala B', 'Av. Central, 456')
        ]

        eventos = [
            ('Palestra de Python', '2025-11-02', 1),
            ('Oficina de Git', '2025-11-03', 2)
        ]

        participantes = [
            ('Alice', 'alice@example.com', 1),
            ('Bob', 'bob@example.com', 2),
            ('Charlie', 'charlie@example.com', 1)
        ]

        # Evitar duplicatas: só popula se a respectiva tabela estiver vazia
        cursor.execute("SELECT COUNT(*) FROM Locais")
        if cursor.fetchone()[0] == 0:
            cursor.executemany("INSERT INTO Locais(nome, endereco) VALUES (?, ?);", locais)
            print("Locais inseridos")
        else:
            print("Locais já possuem dados — pulando inserção")

        cursor.execute("SELECT COUNT(*) FROM Eventos")
        if cursor.fetchone()[0] == 0:
            cursor.executemany("INSERT INTO Eventos(nome, data, local_id) VALUES (?, ?, ?);", eventos)
            print("Eventos inseridos")
        else:
            print("Eventos já possuem dados — pulando inserção")

        cursor.execute("SELECT COUNT(*) FROM Participantes")
        if cursor.fetchone()[0] == 0:
            cursor.executemany("INSERT INTO Participantes(nome, email, evento_id) VALUES (?, ?, ?);", participantes)
            print("Participantes inseridos")
        else:
            print("Participantes já possuem dados — pulando inserção")

        conexao.commit()
        print("Tabelas populadas com sucesso.\n")

    except Exception as e:
        print("Erro em popular as tabelas:", e)

    finally:
        cursor.close()


if __name__ == "__main__":
    print("Iniciando script")
    conexao = conectar_banco("ecommerce.db")

    print("Criando as tabelas")
    criar_tabelas(conexao)

    print("Populando as tabelas")
    popular_tabelas(conexao)

    conexao.close()
    print("Conexao encerrada")