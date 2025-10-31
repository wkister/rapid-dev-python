arquivo = open("teste.txt", "r")

conteudo = arquivo.read()

print("Conteúdo do arquivo com caracteres especiais:")
print(repr(conteudo), '\n')

conteudo_releitura = arquivo.read()
print("Conteúdo do arquivo após tentativa de releitura:")
print(repr(conteudo_releitura), '\n')

arquivo.close()

arquivo_reaberto = open("teste.txt", "r")
conteudo_reaberto = arquivo_reaberto.read()
print("Conteúdo do arquivo após reabertura:")
print(repr(conteudo_reaberto), '\n')

arquivo_reaberto.seek(0)
conteudo_seek = arquivo_reaberto.read()
print("Conteúdo do arquivo após seek(0):")
print(repr(conteudo_seek), '\n')

arquivo_reaberto.close()