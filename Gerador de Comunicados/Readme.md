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

## 📦 Instalando Bibliotecas necessárias
     pip install pywin32
     pip install reportlab

## ✉️ Configuração do Envio de E-mails
          {
    "Destinatarios": ["Destinatário1", "Destinatário2"],
    "Assunto": "Comunicado de Alteração",
    "Cc": "",
    "Anexo": "",
    "Corpo-email": [
        "<a>Prezados colaboradores, </a>",
        "<p>Informamos que um novo documento foi gerado e está disponível em anexo.</p>",
        "<p>Este documento contém informações detalhadas sobre as alterações realizadas em códigos, similaridade ou aplicação de [produto/código/referência].</p><br>",
        "<p>Atenciosamente,</p>",
        "<p>MB PROJECTS</p>"
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
