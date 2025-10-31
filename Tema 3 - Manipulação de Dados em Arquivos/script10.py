linhas = ["Primeira linha\n", "Segunda linha\n", "Terceira linha\n"]

arquivo = open("dados_writelines.txt", "a")

arquivo.writelines(linhas)

arquivo.close()