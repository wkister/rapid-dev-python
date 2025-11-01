import sqlite3 as conector
import os

def conectar_banco(nome_banco):
    """Conecta (ou cria) um banco SQLite no mesmo diretório do script.

    Parâmetros:
        nome_banco (str): nome do arquivo do banco. Atualmente a função
            ignora este argumento e sempre usa 'meu_banco.db' no diretório do
            script.

    Retorno:
        sqlite3.Connection: objeto de conexão com o banco SQLite.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, "meu_banco.db")

    print(f"\nConectando ao banco '{db_path}'\n")
    
    return conector.connect(db_path)

def criar_tabelas(conexao):
    cursor = conexao.cursor()

    print("Criando a tabela Locais\n")
   
    cursor.execute('''CREATE TABLE IF NOT EXISTS Locais (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nome TEXT NOT NULL,
                      endereco TEXT NOT NULL)''')
   
    print("Criando a tabela Eventos\n")

    cursor.execute('''CREATE TABLE IF NOT EXISTS Eventos (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nome TEXT NOT NULL,
                      data TEXT NOT NULL,
                      local_id INTEGER NOT NULL,
                      FOREIGN KEY(local_id) REFERENCES Locais(id))''')
    
    print("Criando a tabela Participantes\n")
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Participantes (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nome TEXT NOT NULL,
                      email TEXT NOT NULL,
                      evento_id INTEGER NOT NULL,
                      FOREIGN KEY(evento_id) REFERENCES Eventos(id))''')
   
    conexao.commit()

if __name__ == '__main__':
    conexao = conectar_banco('eventos.db')
    criar_tabelas(conexao)
    conexao.close()
