# 🔍 Web Scraper - Mercado Livre

## 📌 Descrição

Este script em Python utiliza Selenium para automatizar a busca de produtos no Mercado Livre, coletando informações como nome, preço e avaliação, e salvando os dados em um arquivo Excel.

## 🚀 Funcionalidades

- Pesquisa automática de produtos no Mercado Livre.
- Coleta nome, preço e avaliação dos produtos.
- Salva os dados extraídos em um arquivo `.xlsx`.
- Utiliza Selenium para navegação e extração de dados.

## 🛠 Tecnologias Utilizadas

- Python 3
- Selenium (automação de navegador)
- Pandas (manipulação e exportação de dados)
- Chrome WebDriver

## 📂 Estrutura de Arquivos

```
WebScraper_MercadoLivre/
│-- scraper.py
│-- Pesquisa_MercadoLivre.xlsx (arquivo gerado com os dados)
```

## ⚙️ Configuração

1. **Instale as dependências necessárias**:
   ```bash
   pip install selenium pandas
   ```
2. **Baixe o Chrome WebDriver** compatível com sua versão do Chrome e adicione-o ao PATH.

## ▶️ Como Usar

1. **Execute o script**:
   ```bash
   python scraper.py
   ```
2. **Digite o nome ou código do produto** que deseja pesquisar.
3. O script abrirá o navegador, fará a pesquisa e salvará os dados em `Pesquisa_MercadoLivre.xlsx`.

## 📜 Exemplo de Dados Extraídos

| Produto | Preço | Avaliação |
|---------|-------|-----------|
| Teclado Mecânico RGB | R$ 199,90 | 4.8 ⭐ |
| Mouse Gamer XYZ | R$ 129,99 | 4.5 ⭐ |

## 🔥 Melhorias Futuras

- Suporte para múltiplas páginas de resultados.
- Exportação dos dados para banco de dados.
- Integração com APIs para notificações automatizadas.

## 📄 Licença

Este projeto é de uso livre e pode ser modificado conforme necessário.

---

🚀 Desenvolvido para facilitar a pesquisa de produtos e análise de preços no Mercado Livre!

