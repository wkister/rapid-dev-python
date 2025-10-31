arquivo = open("teste.txt", "r")

conteudo = arquivo.readlines()

print("Tipo de dado de 'conteudo':", type(conteudo))
print("Conteúdo do retornado por 'readlines':")
print(conteudo)
print(repr(conteudo))

arquivo.close()