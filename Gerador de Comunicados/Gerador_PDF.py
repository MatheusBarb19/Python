import tkinter as tk # cria a janela
from tkinter import ttk
from tkinter import messagebox

from reportlab.pdfgen import canvas #Cria o PDF
import textwrap
from reportlab.lib.pagesizes import A4 #Tamanho do PDF em A$

from Envio_email import enviar_email  # Importa a função sem executá-la automaticamente
from datetime import datetime #biblioteca datetime
import json #manipula json
import os #disponiniliza recursos do Windosw

def mm_to_p(mm):
    return mm / 0.352777  # Converte mm para pontos

#função para permitir a quebra de linha automática ao final da pagina
def adicionar_texto_multilinha(pdf, texto, x, y, largura_max, fonte="Helvetica", tamanho=12, leading=20):
    """ Adiciona um bloco de texto com quebras automáticas de linha. """
    text_object = pdf.beginText(mm_to_p(x), mm_to_p(y))
    text_object.setFont(fonte, tamanho)
    text_object.setLeading(leading)

    palavras = texto.split()
    linha_atual = ""
    
    for palavra in palavras:
        if pdf.stringWidth(linha_atual + " " + palavra, fonte, tamanho) < mm_to_p(largura_max):
            linha_atual += " " + palavra
        else:
            text_object.textLine(linha_atual.strip())
            linha_atual = palavra
    
    if linha_atual:
        text_object.textLine(linha_atual.strip())

    pdf.drawText(text_object)

     
