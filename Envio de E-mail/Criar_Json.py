# Oejtivo: Criar arquivo Json para ser lido na criação de e-mails
import json
import os 

name_file =  "desnatario.json" #nome do arquivo Json

#Configurando informações do email
configuracao = { #Configurando o conteudo do arquivo
    "Destinatarios" : "",
    "Assunto": "",
    "Body": """ """
    
}

#Se não existir cria o arquivo json 
if not os.path.exists(name_file) or os.stat(name_file).st_size == 0:
    with open(name_file, 'w') as file:
        json.dump(configuracao, file, indent=4)
        
      