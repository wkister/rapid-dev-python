arquivo = open("dados_write.txt", "w")

arquivo.write("Primeira linha adicionada.\n")
arquivo.write("Segunda linha adicionada.") # O Python não adiciona nova linha automaticamente

arquivo.close()