class Application:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Gerador de Comunicados") #titulo da interface
        self.master.geometry("500x400") #tamanho da interface
        
        self.fonte_padrao = ("Arial", 10) #padronização da fonte

        # Container Principal
        self.container_principal = tk.Frame(master)
        self.container_principal.pack(pady=20)

        # Título
        self.titulo = tk.Label(self.container_principal, text="Gerador de Comunicados", font=("Arial", 12, "bold"))
        self.titulo.pack()

        # Tipo de Alteração
        self.label_tipo = tk.Label(self.container_principal, text="Tipo de Alteração:", font=self.fonte_padrao)
        self.label_tipo.pack(pady=5)

        #Criando uma combobox    
        self.tipo_alteracao = ttk.Combobox(self.container_principal, values=[ 
            #opções da combobox
            "Novo Produto",                                                                 
            "Alteração de Código",          
            "Alteração de Similaridade",
            "Alteração de Aplicação"
            
        ])
        self.tipo_alteracao.pack()
        self.tipo_alteracao.bind("<<ComboboxSelected>>", self.mostrar_campos)

        # Frame para campos dinâmicos
        self.frame_dinamico = tk.Frame(self.container_principal)
        self.frame_dinamico.pack(pady=10)

        # Botão para gerar PDF
        self.botao_gerar = tk.Button(self.container_principal, text="Gerar PDF", font=self.fonte_padrao, command=self.gerar_pdf) #atribuindo a função ao botão
        self.botao_gerar.pack(pady=10)

       #botão enviar Gerar e enviar e-mail
        self.botao_GerareEnviar = tk.Button(self.container_principal, text="Gerar e Enviar", font=self.fonte_padrao, command=self.gerar_e_enviar) #atribuindo a função ao botão
        self.botao_GerareEnviar.pack(pady=10) 

    def mostrar_campos(self, event):
        """ Atualiza os campos conforme o tipo de alteração selecionado. """
        for widget in self.frame_dinamico.winfo_children():
            widget.destroy()

        self.campos = {}

        tipo = self.tipo_alteracao.get()

        #campos input para inserir informações
        if tipo == "Novo Produto":
            self.adicionar_campo("SKU")
            self.adicionar_campo("Linha produto")
            self.adicionar_campo("Aplicação")
            
        elif tipo == "Alteração de Código":
            self.adicionar_campo("Código Atual")
            self.adicionar_campo("Novo Código")

        elif tipo == "Alteração de Similaridade":
            self.adicionar_campo("Marca Similar")
            self.adicionar_campo("Código Antigo do Similar")
            self.adicionar_campo("Código Novo do Similar")

        elif tipo == "Alteração de Aplicação":
            self.adicionar_campo("SKU")
            self.adicionar_campo("Aplicação Nova")
                

    def adicionar_campo(self, label_texto):
        """ Adiciona um campo de entrada na interface. """
        label = tk.Label(self.frame_dinamico, text=label_texto, font=self.fonte_padrao) #nome do campo ex: SKU
        label.pack() #Atribui a label no frame
        entry = tk.Entry(self.frame_dinamico, width=35) #insere o Entry (campo input)
        entry.pack() #atribui o Entry no frame
        self.campos[label_texto] = entry
        
        
    def gerar_pdf(self):
        #Funcão responsável por gerar o PDF
        
        dia_atual = datetime.now().strftime('%d/%m/%Y') #extrai o dia atual
        
        """ Gera um PDF com as informações inseridas na interface. """
        tipo = self.tipo_alteracao.get()
        if not tipo:
            messagebox.showerror("Erro", "Por favor, selecione um tipo de alteração!") #força a escolha do usuário 
            return

        dados = {campo: entry.get() for campo, entry in self.campos.items()}
        if any(not valor for valor in dados.values()):
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!") #Obriga que todos os Campos devem ser preenchidos
            return
        
        # Gerar o texto do comunicado
        if tipo == "Alteração de Código":
            texto_doc = f""" A MB PROJECTS comunica a partir de {dia_atual} o SKU, anteriormente identificado como {dados['Código Atual']}, será alterado
            para {dados['Novo Código']}. """
            

        elif tipo == "Alteração de Similaridade":
            texto_doc = f""" A MB PROJECTS informa que a marca {dados['Marca Similar']}, alterou o código anteriormente conhecido como {dados["Código Antigo do Similar"]},
            será descontinuado e substituído pelo código {dados["Código Novo do Similar"]}, esse comunicado é valido a partir de {dia_atual}."""


        elif tipo == "Alteração de Aplicação":
            texto_doc = f""" A MB PROJECTS informa que, a partir de {dia_atual},  o produto identificado pelo código {dados['SKU']} 
            terá sua aplicação alterada. Segue abaixo a nova aplicação:"""
            
        elif tipo == "Novo Produto":
            texto_doc = f""" A MB PROJECTS tem o prazer de anunciar o lançamento do código {dados['SKU']}, referente à linha {dados['Linha produto']}.
            Este novo código é destinado à aplicação abaixo, garantindo qualidade e desempenho conforme os padrões MB PROJECTS."
            """
            
        # Criando o PDF
        pdf = canvas.Canvas("COMUNICADO_MBPROJECTS.pdf", pagesize=A4) #Nomeando o documento.pdf e incorporando o tamanho A4

        # Adicionando um título fixo
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(mm_to_p(60), mm_to_p(265), "COMUNICADO MB PROJECTS SA") #Título do PDF

        pdf.setFont("Helvetica", 12)
        pdf.drawString(mm_to_p(15), mm_to_p(240), "Prezados colaboradores,") #Comprimentos

        #Caso o usuário escolha "Alteração de Aplicação", a aplicação é inserida no documento, como último elemento, para não causar divergências.
        if tipo=="Alteração de Aplicação": #inserir a aplicação no documento
            if tipo == "Alteração de Aplicação":
                pdf.setFont("Helvetica", 11)
                texto = dados["Aplicação Nova"]

                # Define a largura máxima do texto antes de quebrar a linha
                largura_maxima = 75  # Ajuste conforme necessário

                # Quebra o texto em várias linhas
                linhas = textwrap.wrap(texto, largura_maxima)

                # Posição inicial do texto
                x = mm_to_p(20)
                y = mm_to_p(165)

                # Escreve cada linha no PDF
                for linha in linhas:
                    pdf.drawString(x, y, linha)
                    y -= 15  # Move para a próxima linha (ajuste conforme necessário)

        #Caso o usuário escolha "Novo Produto", a aplicação é inserida no documento, como último elemento, para não causar divergências.
        if tipo=="Novo Produto":
             if tipo == "Novo Produto":
                pdf.setFont("Helvetica", 11)
                texto = dados["Aplicação"]

                # Define a largura máxima do texto antes de quebrar a linha
                largura_maxima = 75  # Ajuste conforme necessário

                # Quebra o texto em várias linhas
                linhas = textwrap.wrap(texto, largura_maxima)

                # Posição inicial do texto
                x = mm_to_p(20)
                y = mm_to_p(165)

                # Escreve cada linha no PDF
                for linha in linhas:
                    pdf.drawString(x, y, linha)
                    y -= 15  # Move para a próxima linha (ajuste conforme necessário)
        
        
        
        pdf.setFont("Helvetica", 12)
        pdf.drawString(mm_to_p(15), mm_to_p(180), f"Caso haja dúvidas, estamos à disposição para prestar esclarecimentos.") #Texto 1 rodape
        
        pdf.setFont("Helvetica", 12)
        pdf.drawString(mm_to_p(15), mm_to_p(30), f"Equipe Logística") #Texto 2 rodape
        
        pdf.setFont("Helvetica", 12)
        pdf.drawString(mm_to_p(15), mm_to_p(20), f"MB PROJECTS SA - {datetime.now().strftime('%Y')}.") #Texto 3 rodape
        
        """Adicionar imagem ao pdf"""
        largura_pagina, altura_pagina = A4
        caminho_imagem = os.path.join(os.getcwd(), "Logo.png") #camihno da imagem no computador
        
        #definir tamanho da imagem
        largura_imagem = 100
        altura_imagem = 50
        
        #Define a posição da imagem no topo
        x = (largura_pagina - largura_imagem) / 2 #Centraliza na horizontal
        y = 780
        
        #Adiciona a imagem no PDF (caminho, posição x, posição y, largura, altura)
        pdf.drawImage(caminho_imagem, x, y, width=largura_imagem, height=altura_imagem)
        
        texto_descritivo = """
        Essa alteração deve ser considerada em todos os processos internos, garantindo que os registros, sistemas e demais controles 
        estejam devidamente atualizados. Reforçamos a importância de revisar sua base de dados para evitar inconsistências nas operações.
        
        """

        # Adiciona o texto ao PDF
        adicionar_texto_multilinha(pdf, texto_doc, x=15, y=230, largura_max=185, fonte="Helvetica", tamanho=12) #Texto varíavel conforme o tipo de Alteração
        adicionar_texto_multilinha(pdf, texto_descritivo, x=15, y=208, largura_max=185, fonte="Helvetica", tamanho=12) #Inserindo um texto descritivo
        pdf.save()

        messagebox.showinfo("Sucesso", "PDF gerado com sucesso!") #exibe um abiso de sucesso
        
        caminho_pdf = os.path.join(os.getcwd(), "COMUNICADO_MBPROJECTS.pdf") #obtendo o caminho do pdf na pasta

        return caminho_pdf
    
    def gerar_e_enviar(self, event=None): #Gerar o PDF e envia o documento por e-mail
        
        caminho_pdf = self.gerar_pdf() # type: ignore
        
        # Carrega os dados do JSON
        with open("destinatario.json", "r", encoding="utf-8") as file: #Lê as informações que estrturam o E-mail
            dados = json.load(file) #Atribui os valores 
            
        # Pega as informações do JSON
        assunto = dados["Assunto"]
        destinatario = dados["Destinatarios"]
        corpo_email = dados["Corpo-email"]
        Cc = dados.get("Cc", "")  # Se não houver Cc, mantém vazio
        anexo = caminho_pdf
        
        enviar_email(assunto, destinatario, corpo_email, Cc, anexo) #Chamando a função no arquivo Envio_email.py
        
# Inicialização da Aplicação
root = tk.Tk()
app = Application(root)
root.mainloop()
