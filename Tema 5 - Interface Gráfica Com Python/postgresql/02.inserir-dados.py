import psycopg2

con = psycopg2.connect(database="meu-banco", user="meu-usuario", password="minha-senha-segura", host = "localhost", 
    port = "5432")

cur = con.cursor()

sql = """INSERT INTO AGENDA Values (1, 'Pessoa 1', '02199999999' )"""

cur.execute(sql)

con.commit()

print("Dados inseridos com sucesso")

con.close()