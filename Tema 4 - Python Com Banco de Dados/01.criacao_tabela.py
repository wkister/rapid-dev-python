import os
import sqlite3 as conector


conexao = None
cursor = None

try:
    # Abertura da conexao (usar o diretório do script para o arquivo do DB)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, "meu_banco.db")
    conexao = conector.connect(db_path)

    # Criacao do cursor
    cursor = conexao.cursor()

    # Execucao dos comandos
    sql = '''CREATE TABLE Pessoa (
                cpf INTEGER NOT NULL,
                nome TEXT NOT NULL,
                nascimento DATE NOT NULL,
                oculos BOOLEAN NOT NULL,
                PRIMARY KEY (cpf)
            );
        '''

    cursor.execute(sql)

    sql = '''CREATE TABLE Marca (
                id INTEGER NOT NULL,
                nome TEXT NOT NULL,
                sigla CHARACTER(2) NOT NULL,
                PRIMARY KEY (id)
            );
        '''
    
    cursor.execute(sql)

    sql = '''CREATE TABLE Veiculo (
                placa CHARACTER(7) NOT NULL,
                ano INTEGER NOT NULL,
                cor TEXT NOT NULL,
                proprietario INTEGER NOT NULL,
                marca INTEGER NOT NULL,
                PRIMARY KEY (placa),
                FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
                FOREIGN KEY(marca) REFERENCES Marca(id)
            );
        '''
                
    cursor.execute(sql)

    # Adicionar a coluna motor em Veiculo
    sql = '''ALTER TABLE Veiculo
                 ADD motor REAL;
        '''

    cursor.execute(sql)

    # Efetivacao do comando (commit deve ser chamado na conexao, não no cursor)
    conexao.commit()
    
except conector.DatabaseError as err:
    print("Erro de banco de dados", err)
    
finally:
    # Fechamento das conexoes
    if cursor is not None:
        cursor.close()
    if conexao is not None:
        conexao.close()
