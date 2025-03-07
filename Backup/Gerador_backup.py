from datetime import datetime
from pathlib import Path
import os
import shutil #Disponibiliza recursos entre pastas

data = datetime.now().strftime('%Y-%m-%d')  # Exemplo: 2025-02-28
print("Sistema de Backup iniciado!")


def criar_pasta(): #cria a estrutra de pastas (UnidadeDisco:/Backup/Dia)
    
    unidade_backup = "C:/" #unidade de disco onde será armazenado o backup
    pasta_uni_disco = Path(unidade_backup)/ "Backup"  #Cria dentro da unidade de disco a pasta "Backup"
    
    # Criar a pasta, caso não exista
    pasta_uni_disco.mkdir(parents = True, exist_ok = True)

    # Criar dentro da pasta "Backup" uma pasta com a data atual
    pasta_backup = Path(pasta_uni_disco) / data #criar dentro da pasta "Backup" uma pasta com a data que será feito o backup
    pasta_backup.mkdir(parents = True, exist_ok = True)

    return pasta_backup #retorna o valor past_backup(caminho)

def criar_log(caminho_pasta): #Criar o arquivo log
    inicio_backup = datetime.now().strftime("%d-%m-%Y %H:%M")
    
    conteudo = f"""
    Backup Iniciado em: {inicio_backup}
    Origem dos Arquivos: #colocar aqui a pasta que será feito o backup
    Caminho Destino: 
    
    Arquivos/ Pastas incluídos:  
    Listar todos os arquivos
    
    Tamanho total do backup: #informar o tamanho 
    Tempo de Execução: x minutos
    
    Resumo:
    Arquivos compactados: #numero de arquivos compactados
    Pastas compactadas: #numero de pastas compactados
    
    Status: Concluído com Sucesso #informar se foi feito ou não
    Backup concluído em:
    """
    fim_backup = datetime.now().strftime("%d-%m-%Y %H:%M")
    
    #caminho completo para cirar o log
    arquivo_log = os.path.join(caminho_pasta, "arquivo_log.txt")
    
    #Criar e escrever no log
    with open(arquivo_log, "w") as log:
        log.write(conteudo)

# Função para realizar o backup
def gerar_backup(origem, destino):
    # Verifica se o diretório de destino não existe e cria
    if not os.path.exists(destino):
        os.makedirs(destino)
    
    # Listagem de todos os arquivos e pastas dentro do diretório de origem
    arquivos = os.listdir(origem)  # Lista os itens presentes dentro de um diretório
    #arquivos = ", ".join(arquivos) #transforma os elementos da lista em str
    
    for arquivo in arquivos:  # Para cada item na lista 'arquivos'
        caminho_origem = os.path.join(origem, arquivo)  # Caminho completo do item na origem
        caminho_destino = os.path.join(destino, arquivo)  # Caminho completo do item no destino
        
        # Verifica se é um diretório
        if os.path.isdir(caminho_origem):
            # Se for diretório, chama recursivamente a função para fazer o backup
            gerar_backup(caminho_origem, caminho_destino)
        else:
            # Se for arquivo, copia o arquivo para o destino
            shutil.copy2(caminho_origem, caminho_destino)  # Copia o arquivo da origem para o destino

#Compactar diretório
def compactar_diretorio(destino):#Compactando o diretório com ZIP
    # Caminho do arquivo compactado (sem a extensão .zip)
    arquivo_compacto = destino  # Não adicione a extensão .zip aqui
    
    # Compacta a pasta destino no formato .zip
    shutil.make_archive(arquivo_compacto, "zip", destino)


#excluir diretório
def excluir_diretorio(destino):#Excluindo o diretório antigo
    try:
        shutil.rmtree(destino)
        
    except OSError as e:
        # Informe o usuário sobre quaisquer erros
        print(f"Erro: {e.filename} - {e.strerror}")

#definir pastas que será feito backup  
origem = r"C:\Users\mathe\Desktop\Projetos Python\Gerador de Etiquetas" #Pasta alvo do Backup
destino = fr"E:\backup\{data}" #Enderço onde será salvo

#Chamando as funções
caminho_pasta = criar_pasta() # Cria a pasta e retorna o caminho
criar_log(caminho_pasta) #caminho_pasta é passado como argumento
gerar_backup(origem, destino)#informa a variável arquivos como parâmetro
compactar_diretorio(destino)
excluir_diretorio(destino)

print("Processo de Backup Concluído com Sucesso!")
