import psycopg2
from psycopg2 import sql

class DatabaseManager:
    def __init__(self):
        self.connection = None
        
    def connect(self):
        """Estabelece conex�o com o banco"""
        try:
            self.connection = psycopg2.connect(
                host="localhost",
                port=5432,
                database="meu-banco",
                user="meu-usuario",
                password="minha-senha-segura"
            )
            print("\u2705 Conectado ao PostgreSQL!")
        except Exception as e:
            print(f"\u274c Erro na conex�o: {e}")
    
    def create_table(self):
        """Cria uma tabela de exemplo"""
        try:
            cursor = self.connection.cursor()
            
            create_table_query = """
            CREATE TABLE IF NOT EXISTS usuarios (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                idade INTEGER,
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
            
            cursor.execute(create_table_query)
            self.connection.commit()
            print("\u2705 Tabela 'usuarios' criada/verificada!")
            cursor.close()
            
        except Exception as e:
            print(f"\u274c Erro ao criar tabela: {e}")
    
    def insert_user(self, nome, email, idade=None):
        """Insere um novo usu�rio"""
        try:
            cursor = self.connection.cursor()
            
            insert_query = """
            INSERT INTO usuarios (nome, email, idade)
            VALUES (%s, %s, %s)
            RETURNING id;
            """
            
            cursor.execute(insert_query, (nome, email, idade))
            user_id = cursor.fetchone()[0]
            self.connection.commit()
            
            print(f"\u2705 Usu�rio inserido com ID: {user_id}")
            cursor.close()
            return user_id
            
        except Exception as e:
            print(f"\u274c Erro ao inserir usu�rio: {e}")
            return None
    
    def get_users(self):
        """Recupera todos os usu�rios"""
        try:
            cursor = self.connection.cursor()
            
            cursor.execute("SELECT * FROM usuarios;")
            users = cursor.fetchall()
            
            print("\U0001f4cb Lista de usu�rios:")
            for user in users:
                print(f"ID: {user[0]}, Nome: {user[1]}, Email: {user[2]}, Idade: {user[3]}")
            
            cursor.close()
            return users
            
        except Exception as e:
            print(f"\u274c Erro ao buscar usu�rios: {e}")
            return []
    
    def update_user(self, user_id, nome=None, email=None, idade=None):
        """Atualiza um usu�rio"""
        try:
            cursor = self.connection.cursor()
            
            update_query = "UPDATE usuarios SET "
            params = []
            
            if nome:
                update_query += "nome = %s, "
                params.append(nome)
            if email:
                update_query += "email = %s, "
                params.append(email)
            if idade is not None:
                update_query += "idade = %s, "
                params.append(idade)
            
            # Remove a �ltima v�rgula e adiciona WHERE
            update_query = update_query.rstrip(', ') + " WHERE id = %s"
            params.append(user_id)
            
            cursor.execute(update_query, params)
            self.connection.commit()
            
            print(f"\u2705 Usu�rio {user_id} atualizado!")
            cursor.close()
            
        except Exception as e:
            print(f"\u274c Erro ao atualizar usu�rio: {e}")
    
    def delete_user(self, user_id):
        """Deleta um usu�rio"""
        try:
            cursor = self.connection.cursor()
            
            delete_query = "DELETE FROM usuarios WHERE id = %s;"
            cursor.execute(delete_query, (user_id,))
            self.connection.commit()
            
            print(f"\u2705 Usu�rio {user_id} deletado!")
            cursor.close()
            
        except Exception as e:
            print(f"\u274c Erro ao deletar usu�rio: {e}")
    
    def close_connection(self):
        """Fecha a conex�o"""
        if self.connection:
            self.connection.close()
            print("\U0001f50c Conex�o fechada!")

# Exemplo de uso
if __name__ == "__main__":
    db = DatabaseManager()
    db.connect()
    
    if db.connection:
        # Criar tabela
        db.create_table()
        
        # Inserir usu�rios
        db.insert_user("Jo�o Silva", "joao@email.com", 30)
        db.insert_user("Maria Santos", "maria@email.com", 25)
        db.insert_user("Pedro Oliveira", "pedro@email.com")
        
        # Listar usu�rios
        db.get_users()
        
        # Atualizar usu�rio
        db.update_user(1, nome="Jo�o da Silva", idade=31)
        
        # Listar novamente
        db.get_users()
        
        # Fechar conex�o
        db.close_connection()