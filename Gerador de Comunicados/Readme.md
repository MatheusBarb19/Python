# 📢 Gerador de Comunidados em PDF

## 📝 Descrição:
O Gerador de Comunicados é uma ferramenta desenvolvida em Python para automatizar a criação de comunicados em formato PDF e seu envio por e-mail. O sistema utiliza a biblioteca reportlab para gerar os PDFs e o pywin32 para no envio das mensagens eletrônicas.

## 🚀 Funcionalidades

.Gera comunicados automáticos em PDF com base em informações estruturadas.
.Envia os comunicados por e-mail para destinatários especificados.
.Utiliza arquivos JSON para facilitar a personalização dos comunicados.
.Interface amigável baseada em Tkinter.

## 🛠️ Tecnologias Utilizadas

- Linguagem: Python 3.x 🐍
- Bibliotecas:
     . reportlab (para gerar PDFs)
     . pywin32 (para envio de e-mails)
     . tkinter (para interface gráfica)
     . json (para armazenar dados de destinatários)
  
## 🛠️ Instalação

### 📌 Requistos
Certifique-se de ter o Python 3 instalado em sua máquina. Caso não tenha, baixe e instale <a href="https://www.python.org/downloads/">aqui.</a>

### 📦 Instalando Bibliotecas necessárias

1. **Antes de rodar o projeto, instale as bibliotecas necessárias executando**:
     pip install pywin32
     pip install reportlab

## ✉️ Configuração do Envio de E-mails
          {
    "Destinatarios": "ministro@economia",
    "Cc": "Acessor@Ministro",
    "Assunto": "Análise do PIB dos Municípios e Estados Brasileiros",
    "Anexo": "Informe o caminho do anexo",
    "Body": [
        "<p>Prezado Ministro,</p>",
        "<p>Espero encontrá-lo bem!</p>",
        "<p>Segue o relatório atualizado com os dados do Produto Interno Bruto (PIB) dos principais municípios e estados brasileiros.</p>",
        "<a href='https://app.powerbi.com/groups/me/reports/2cf50fb9-19e4-4d9e-911b-140146bfbe01?ctid=d193e68c-e53f-4610-a66d-56ff300fec7a&pbi_source=linkShare'>Relatório Interativo em PowerBi</a>",
        "<img src='PIB-Nacional-2020.jpg' />",
        "<p>Atenciosamente,<br>Matheus - Desenvolvedor FullStack e Analista</p>"
    ]
         }
- O uso do JSON torna o script mais flexível, permitindo a troca de informações de maneira dinâmica e personalizável.
- No meu projeto, simulei o envio de e-mail para o Ministro da Economia do Brasil. Mas, você pode construir o e-mail e explorar novos recursos, conforme as suas necessidades.

## 📌 Como usar

## ▶️ Funcionamento da Aplicação

## 👨‍💻 Desenvolvido por:

📌 Autor: Matheus Barbosa
- 🔗 Repositório: GitHub - MatheusBarb19
- 🔗 LinkedIn: https://www.linkedin.com/in/matheus-felix-barbosa-658422227
- 💡 Sugestões e melhorias são bem-vindas!
