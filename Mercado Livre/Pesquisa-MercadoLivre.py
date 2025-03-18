import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Função principal que pesquisa um produto no Mercado Livre
def pesquisa_mercadolivre(codigo): #Passa o código inserido pelo usuário como parametro
    
    # Configurando opções do Chrome para ignorar erros e evitar ser detectado como robô
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')  # Ignora erros de certificado SSL
    chrome_options.add_argument('--ignore-ssl-errors=yes')  # Ignora erros relacionados ao SSL
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')  # Tenta ocultar que é uma automação
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Evita mensagens desnecessárias no terminal

    # Inicializa o navegador com as opções configuradas
    driver = webdriver.Chrome(options=chrome_options)
    
    # Acessa o site do Mercado Livre
    driver.get("https://www.mercadolivre.com.br/")
    
    # Espera 2 segundos para garantir que a página carregue completamente
    time.sleep(2)
    
    # Localiza o campo de pesquisa pelo XPATH
    campo_pesquisa = driver.find_element(By.XPATH, '//*[@id="cb1-edit"]')
    campo_pesquisa.clear()  # Limpa o campo de pesquisa
    campo_pesquisa.send_keys(codigo)  # Insere o código ou nome do produto
    campo_pesquisa.send_keys(Keys.RETURN)  # Pressiona Enter para buscar
    
    # Espera até que os anúncios apareçam na página, com tempo máximo de 20 segundos
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, '//li[contains(@class, "ui-search-layout__item")]')) #Acessa a Class de contem todos os anuncios
        )
        print("Anúncios carregados com sucesso!")
    except Exception as e:
        print(f"Erro ao carregar anúncios: {e}")
    
    # Coleta todos os anúncios exibidos na página
    anuncios = driver.find_elements(By.XPATH, '//li[contains(@class, "ui-search-layout__item")]') #Acessa a Class de contem todos os anuncios
    
    # Cria listas vazias para armazenar os dados coletados
    produtos = []
    precos = []
    avaliacao = []
    
    # Loop para percorrer cada anúncio encontrado
    for anuncio in anuncios:
        try:
            # Tenta capturar o nome do produto
            nome_produto = anuncio.find_element(By.XPATH, './/h3[@class="poly-component__title-wrapper"]').text #Acessa a classe que cotem os nomes do anuncios
            produtos.append(nome_produto) #adciona dentro da lista
            
            # Tenta capturar o preço do produto
            try:
                preco_produto = anuncio.find_element(By.XPATH, './/span[contains(@class, "andes-money-amount andes-money-amount--cents-superscript")]').text        
            except:
                preco_produto = "N/A"  # Se não encontrar o preço, define como "N/A"
            precos.append(preco_produto) #adciona dentro da lista
    
            # Tenta capturar a avaliação do produto
            try: 
                avaliacao_produto = anuncio.find_element(By.XPATH, './/span[contains(@class, "poly-reviews__rating")]').text #acessa a class que contem as avalicões dos anuncios
            except:
                avaliacao_produto = "Sem avaliação"  # Se não encontrar avaliação, define como "Sem avaliação"
            avaliacao.append(avaliacao_produto) #adciona dentro da lista
            
        except Exception as e:
            # Se der erro ao capturar qualquer dado, preenche com "N/A"
            print(f"Erro ao capturar dados de um anúncio: {e}")
            #Inserando na lista como N/A
            produtos.append("N/A") 
            precos.append("N/A")
            avaliacao.append("N/A")
    
    # Cria uma tabela (DataFrame) com os dados coletados
    dados = pd.DataFrame({
        "Produto": produtos,
        "Preço": precos,
        "Avaliação": avaliacao
    })
    
    # Salva a tabela em um arquivo Excel
    dados.to_excel("Pesquisa_MercadoLivre.xlsx", index=False) #salva o DF como Excel
    
    print("Dados salvos com sucesso!")
    print("Encerrando processo!")
    
    # Espera mais 3 segundos antes de fechar o navegador
    time.sleep(3)
    
    # Fecha o navegador
    driver.quit() 

# Solicita ao usuário o nome ou código do produto que deseja pesquisar
codigo = input("Insira o código ou nome do produto que será pesquisado: ")
pesquisa_mercadolivre(codigo)
