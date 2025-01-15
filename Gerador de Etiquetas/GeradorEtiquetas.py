import os
import requests
from datetime import datetime
from fpdf import FPDF
from LeitorDados import Etiqueta


# Defina o caminho e o nome do arquivo
caminho = r"C:\Users\mathe\Desktop\Projetos Python\Gerador de Etiquetas"
arquivo = "Dados-Etiquetas.xlsx"
pasta_saida = os.path.join(caminho, 'PDFs_Gerados')  # Caminho para a pasta de saída

# Crie a pasta se não existir
os.makedirs(pasta_saida, exist_ok=True)

# Crie uma instância da classe Etiqueta
gerador = Etiqueta(caminho, arquivo)

# Extraia as informações
informacoes = gerador.extrair_informacoes()

# Criação do PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Definindo parâmetros de grade ajustados
colunas = 2  # Número de colunas na grade
largura_etiqueta = 190  # Largura das etiquetas (aumentada para ajustá-las)
altura_etiqueta = 80  # Altura das etiquetas (aumentada para ajustá-las)
espaco_x = -90  # Reduzido o espaçamento horizontal entre as etiquetas
espaco_y = -30  # Reduzido o espaçamento vertical entre as etiquetas

# Posição inicial na página
x_position = 10  # Posição inicial X
y_position = 10  # Posição inicial Y

# Função para excluir os arquivos temporários (imagens PNG)
def excluir_arquivos_temporarios(caminho_arquivo):
    if os.path.exists(caminho_arquivo):
        os.remove(caminho_arquivo)


# Loop para gerar e adicionar as etiquetas
for i, info in enumerate(informacoes):
    # Geração do ZPL
    zpl_code = fr""" 
        ^XA

        ^CF0,20
        ^FO8,10^FD AeroBrasil^FS
        ^FO93,20^FD Parts^FS

        ^FX-------------------(LABEL)^FS 

        ^FO25,30^BQ,4,4^FD>https://www.gov.br/anac/pt-br^FS ^FX----- QR code

        ^CF0,20
        ^FO215,8^FD {info['codigo']}^FS ^FX-----CODE DA PEÇA

        ^A@N,10,5,C:\Fonts\Calibri.FNT
        ^FO175,40^FD {info['item']}^FS ^FX-----NOME DA PEÇA

        ^A@N,10,5,C:\Fonts\Calibri.FNT
        ^FO290,40^FD {info["modelo"]}^FS ^FX----- MODELO PEÇA

        ^A@N,10,5,C:\Fonts\Calibri.FNT
        ^FO175,60^FD {info['marca']}^FS ^FX-----MARCA

        ^A@N,10,5,C:\Fonts\Calibri.FNT
        ^FO290,60^FD {info['cod_marca']}^FS ^FX-----COD MARCA

        ^A@N,10,5,C:\Fonts\Calibri.FNT
        ^FO175,80^FD {info["aplicacao"]}^FS ^FX-----APLICAÇÃO

        ^CF0,14
        ^FO175,105^FD MANUFCTURING DESCRIPTION^FS ^FX----- Descrição

        ^A@N,15,10,C:\Fonts\Calibri.FNT
        ^FO255,122^FD {info["serial_number"]}^FS ^FX-----Serial Number

        ^A@N,10,5,C:\Fonts\Calibri.FNT
        ^FO175,125^FD {info['cod_marca']}^FS ^FX-----Fabricação

        ^A@N,10,5,C:\Fonts\Calibri.FNT
        ^FO175,148^FD CERTIFACED: ^FS ^FX-----Certificado

        ^A@N,10,5,C:\Fonts\Calibri.FNT
        ^FO245,148^FD {info["certificado"]} ^FS ^FX-----Certificado

        ^CF0,16
        ^FO15,165^FD CERTIFIED BY ANAC^FS ^FX-----Certificado ANAC

        ^A@N,10,5,C:\Fonts\Calibri.FNT
        ^FO15,190^FD {info['data_fab']}^FS ^FX----- DATA FABRICAÇÃO

        ^A@N,10,5,C:\Fonts\Calibri.FNT
        ^FO90,190^FD {info['origem']}^FS ^FX----- ORIGEM

        ^A@N,10,5,C:\Fonts\Calibri.FNT
        ^FO15,210^FD VALID: {info['validade']}^FS ^FX----- DATA FABRICAÇÃO

        ^FX-------------------(LAYOUT)^FS 
        ^FO0,0^GB359,239,1,0,^FS ^FX --- Retângulo Externo
        ^FO0,0^GB170,239,1,0,^FS
        ^FO169,0^GB190,29,1,0,^FS
        ^FO169,0^GB190,100,1,0,^FS
        ^FO169,0^GB190,120,1,0,^FS
        ^FO169,119^GB90,20,1,0,^FS
        ^FO169,119^GB190,20,1,0,^FS
        ^FO169,138^GB190,25,1,0,^FS

        ^FO200,170^BY1^BCN,50^FD {info['codbarras']}^FX VALOR DO EAN

        ^XZ

    """

    # Requisição para gerar a imagem da etiqueta em PNG
    url = 'http://api.labelary.com/v1/printers/6dpmm/labels/7x4/0/'
    files = {'file': zpl_code}
    headers = {'Accept': 'image/png'}  # Alterado para aceitar PNG
    response = requests.post(url, headers=headers, files=files, stream=True)

    if response.status_code == 200:
        # Salva a imagem da etiqueta na pasta de saída
        image_filename = os.path.join(pasta_saida, f'label_{info["codigo"]}.png')
        with open(image_filename, 'wb') as img_file:
            img_file.write(response.content)

        # Adiciona uma nova página ao PDF se for a primeira etiqueta ou se a posição excede a altura da página
        if pdf.page_no() == 0 or y_position + altura_etiqueta + espaco_y > 280:  # 280 é o limite para A4 com margem
            pdf.add_page()
            y_position = 10  # Reset da posição vertical
            x_position = 10  # Reset da posição horizontal

        # Adiciona a imagem da etiqueta na posição atual (grade)
        pdf.image(image_filename, x=x_position, y=y_position, w=largura_etiqueta)
        
        # Excluir o arquivo PNG temporário após usá-lo
        excluir_arquivos_temporarios(image_filename)

        # Atualiza a posição para a próxima etiqueta na grade
        x_position += largura_etiqueta + espaco_x
        if x_position > 200:  # Se ultrapassar a largura da página
            x_position = 10
            y_position += altura_etiqueta + espaco_y
    else:
        print(f"Erro ao gerar a imagem para o código {info['codigo']}.")
          
#extrair data atual
hoje = datetime.now().strftime("%d_%m_%Y")         

# Salva o PDF gerado
entrada_usuario = input("Insira o nome do arquivo: ")
pdf_output_path = os.path.join(pasta_saida, f"Etiquetas-{entrada_usuario}_{hoje}.pdf")
pdf.output(pdf_output_path)

print("PDF gerado com sucesso!")

print(f"Salvo em {pdf_output_path}") 
      


comando = input("Deseja Sair? (S/N) ")
while comando == "S" or "s":
    break