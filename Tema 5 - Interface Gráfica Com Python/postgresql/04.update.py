import psycopg2

con = psycopg2.connect(
    database = 'meu-banco',
    user = 'meu-usuario',
    password = 'minha-senha-segura',
    host = 'localhost',
    port = '5432'
)

print("\nConexao efetuada com sucesso!\n")

cur = con.cursor()

print( "Consultando o banco de dados")

cur.execute("SELECT * FROM Agenda")
reg = cur.fetchone()

print("Registros (antes da mudança): \n")
print(reg)

print("\nRealizando alterações\n")

cur.execute("""UPDATE Agenda set "telefone"='02188888888' where "id"=1;""")

print("\nRegistros (antes do commit): \n")
cur.execute("SELECT * FROM Agenda")
reg = cur.fetchone()
print(reg)

con.commit()

print("\nRegistros (após commit): \n")
cur.execute("SELECT * FROM Agenda")
reg = cur.fetchone()
print(reg)

print("\nPrograma finalizado!\n")
