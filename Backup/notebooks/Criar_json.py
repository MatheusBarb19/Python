import json
import os

# Função para criar o arquivo JSON se ele não existir ou estiver vazio
def criar_json():
    pasta = r"C:\Backup"  # Caminho da pasta (uso de raw string para evitar problemas)
    name_file = os.path.join(pasta, "config_backup.json")  # Caminho completo do arquivo

    config_padrao = {  # Conteúdo padrão
        "origem": "Insira a pasta origem do backup",
        "destino": "Insira a pasta destino do backup"
    }

    # Se a pasta não existir, cria
    if not os.path.exists(pasta):
        os.makedirs(pasta)  # Cria a pasta

    # Se o arquivo não existir ou estiver vazio, cria com os dados padrão
    if not os.path.exists(name_file) or os.stat(name_file).st_size == 0:
        with open(name_file, "w") as file:
            json.dump(config_padrao, file, indent=4)  # Escreve o JSON formatado
    
    return name_file  # Retorna o caminho do arquivo

# Função para ler os dados do arquivo JSON
def ler_json(name_file):
    try:
        with open(name_file, "r") as dados:
            config = json.load(dados)  # Carrega o conteúdo do JSON
        return config  # Retorna o dicionário
    except json.decoder.JSONDecodeError:
        print(f"Erro ao ler {name_file}: arquivo corrompido. Criando um novo...")
        return criar_json()  # Se houver erro, recria o arquivo corretamente

# Chama a função para garantir que o arquivo exista
name_file = criar_json()

# Tenta ler o JSON e armazenar os dados
config = ler_json(name_file)



