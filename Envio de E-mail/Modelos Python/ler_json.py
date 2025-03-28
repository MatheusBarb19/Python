import json

name_file =  "desnatario.json" #nome do arquivo Json

try:
    with open(name_file, 'r') as dados: #Lê o arquivo
        config = json.load(dados)
        
except (json.decoder.JSONDecodeError, KeyError) as e:
    print(f"Erro ao ler {name_file}")
    
    
print(config['Assunto'])
print(config['Body'])