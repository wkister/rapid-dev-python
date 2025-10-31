arquivo = open('teste.txt', 'r')  # Abre o arquivo em modo de leitura

print("Iteranado sobre o arquivo (com caracteres especiais visíveis):")
for linha in arquivo:
  print(repr(linha))  # Imprime cada linha com caracteres especiais visíveis

print("\nIteranado sobre o arquivo (normal):")
arquivo.seek(0)  # Retorna ao início do arquivo para nova leitura
for linha in arquivo:
  print(linha)        # Imprime cada linha normalmente

arquivo.close()  # Fecha o arquivo após a leitura