"""
Manipulação de Dados em Arquivos

Este script demonstra operações básicas de manipulação de arquivos em Python,
incluindo escrita e leitura de arquivos de texto.

Funcionalidades:
1. Coleta frases do usuário via entrada de console
2. Salva as frases em um arquivo de texto
3. Lê o arquivo, modifica as frases (convertendo para maiúsculas)
4. Salva as frases modificadas em um novo arquivo

Arquivos gerados:
- frases_usuario.txt: Contém as frases originais do usuário
- frases_modificadas.txt: Contém as frases convertidas para maiúsculas

Autor: Willian Kister
Data: Outubro 2025
"""

def main():
    """
    Função principal que gerencia a coleta, processamento e armazenamento de frases.

    O fluxo de execução é:
    1. Coleta frases do usuário até que 'sair' seja digitado
    2. Salva as frases originais em 'frases_usuario.txt'
    3. Lê as frases do arquivo, converte para maiúsculas
    4. Salva as frases modificadas em 'frases_modificadas.txt'
    """
    print("Digite suas frases (Digite 'sair' para sair):")

    # Lista para armazenar as frases do usuário
    frases = []

    # Loop de coleta de frases
    while True:
        # Obtém a entrada do usuário
        entrada = input("> ")

        # Verifica se o usuário quer sair
        if entrada.lower() == 'sair':
            break

        # Adiciona a frase à lista
        frases.append(entrada)

    # Salva as frases originais no arquivo
    with open("frases_usuario.txt", "w") as arquivo:
        # Escreve cada frase no arquivo, adicionando uma nova linha após cada uma
        for frase in frases:
            arquivo.write(frase + "\n")

    print("Frases salvas no arquivo 'frases_usuario.txt'.")

    # Processamento e modificação das frases
    frases_modificadas = []

    # Lê o arquivo original e modifica as frases
    with open("frases_usuario.txt", "r") as arquivo:
        for linha in arquivo:
            # Remove espaços em branco extras e converte para maiúsculas
            frase_modificada = linha.strip().upper()
            frases_modificadas.append(frase_modificada)

    # Salva as frases modificadas em um novo arquivo
    with open("frases_modificadas.txt", "w") as arquivo_modificado:
        for frase in frases_modificadas:
            arquivo_modificado.write(frase + "\n")

    print("Frases modificadas salvas no arquivo 'frases_modificadas.txt'.")


# Executa a função principal
if __name__ == "__main__":
  main()