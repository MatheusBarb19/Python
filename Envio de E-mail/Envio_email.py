import win32com.client as win32 #install pywin32
import json
import os

#cria um arquivo Json caso não exista
def criar_json(name_file):

    configuracao = { #Configurando o conteudo do arquivo
        "Destinatarios" : "",
        "Assunto": "",
        "Cc": "",
        "Anexo": "",
        "Body": ""
            }

    #Se não existir cria o arquivo json 
    if not os.path.exists(name_file) or os.stat(name_file).st_size == 0:
        with open(name_file, 'w') as file:
            json.dump(configuracao, file, indent=4)
        
    
#Função para ler o JSON corretamente   
def ler_json(name_file):
    
    try:
       with open(name_file, 'r', encoding='utf-8') as dados:
            return json.load(dados)  # Retorna os dados lidos do JSON
        
    except (json.decoder.JSONDecodeError, FileNotFoundError, KeyError) as e:
        print(f"Erro ao ler {name_file}: {e}")
        return None  # Retorna None se houver erro


def enviar_email(assunto, destinatario, corpo_email, Cc, anexo):
    
    #Criando integração com outlook
    outlook = win32.Dispatch('outlook.application')

    #Criando um e-mail
    email = outlook.CreateItem(0)

     # Configurando informações do e-mail
    email.To = destinatario  # Destinatários, sep=;
    email.Subject = assunto  # Assunto do E-mail
    email.CC = Cc
    email.HTMLBody = corpo_email  # Corpo do e-mail
    
     # Se houver anexo, adiciona
    if anexo:
        try:
            email.Attachments.Add(anexo)  # Adiciona o anexo ao e-mail
        except Exception as e:
            print(f"Erro ao adicionar anexo: {e}")
    
    
    
    email.display() #Função para enviar o email

    print("E-mail enviado")

#nome do arquivo Json
name_file =  "desnatario.json" 

#ler o JSON
config = ler_json(name_file)

#verificar se o arquivo Json foi carregado corretamente
if config: 
    assunto = config['Assunto']
    destinatario = config['Destinatarios']
    Cc = config['Cc']
    anexo = config['Anexo']  # Certifique-se de que o caminho do anexo está correto
    corpo_email = "\n".join(config.get("Body", ["<p>Sem conteúdo disponível.</p>"]))  # Junta os elementos da lista com "\n"
    
    #Verificar se o destinário está vazio
    if not destinatario:
        print("Erro: O campo 'destinatário' no arquivo Json está vázio!")
        
    else:    
        #Enviar e-mail
        enviar_email(assunto, destinatario, corpo_email, Cc, anexo)
else:
    print("Erro ao carregar JSON")
