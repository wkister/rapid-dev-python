import psycopg2 
from faker import Faker

import tkinter as tk 
from tkinter import ttk 

class BancoDados: 
    def __init__(self): 
        self.conexao = psycopg2.connect( 
            database="meu-banco",
            user="meu-usuario",
            password="minha-senha-segura",
            host="localhost" 
        ) 
        self.cursor = self.conexao.cursor() 
    
    def criar_tabela(self): 
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS livros ( 
                id SERIAL PRIMARY KEY, 
                titulo VARCHAR(255), 
                autor VARCHAR(255), 
                ano_publicacao INTEGER, 
                genero VARCHAR(100) 
            ) 
        """) 
        self.conexao.commit() 

    def inserir_dados(self, titulo, autor, ano_publicacao, genero): 
        self.cursor.execute(""" 
            INSERT INTO livros (titulo, autor, ano_publicacao, genero) 
            VALUES (%s, %s, %s, %s) 
        """, (titulo, autor, ano_publicacao, genero)) 
        self.conexao.commit()
    
    def selecionar_dados(self):
        self.cursor.execute("SELECT * FROM livros")
        return self.cursor.fetchall()

class BibliotecaGUI: 
    def __init__(self, root, bd): 
        self.bd = bd 
        self.root = root 
        self.root.title("Gerenciador de Biblioteca") 
        
        self.tree = ttk.Treeview(root, columns=("ID", "Título", "Autor", "Ano", "Gênero"), show="headings") 
        self.tree.heading("ID", text="ID") 
        self.tree.heading("Título", text="Título") 
        self.tree.heading("Autor", text="Autor") 
        self.tree.heading("Ano", text="Ano de Publicação") 
        self.tree.heading("Gênero", text="Gênero") 
        self.tree.pack() 

        self.carregar_dados() 

    def carregar_dados(self): 
        registros = self.bd.selecionar_dados() 
        for registro in registros: 
            self.tree.insert("", "end", values=registro) 

if __name__ == "__main__":
    fake = Faker() 
    app_bd = BancoDados() 
    app_bd.criar_tabela() 
    for _ in range(100): 
        app_bd.inserir_dados(fake.text(max_nb_chars=20), fake.name(), fake.year(), fake.word())
    
    root = tk.Tk()
    app_gui = BibliotecaGUI(root, app_bd) 
    root.mainloop()

    