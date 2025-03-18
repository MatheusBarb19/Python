# 📁 Sistema de Backup Automatizado

## 📌 Descrição

Este script em Python automatiza o backup de arquivos e pastas, copiando-os para um diretório de destino, compactando os dados em um arquivo `.zip` e gerando um log do processo. Ele também permite a configuração dinâmica da origem e destino dos arquivos por meio de um arquivo JSON.

## 🚀 Funcionalidades

- Cria automaticamente um diretório de backup baseado na data atual.
- Lê configurações de origem e destino a partir de um arquivo `config_backup.json`.
- Copia arquivos e pastas da origem para o destino.
- Compacta o backup em um arquivo `.zip`.
- Gera um log detalhado do processo.
- Remove a pasta temporária após a compactação.

## 🛠 Tecnologias Utilizadas

- Python 3
- `shutil` (cópia e compactação de arquivos)
- `pathlib` (manipulação de diretórios)
- `json` (leitura/escrita do arquivo de configuração)
- `datetime` (registro de logs e nomeação de arquivos)

## 📂 Estrutura de Arquivos

```
Backup_Script/
│-- config_backup.json
│-- backup_script.py
│-- Backup/ (gerado automaticamente)
│   ├── YYYY-MM-DD/ (arquivos copiados)
│   ├── YYYY-MM-DD.zip (backup compactado)
│   ├── arquivo_log.txt (log do processo)
```

## ⚙️ Configuração

Antes de executar o script, edite o arquivo `config_backup.json` para definir a origem e destino do backup:

```json
{
    "origem": "C:/caminho/para/origem",
    "destino": "D:/
