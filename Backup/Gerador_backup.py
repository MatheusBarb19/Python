# Forçando atualização da linguagem no GitHub
from datetime import datetime
from pathlib import Path
import shutil
import json
import os

# Obtém a data atual no formato YYYY-MM-DD
data = datetime.now().strftime('%Y-%m-%d')
print("Sistema de Backup iniciado!")

# Registra a hora e data de início do backup
inicio_backup = datetime.now().strftime("%d-%m-%Y %H:%M")

def criar_pasta(unidade_backup):
    """Cria a pasta de backup e retorna o caminho"""
    pasta_backup = Path(unidade_backup) / "Backup" / data
    pasta_backup.mkdir(parents=True, exist_ok=True)  # Cria a pasta de backup com a data atual
    return pasta_backup

def criar_json():
    """Cria o arquivo JSON de configuração se não existir"""
    pasta = Path("C:/Backup")
    name_file = pasta / "config_backup.json"
    
    # Configuração padrão do backup
    config_padrao = {
        "origem": "Insira a pasta origem do backup",
        "destino": "Insira a pasta destino do backup",
        "unidade_backup": "C:/"  # Unidade de backup configurável
    }
    
    if not pasta.exists():
        pasta.mkdir(parents=True)

    if not name_file.exists() or name_file.stat().st_size == 0:
        with open(name_file, "w") as file:
            json.dump(config_padrao, file, indent=4)

    return name_file

def ler_json(name_file):
    """Lê o arquivo JSON e retorna as configurações"""
    try:
        with open(name_file, "r") as dados:
            config = json.load(dados)

        # Valida se as chaves essenciais estão presentes no JSON
        if "origem" not in config or "destino" not in config or "unidade_backup" not in config:
            raise KeyError("O arquivo JSON não contém as chaves necessárias.")
        
        return config  # Retorna as configurações lidas do arquivo JSON
    
    except (json.decoder.JSONDecodeError, KeyError) as e:
        print(f"Erro ao ler {name_file}: {str(e)}. Criando um novo arquivo de configuração...")
        return criar_json()  # Cria um novo arquivo JSON se houver erro

def gerar_backup(origem, destino):
    """Realiza o backup dos arquivos da origem para o destino"""
    if not origem.exists():
        raise FileNotFoundError(f"A origem '{origem}' não existe.")
    
    if not destino.exists():
        destino.mkdir(parents=True)

    # Itera sobre os arquivos da origem e os copia para o destino
    for arquivo in origem.iterdir():
        caminho_destino = destino / arquivo.name
        
        if arquivo.is_dir():  # Se for uma pasta, faz chamada recursiva
            gerar_backup(arquivo, caminho_destino)
        else:  # Se for um arquivo, copia o arquivo preservando metadados
            shutil.copy2(arquivo, caminho_destino)

def listar_arquivos(origem):
    """Retorna uma lista formatada dos arquivos na origem"""
    return "\n\t".join([f"{arquivo.name}" for arquivo in origem.iterdir()])

def compactar_diretorio(destino, destino_zip):
    """Compacta o diretório de destino em um arquivo .zip"""
    # Cria o arquivo .zip no caminho especificado (destino_zip)
    shutil.make_archive(str(destino_zip), "zip", str(destino))  # Compacta a pasta de destino
    return destino_zip  # Retorna o caminho completo do arquivo compactado

def excluir_diretorio(destino):
    """Exclui o diretório de backup após a compactação"""
    try:
        shutil.rmtree(destino)  # Exclui a pasta de backup
    except OSError as e:
        print(f"Erro ao excluir diretório: {e.filename} - {e.strerror}")

def criar_log(origem, destino, caminho_pasta, inicio_backup):
    """Cria o log do processo de backup"""
    fim_backup = datetime.now().strftime("%d-%m-%Y %H:%M")
    arquivos = listar_arquivos(origem)

    # Formata o conteúdo do log
    conteudo = f"""
    Backup Iniciado em: {inicio_backup}
    Origem dos Arquivos: {origem}
    Caminho Destino: {destino}
    
    Arquivos/ Pastas incluídos:  
    {arquivos}
    
    Status: Concluído com Sucesso 
    Backup concluído em: {fim_backup}
    """

    # Define o caminho do arquivo de log
    arquivo_log = caminho_pasta / "arquivo_log.txt"
    with open(arquivo_log, "w") as log:
        log.write(conteudo)

# Cria e lê o arquivo JSON de configuração
name_file = criar_json()
config = ler_json(name_file)

# Lê as configurações de origem, destino e unidade de backup do arquivo JSON
origem = Path(config['origem'])  # Caminho da pasta de origem
destino = Path(config['destino']) / data  # Caminho de destino com data atual
unidade_backup = config['unidade_backup']  # Unidade de backup configurada no JSON

# Cria a pasta de backup na unidade especificada
caminho_pasta = criar_pasta(unidade_backup)

# Cria o log de início de backup
criar_log(origem, destino, caminho_pasta, inicio_backup)

# Realiza o backup copiando os arquivos da origem para o destino
gerar_backup(origem, destino)

# Define o caminho onde o arquivo .zip será salvo, conforme o destino configurado no JSON
# Modificado para garantir que o arquivo .zip seja salvo no diretório correto
destino_zip = Path(config['destino']) / f"{data}"  # Caminho correto para o arquivo .zip, baseado no arquivo JSON

# Compacta o diretório de backup em um arquivo .zip
arquivo_zip = compactar_diretorio(destino, destino_zip)

# Exclui o diretório de backup após a compactação
excluir_diretorio(destino)

# Exibe o caminho do arquivo compactado
print(f"Backup concluído com sucesso. Arquivo compactado em: {arquivo_zip}")
