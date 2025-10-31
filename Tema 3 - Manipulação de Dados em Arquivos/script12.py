print("Iterando sobre o arquivo linha a linha com 'with':")

with open('teste.txt', 'r') as arquivo:
    for linha in arquivo:
        print(repr(linha))  # Imprime cada linha com caracteres especiais visíveis

print("\nArquivo fechado automaticamente após o bloco 'with':", arquivo.closed)