arquivo = open("teste.txt",  "r")

conteudo = arquivo.readline()

print("Tipo de dado de 'conteudo':", type(conteudo))
print("Conteúdo do retornado por 'readline':")
print(conteudo)
print(repr(conteudo))

conteudo = arquivo.readline()
print("Conteúdo do retornado por 'readline' novamente:")
print(conteudo)
print(repr(conteudo))

conteudo = arquivo.readline()
print("Conteúdo do retornado por 'readline' novamente:")
print(conteudo)
print(repr(conteudo))

arquivo.close()