import win32com.client as win32 #install pywin32

#Criando integração com outlook
outlook = win32.Dispatch('outlook.application')

#Criando um e-mail
email = outlook.CreateItem(0)

#Configurndo informações do email
email.to = "Destino1; Destino2" #Destinatários, sep=;
email.Subject = "" #Asssunto do Email
email.HTMLBody =F""" """ #Corpo do email em HTML

email.display() #Função para enviar o email

print("E-mail enviado")