# Scripts de Criação e Leitura de Arquivo JSON para E-mail (Módulos)

Este repositório contém dois scripts Python que trabalham com arquivos JSON para a configuração de envio de e-mails. São módulos simples que desenvolvi no processo de criação do script, que pode de maneira geral ensinar didaticamente a lógica da aplicação.

## 1. Criar_Json.py

# Objetivo
Este script tem como objetivo criar um arquivo JSON contendo informações sobre o destinatário, assunto e corpo de um e-mail. Caso o arquivo JSON não exista ou esteja vazio, ele será criado com as configurações padrão.

# Como funciona
O script verifica se o arquivo desnatario.json já existe ou se está vazio.

- Se o arquivo não existir ou estiver vazio, ele cria o arquivo com a estrutura definida.

- As configurações padrão no arquivo JSON são:

   - Destinatários: Um campo em branco para adicionar os destinatários do e-mail.

   - Assunto: Um campo em branco para adicionar o assunto do e-mail.

   - Body: Um campo em branco para adicionar o corpo do e-mail.

# Como usar:
1. execute o script para garantir que o arquivo 'destinatario.json' seja criado com as configurações padrões.
         python Criar_Json.py


## 2. Ler_Json.py

# Objetivo
Este script é utilizado para ler o arquivo JSON gerado pelo script Criar_Json.py e extrair as informações do destinatário, assunto e corpo do e-mail.

# Como funciona
- O script abre o arquivo desnatario.json e carrega seu conteúdo em um dicionário Python.
- Ele então imprime o conteúdo das chaves Assunto e Body.

# Como usar:
1. Após ter criado o arquivo desnatario.json, execute o script Ler_json.py para ver as informações configuradas.
         python Ler_Json.py