import os
import shutil

def criar_diretorios(diretorios):
    for diretorio in diretorios:
        if not os.path.exists(diretorio):
            try:
                os.makedirs(diretorio)
                print(f"Diretório {diretorio} criado.")
            except PermissionError:
                print(f"Sem permissão para criar o diretório {diretorio}.")
            except Exception as e:
                print(f"Erro inesperado ao criar {diretorio}: {e}")

def mover_arquivos(diretorio_origem, lista_extensoes):
    for arquivo in os.listdir(diretorio_origem):
        caminho_arquivo = os.path.join(diretorio_origem, arquivo)
    
        if os.path.isfile(caminho_arquivo):
            extensao = arquivo.split('.')[-1].lower()
            if extensao in lista_extensoes:
                diretorio_destino = os.path.join(diretorio_origem, extensao)
                try:
                    shutil.move(caminho_arquivo, diretorio_destino)
                    print(f"{arquivo} movido para {diretorio_destino}.")
                except PermissionError:
                    print(f"Sem permissão para mover {arquivo}.")
                except Exception as e:
                    print(f"Erro inesperado ao mover {arquivo}: {e}")
            else:
                print(f"Extensão {extensao} de {arquivo} não é suportada.")

def main():
    # Definindo a lista de extensões
    lista_extensoes = ['pdf', 'txt', 'jpg']
    # Definindo o diretório de trabalho
    diretorio_trabalho = "."
    # Criando a list de diretórios para cada extensão
    diretorios = [os.path.join(diretorio_trabalho, ext) for ext in lista_extensoes]

    # diretorios = [os.path.join(diretorio_trabalho, 'pdf'),
                    # os.path.join(diretorio_trabalho, 'txt'),
                    # os.path.join(diretorio_trabalho, 'jpg')]

    # Criar diretórios se não existirem
    criar_diretorios(diretorios)

    # Mover arquivos para os diretórios correspondentes
    mover_arquivos(diretorio_trabalho, lista_extensoes)

if __name__ == "__main__":
    main()