# 📧 Envio de E-mails Automatizado

## 🎯 Objetivo:
Este projeto tem como objetivo automatizar o envio de e-mails utilizando Python. O script gera um arquivo JSON, permitindo que o usuário personalize facilmente as configurações do e-mail, como:

✅ Destinatário(s)
✅ Destinatário(s) em cópia (CC)
✅ Assunto
✅ Anexo(s)
✅ Corpo do e-mail

Com essa abordagem, o envio de e-mails se torna mais dinâmico, eficiente e facilmente integrável a outros sistemas.

## 🛠 Tecnologias Utilizadas

- Win32 -> Permite interagir com a API do Windows.
- Json -> Manipulação de arquivos json.
- OS -> Manipulação do sistema operacional.

## 📦 Instale bibliotecas necessárias:
         pip install pywin32
⚠️ A biblioteca JSON já vem integrada ao Python, portanto, não é necessário instalá-la separadamente.

## 📚 Exemplo do arquivo desnatario.json

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

## 👨‍💻 Desenvolvido por:

📌 Autor: Matheus Barbosa
- 🔗 Repositório: GitHub - MatheusBarb19
- 🔗 LinkedIn: https://www.linkedin.com/in/matheus-felix-barbosa-658422227
- 💡 Sugestões e melhorias são bem-vindas!
