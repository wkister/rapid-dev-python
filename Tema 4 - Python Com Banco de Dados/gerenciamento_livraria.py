"""Gerenciamento simples de livraria (SQLite).

Este módulo fornece classes leves (Livro, Cliente, Pedido) e
funções para criar um banco SQLite local, popular com dados de
exemplo e exibir pedidos.

O arquivo é intencionalmente simples: usa caminhos relativos ao
arquivo (__file__) para criar o banco na mesma pasta do script.
"""

import os
import sqlite3
from typing import Optional


class Livro:
    """Representa um livro."""

    def __init__(self, titulo: str, autor: str, preco: float) -> None:
        self.titulo = titulo
        self.autor = autor
        self.preco = preco

    def __repr__(self) -> str:  # útil para depuração
        return f"Livro(titulo={self.titulo!r}, autor={self.autor!r}, preco={self.preco!r})"
        
class Cliente:
    """Representa um cliente."""

    def __init__(self, nome: str, email: str) -> None:
        self.nome = nome
        self.email = email

    def __repr__(self) -> str:
        return f"Cliente(nome={self.nome!r}, email={self.email!r})"
        
class Pedido:
    """Representa um pedido (referencia IDs de Cliente e Livro)."""

    def __init__(self, cliente_id: int, livro_id: int, quantidade: int, data_pedido: str) -> None:
        self.cliente_id = cliente_id
        self.livro_id = livro_id
        self.quantidade = quantidade
        self.data_pedido = data_pedido

    def __repr__(self) -> str:
        return (
            f"Pedido(cliente_id={self.cliente_id!r}, livro_id={self.livro_id!r}, "
            f"quantidade={self.quantidade!r}, data_pedido={self.data_pedido!r})"
        )


def conectar_banco(nome_banco: str) -> sqlite3.Connection:
    """Conecta (ou cria) um banco de dados SQLite localizado na mesma pasta do script.

    Args:
        nome_banco: nome do arquivo de banco (ex: 'livraria.db')

    Returns:
        sqlite3.Connection conectado ao arquivo especificado.
    """

    script_dir_path = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir_path, nome_banco)
    conexao = sqlite3.connect(db_path)
    return conexao
    
def criar_tabelas(conexao: sqlite3.Connection) -> None:
    """Cria as tabelas necessárias (se não existirem)."""

    cursor = conexao.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            preco REAL NOT NULL
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            livro_id INTEGER NOT NULL,
            quantidade INTEGER NOT NULL,
            data_pedido TEXT NOT NULL,
            FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
            FOREIGN KEY (livro_id) REFERENCES Livros(id)
        )
        """
    )

    conexao.commit()
    
def inserir_dados(conexao: sqlite3.Connection) -> None:
    """Insere dados de exemplo — não duplica se já existirem registros."""

    cursor = conexao.cursor()

    # dados de exemplo
    livros = [
        Livro("Python para Iniciantes", "John Doe", 39.99),
        Livro("Algoritmos e Estruturas de Dados", "Jane Smith", 49.99),
        Livro("Inteligência Artificial", "Alan Turing", 59.99),
    ]

    clientes = [
        Cliente("Alice", "alice@example.com"),
        Cliente("Bob", "bob@example.com"),
        Cliente("Charlie", "charlie@example.com"),
    ]

    pedidos = [
        Pedido(1, 1, 2, "2023-06-15"),
        Pedido(2, 2, 1, "2023-06-16"),
        Pedido(3, 3, 3, "2023-06-17"),
    ]

    # Inserir somente se as tabelas estiverem vazias (idempotente)
    cursor.execute("SELECT COUNT(*) FROM Livros")
    livros_count = cursor.fetchone()[0]
    if livros_count == 0:
        for livro in livros:
            cursor.execute(
                "INSERT INTO Livros (titulo, autor, preco) VALUES (:titulo, :autor, :preco)",
                vars(livro),
            )
        print("Livros inseridos.")
    else:
        print("Livros já possuem dados — pulando inserção.")

    cursor.execute("SELECT COUNT(*) FROM Clientes")
    clientes_count = cursor.fetchone()[0]
    if clientes_count == 0:
        for cliente in clientes:
            cursor.execute(
                "INSERT INTO Clientes (nome, email) VALUES (:nome, :email)", vars(cliente)
            )
        print("Clientes inseridos.")
    else:
        print("Clientes já possuem dados — pulando inserção.")

    cursor.execute("SELECT COUNT(*) FROM Pedidos")
    pedidos_count = cursor.fetchone()[0]
    if pedidos_count == 0:
        for pedido in pedidos:
            cursor.execute(
                "INSERT INTO Pedidos (cliente_id, livro_id, quantidade, data_pedido) VALUES (:cliente_id, :livro_id, :quantidade, :data_pedido)",
                vars(pedido),
            )
        print("Pedidos inseridos.")
    else:
        print("Pedidos já possuem dados — pulando inserção.")

    conexao.commit()
    
def exibir_pedidos(conexao: sqlite3.Connection) -> None:
    """Consulta e imprime os pedidos presentes no banco."""

    cursor = conexao.cursor()
    query = """
    SELECT Pedidos.id, Clientes.nome, Livros.titulo, Pedidos.quantidade, Pedidos.data_pedido
    FROM Pedidos
    JOIN Clientes ON Pedidos.cliente_id = Clientes.id
    JOIN Livros ON Pedidos.livro_id = Livros.id
    """
    cursor.execute(query)
    pedidos = cursor.fetchall()
    print("Pedidos:")

    for pedido in pedidos:
        print(pedido)

if __name__ == '__main__':
    conexao = conectar_banco('livraria.db')
    criar_tabelas(conexao)
    inserir_dados(conexao)
    exibir_pedidos(conexao)
    conexao.close()