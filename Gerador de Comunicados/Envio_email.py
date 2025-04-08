import os
import win32com.client as win32
import json

def enviar_email(assunto, destinatario, corpo_email, Cc, anexo):
    try:
        # Criar o objeto Outlook
        outlook = win32.Dispatch('Outlook.Application')
        email = outlook.CreateItem(0)

        # Definir os campos do e-mail
        email.To = ";".join(destinatario) if isinstance(destinatario, list) else destinatario
        email.CC = ";".join(Cc) if isinstance(Cc, list) else Cc
        email.Subject = assunto
        email.HTMLBody = "\n".join(corpo_email) if isinstance(corpo_email, list) else corpo_email

        # Adicionar anexo se existir
        if anexo and os.path.exists(anexo):
            email.Attachments.Add(anexo)
        
        email.display()  # Para visualizar antes de enviar
        # email.Send()  # Para enviar diretamente
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

def carregar_dados_email(json_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            config = json.load(file)
        return config
    except Exception as e:
        print(f"Erro ao carregar JSON: {e}")
        return {}

if __name__ == "__main__":
    config = carregar_dados_email("destinatario.json")
    enviar_email(
        assunto=config.get("Assunto", "Sem assunto"),
        destinatario=config.get("Destinatarios", []),
        corpo_email=config.get("Corpo-email", "<p>Sem conteúdo disponível.</p>"),
        Cc=config.get("Cc", ""),
        anexo=config.get("Anexo", "")
    )
