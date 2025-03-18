# 🔍 Web Scraping no Mercado Livre

## 📌 Descrição

Este script em Python utiliza `Selenium` para automatizar a pesquisa de produtos no Mercado Livre, extraindo informações como nome, preço e avaliação dos produtos exibidos na página de resultados. Os dados coletados são armazenados em um arquivo Excel para futura análise.

## 🚀 Funcionalidades

- Realiza buscas automáticas no Mercado Livre com base em um termo inserido pelo usuário.
- Extrai informações de nome, preço e avaliação dos produtos.
- Salva os dados coletados em um arquivo Excel (`Pesquisa_MercadoLivre.xlsx`).
- Implementa tratamento de erros para garantir que o script funcione mesmo diante de elementos ausentes.

## 🛠 Tecnologias Utilizadas

- Python 3
- `selenium` (automação do navegador)
- `pandas` (manipulação de dados e exportação para Excel)
- `chromedriver` (driver para o navegador Chrome)

## ⚙️ Configuração

Antes de executar o script, certifique-se de ter os seguintes requisitos instalados:

1. **Python 3** instalado em sua máquina.
2. **Bibliotecas necessárias** (instale com o seguinte comando):
   ```bash
   pip install selenium pandas openpyxl
   ```
3. **Chromedriver compatível com a versão do Google Chrome**. Baixe em: [ChromeDriver](https://sites.google.com/chromium.org/driver/)
4. Adicione o caminho do `chromedriver.exe` ao PATH do sistema ou coloque-o na mesma pasta do script.

## ▶️ Como Usar

1. **Execute o script no terminal ou prompt de comando**:
   ```bash
   python Pesquisa_MercadoLivre.py
   ```
2. **Digite o nome ou código do produto** quando solicitado.
3. **Aguarde a extração dos dados** e confira o arquivo gerado `Pesquisa_MercadoLivre.xlsx`.

## 📂 Estrutura de Arquivos

```
WebScraping_ML/
│-- scraping_mercadolivre.py
│-- Pesquisa_MercadoLivre.xlsx (gerado automaticamente)
```

## 📜 Exemplo de Saída no Excel

| Produto               | Preço      | Avaliação    |
|----------------------|-----------|-------------|
| Smartphone XYZ      | R$ 2.499  | 4.7 |
| Notebook ABC        | R$ 5.999  | 4.5 |
| Fone de Ouvido DEF  | R$ 199    | Sem avaliação|

## 🔥 Melhorias Futuras

- Captura de links dos produtos.
- Paginação automática para coletar mais resultados.
- Integração com Google Sheets para armazenar dados online.

## 📄 Licença

Este projeto é de uso livre e pode ser modificado conforme necessário.

---
🚀 Desenvolvido para facilitar a extração de dados do Mercado Livre!

