from PIL import Image

def convert_png_to_pcx(input_file, output_file):
    try:
        # Abrir a imagem PNG
        img = Image.open(input_file)

        # Salvar a imagem como PCX
        img.save(output_file, format='PCX')

        print(f"Imagem convertida com sucesso para: {output_file}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Substitua 'input.png' pelo caminho da sua imagem PNG
input_path = "C:\\Users\\Bruno\\Desktop\\pasta-teste\\teste.png"

# Substitua 'output.pcx' pelo nome desejado do arquivo PCX de saída
output_path = "C:\\Users\\Bruno\\Desktop\\pasta-teste\\teste_02.pcx"

# Chamando a função para converter
convert_png_to_pcx(input_path, output_path)