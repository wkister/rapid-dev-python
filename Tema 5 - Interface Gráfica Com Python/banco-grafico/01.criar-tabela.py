
import psycopg2
from faker import Faker

conn = psycopg2.connect(
    database = "meu-banco", 
    user = "meu-usuario", 
    password = "minha-senha-segura", 
    host = "localhost", 
    port = "5432"
)

print("Conexão com o banco de dados aberta com sucesso!")

cur = conn.cursor()

# Faker: criar uma instância e reutilizar
fake = Faker()

cur.execute('''
    CREATE TABLE IF NOT EXISTS PRODUTO (
        CODIGO SERIAL PRIMARY KEY,
        NOME VARCHAR(100) NOT NULL,
        PRECO NUMERIC(10, 2) NOT NULL
    );
''')

conn.commit()
print("Tabela criada com sucesso!")

for _ in range(10):
    # usar a instância `fake` (métodos não são estáticos)
    nome = fake.word()
    preco = round(fake.random_number(digits=5) / 100, 2)
    cur.execute('''
        INSERT INTO PRODUTO (NOME, PRECO) VALUES (%s, %s)
    ''', (nome, preco))

conn.commit()
print("Dados inseridos com sucesso!")

conn.close()