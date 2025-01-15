import pandas as pd

#Extrai e armazena os dados em cada variável, que serão levadas para o arquivo Gerador Etiqueta
class Etiqueta:
    def __init__(self, caminho, arquivo):
        self.caminho = caminho
        self.df = pd.read_excel(fr"{self.caminho}\{arquivo}")

    def extrair_informacoes(self):
        informacoes = []
        for _, row in self.df.iterrows():
            etiqueta_info = {
                'codigo': row["CODIGO"],
                'item': row["ITEM"],
                'modelo': row["MODELO"],
                'aplicacao': row["APLICACAO"],
                'serial_number': row["SERIAL NUMBER"],
                'marca': row["MARCA"],
                'cod_marca': row["COD MARCA"],
                'data_fab': row["Fab.:"],
                'origem': row["ORIGEM"],
                'validade': row["VALIDADE"],
                'codbarras': row["CODBARRAS"],
                'certificado': row["CERTIFICADO"]
            }
            informacoes.append(etiqueta_info)
        return informacoes

    
# Uso da classe
caminho = r"C:\Users\mathe\Desktop\Projetos Python\Gerador de Etiquetas"
arquivo = "Dados-Etiquetas.xlsx"
gerador = Etiqueta(caminho, arquivo)
