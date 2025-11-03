import psycopg2

con = psycopg2.connect(
    database="meu-banco",
    user="meu-usuario",
    password="minha-senha-segura",
    host="localhost",
    port="5432"
)

print("Conexao efetuada com sucesso!")

cur = con.cursor()

sql = "SELECT * FROM AGENDA;"

cur.execute(sql)

registro = cur.fetchone()

print(registro)

con.close()

print("\n\nComando completo!")