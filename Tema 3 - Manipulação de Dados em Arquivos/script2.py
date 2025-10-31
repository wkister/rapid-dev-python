import os

arquivo = open("teste.txt")

arquivo2 = open("/home/wkister/ciencia-computacao_ead_estacio/2025_2/DGT0235_Desenvolvimento Rápido de Aplicações em Python/Tema 3 - Manipulação de Dados em Arquivos/teste.txt")

arquivo3 = open("../hello.py")
arquivo4 = open("/home/wkister/ciencia-computacao_ead_estacio/2025_2/DGT0235_Desenvolvimento Rápido de Aplicações em Python/hello.py")

print("Caminhos absolutos:")
print(os.path.abspath(arquivo.name))
print(os.path.abspath(arquivo2.name))
print(os.path.abspath(arquivo3.name))
print(os.path.abspath(arquivo4.name))

print("Caminhos relativos:")
print(os.path.relpath(arquivo.name))
print(os.path.relpath(arquivo2.name))
print(os.path.relpath(arquivo3.name))
print(os.path.relpath(arquivo4.name))

print(arquivo)