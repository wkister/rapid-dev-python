from PIL import Image
import numpy as np

def main():
    # Carregar a imagem
    imagem = Image.open("simple_icon.png")

    # Mostrando a imagem original
    print("Mostrando a imagem original...")
    imagem.show()

    # Converter a imagem em dados binários
    dados_binarios = np.array(imagem)
    print("\nDados binários da imagem carregada:")
    print(dados_binarios)

    # Salvar o shape para uso posterior
    shape_original = dados_binarios.shape
    print(f"\nDimensões da imagem: {shape_original}")

    # Converter para bytes
    binary_data = dados_binarios.tobytes()
    print(f"Tamanho dos dados binários: {len(binary_data)} bytes")

    # Salvando os dados binários em um arquivo
    with open("imagem_dados_binarios.bin", "wb") as arquivo_binario:
        arquivo_binario.write(binary_data)
    print("Dados binários salvos em 'imagem_dados_binarios.bin'.")

    # Copiar os dados binários para um novo arquivo
    with open("imagem_dados_binarios.bin", "rb") as arquivo_origem:
        dados = arquivo_origem.read()

    with open("imagem_copia.bin", "wb") as arquivo_destino:
        arquivo_destino.write(dados)
    print("Cópia dos dados binários salva em 'imagem_copia.bin'.")

    # Manipulando os dados binários (exemplo: inverter os bytes)
    with open("imagem_dados_binarios.bin", "rb") as arquivo_original:
        dados_originais = arquivo_original.read()

    # Invertendo os bytes
    dados_invertidos = dados_originais[::-1]

    # Salvando os dados manipulados em um novo arquivo
    with open("imagem_dados_invertidos.bin", "wb") as arquivo_invertido:
        arquivo_invertido.write(dados_invertidos)
    print("Dados binários invertidos salvos em 'imagem_dados_invertidos.bin'.")

    # Carregar e mostrar a imagem manipulada
    try:
        # Converter bytes invertidos de volta para array com o shape original
        modified_data = np.frombuffer(dados_invertidos, dtype=np.uint8).reshape(shape_original)
        modified_img = Image.fromarray(modified_data)
        print("\nMostrando a imagem com bytes invertidos...")
        modified_img.show()
    except Exception as e:
        print(f"\nErro ao manipular a imagem: {str(e)}")
        print("Isso é esperado, pois inverter os bytes pode criar dados inválidos para uma imagem.")

# Executa a função principal
if __name__ == "__main__":
  main()