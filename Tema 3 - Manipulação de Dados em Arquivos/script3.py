import os

arquivo = open("teste.txt")

print("Atributos do arquivo:")
print("Nome do arquivo:", arquivo.name)
print("Modo de abertura:", arquivo.mode)
print("Fechado?", arquivo.closed)

arquivo.close()
print("Fechado após o close?", arquivo.closed)