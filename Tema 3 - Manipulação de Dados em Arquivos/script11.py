arquivo = open("dados_write_apend.txt", "a")

arquivo.write("Linha adicionada.\n")
arquivo.write("Segunda linha adicionada: O Python não adiciona nova linha automaticamente.") # O Python não adiciona nova linha automaticamente

arquivo.close()