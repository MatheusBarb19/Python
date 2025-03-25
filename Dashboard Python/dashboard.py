import pandas as pd
import matplotlib.pyplot as plt

#Lendo df com Pandas
df = pd.read_csv(r"C:\Users\mathe\Documents\GitHub\Python\Dashboard Python\Municipios_brasileiros2020.csv")

#top 10 municipios com maior Pib

# Limpar e formatar a coluna de PIB
df['PIB'] = df['Produto Interno Bruto\na preços correntes\n(1 000 R$)'].str.replace(' ', '').astype(int)

# Ordenar pelos maiores PIBs e selecionar o Top 10
top_10 = df.sort_values(by='PIB', ascending=False).head(10)

# Criar o gráfico de barras
plt.figure(figsize=(10, 6))
plt.barh(top_10['Municípios e respectivas\nUnidades da Federação'], top_10['PIB'], color='royalblue')
plt.xlabel('PIB (em milhares de R$)')
plt.ylabel('Municípios')
plt.title('Top 10 Municípios com Maior PIB no Brasil')
plt.gca().invert_yaxis()  # Inverte o eixo Y para mostrar o maior no topo
plt.show()

                                                        
#Distribuição de PIB por estado

#Concetração de Riqueza

#Comparação entre municipios

#Distribuição do Pib