arquivo = open("teste.txt", "r")

conteudo = arquivo.read()

print("Tipo de dado de 'conteudo':", type(conteudo))

print("Conteúdo do arquivo:")

print(conteudo)

print(repr(conteudo))

arquivo.close()
