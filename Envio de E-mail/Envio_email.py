import win32com.client as win32
import json
import os

# Criar JSON caso não exista
def criar_json(name_file):
    configuracao = {
        "Destinatarios": "",
        "Assunto": "",
        "Cc": "",
        "Anexo": "",
        "Body": []
    }

    if not os.path.exists(name_file) or os.stat(name_file).st_size == 0:
        with open(name_file, 'w', encoding='utf-8') as file:
            json.dump(configuracao, file, indent=4)
        print(f"Arquivo {name_file} criado com sucesso!")

# Ler JSON
def ler_json(name_file):
    try:
        with open(name_file, 'r', encoding='utf-8') as dados:
            return json.load(dados)
    except (json.decoder.JSONDecodeError, FileNotFoundError, KeyError) as e:
        print(f"Erro ao ler {name_file}: {e}")
        return None

# Enviar E-mail
def enviar_email(assunto, destinatario, corpo_email, Cc, anexo):
    outlook = win32.Dispatch('outlook.application')
    email = outlook.CreateItem(0)

    email.To = destinatario
    email.Subject = assunto
    email.CC = Cc
    email.HTMLBody = corpo_email

    if anexo:
        try:
            email.Attachments.Add(anexo)
        except Exception as e:
            print(f"Erro ao adicionar anexo: {e}")

    email.display() #Para visualizar antes de enviar
    # email.Send() # Envia automaticamente
    print("E-mail enviado com sucesso!")

# Nome do arquivo JSON correto
name_file = "destinatario.json"

# Criar JSON caso não exista
criar_json(name_file)

# Ler JSON
config = ler_json(name_file)

if config:
    assunto = config["Assunto"]
    destinatario = config["Destinatarios"]
    Cc = config["Cc"]
    anexo = config["Anexo"].replace("/", "\\")
    corpo_email = "".join(config.get("Body", ["<p>Sem conteúdo disponível.</p>"]))

    if not destinatario:
        print("Erro: O campo 'Destinatarios' está vazio no arquivo JSON!")
    else:
        enviar_email(assunto, destinatario, corpo_email, Cc, anexo)
else:
    print("Erro ao carregar JSON")
