import os
import shutil

def criar_diretorios(ext):    
    """
    Garantir que exista um diretório para a extensão `ext`.

    - Se `ext` for 'py' a função ignora (não cria diretórios para arquivos .py).
    - Se o diretório já existir, considera sucesso.
    - Retorna 1 em caso de sucesso (diretório criado ou já existente) e 0 em caso de falha.
    """
    # Não criar diretórios para arquivos Python do próprio projeto
    if ext == 'py':
        return 0

    # Se já existir, retorne sucesso
    if os.path.exists(ext):
        return 1

    try:
        os.makedirs(ext)
        print(f"Diretório {ext} criado.")
        return 1
    except PermissionError:
        print(f"Sem permissão para criar o diretório {ext}.")
        return 0
    except Exception as e:
        print(f"Erro inesperado ao criar {ext}: {e}")
        return 0

def mover_arquivos(diretorio_origem):
    """
    Percorre os arquivos de `diretorio_origem` e move cada arquivo para
    um subdiretório com o nome de sua extensão (por exemplo: 'pdf', 'jpg').

    Arquivos com extensão 'py' são ignorados. A função usa
    `criar_diretorios` para garantir que o diretório destino exista
    antes de mover o arquivo.
    """
    for arquivo in os.listdir(diretorio_origem):
        caminho_arquivo = os.path.join(diretorio_origem, arquivo)

        if not os.path.isfile(caminho_arquivo):
            # Ignora diretórios e outros tipos (como links)
            continue

        # Extrai a extensão (parte após o último ponto). Para arquivos
        # sem extensão a variável `extensao` será o próprio nome ou
        # igual ao nome completo; decidimos tratá-los como 'sem extensão'.
        parts = arquivo.rsplit('.', 1)
        if len(parts) == 1:
            extensao = ''
        else:
            extensao = parts[-1].lower()

        if criar_diretorios(extensao):
            diretorio_destino = os.path.join(diretorio_origem, extensao)
            try:
                shutil.move(caminho_arquivo, diretorio_destino)
                print(f"{arquivo} movido para {diretorio_destino}.")
            except PermissionError:
                print(f"Sem permissão para mover {arquivo}.")
            except Exception as e:
                print(f"Erro inesperado ao mover {arquivo}: {e}")
        else:
            print(f"Extensão '{extensao}' de {arquivo} não é suportada ou ocorreu erro.")

def main():
    """
    Ponto de entrada do script.

    Define o diretório de trabalho (por padrão o diretório atual) e
    chama `mover_arquivos` para organizar os arquivos por extensão.
    """
    diretorio_trabalho = "."
    mover_arquivos(diretorio_trabalho)

if __name__ == "__main__":
    main()