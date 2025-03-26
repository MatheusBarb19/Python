import pandas as pd
import matplotlib.pyplot as plt
import locale
import seaborn as sns

#Lendo df com Pandas
df = pd.read_csv(r"C:\Users\importacao7\Desktop\Projetos\Projetos Python\Gráficos  Python\Municipios_brasileiros2020.csv")

# Configurar o local para Brasil (pt_BR)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# 1º Gráfico: Top 10 municípios com maior PIB
def top10_municipios():  # Define uma função que gera o gráfico dos 10 municípios com maior PIB

    # Remove espaços em branco da coluna "Produto Interno Bruto" e converte os valores para inteiro
    df['PIB'] = df['Produto Interno Bruto\na preços correntes\n(1 000 R$)'].str.replace(' ', '').astype(int)

    # Ordena o DataFrame pelo PIB em ordem decrescente e pega os 10 primeiros registros (Top 10)
    top_10 = df.sort_values(by='PIB', ascending=False).head(10)

    # Define o tamanho da figura para melhor visualização (largura 9, altura 5)
    plt.figure(figsize=(10, 6))

    # Cria um gráfico de barras horizontais, com barras na cor laranja
    bars = plt.barh(top_10['Municípios e respectivas\nUnidades da Federação'], top_10['PIB'], color='orange')

    # Define o limite do eixo X para garantir espaço extra à direita das barras (10% a mais)
    plt.xlim(0, top_10['PIB'].max() * 1.1)

    # Adiciona rótulos de valor ao lado direito das barras
    for bar in bars:
        formatted_value = locale.currency(bar.get_width(), grouping=True)
        plt.text(
            bar.get_width() + (top_10['PIB'].max() * 0.1), # traz o rótulo um pouco para dentro da barra.
            bar.get_y() + bar.get_height() / 2,
            formatted_value,
            ha='right',
            va='center',
            color='black',
            fontsize=8  # Define o tamanho da fonte menor
    )

    plt.xlabel('PIB (em milhares de R$)')# Define o rótulo do eixo X
    plt.ylabel('Municípios') # Define o rótulo do eixo Y
    plt.title('Top 10 Municípios com Maior PIB no Brasil')# Define o título do gráfico
    plt.gca().invert_yaxis() # Inverte o eixo Y para que o maior valor fique no topo do gráfico
    plt.show() # Exibe o gráfico gerado

#2º Gráfico: Top 5 Estados com maior PIB
def top5_estados():
    top_5_estados = pib_por_estado.head(5)
    
    plt.figure(figsize=(9, 5))
    bars_top5 = plt.barh(top_5_estados.index, top_5_estados.values, color='orange')
    
    # Adicionar rótulos para o Top 5
    for bar in bars_top5:
        plt.text(bar.get_width() + 10, bar.get_y() + bar.get_height()/2,
                 f'{int(bar.get_width()):,}M', 
                 ha='right', 
                 va='center', 
                 fontsize=8)
    
    plt.xlabel('PIB (em milhões de R$)')
    plt.ylabel('Estados')
    plt.title('Top 5 Estados com Maior PIB no Brasil')
    plt.gca().invert_yaxis()
    
    plt.tight_layout()
    plt.show()

#3º Grafico: Participação de cada Estado no PIB Nacional
def part_estado():
    # Remover espaços em branco da coluna do PIB e converter para numérico
    df['PIB'] = df['Produto Interno Bruto\na preços correntes\n(1 000 R$)'].str.replace(' ', '').astype(int)
    
    # Extrair apenas a sigla do estado São Paulo (SP)
    df['Estado'] = df['Municípios e respectivas\nUnidades da Federação'].str.extract(r'\((\w{2})\)')
    
    # Agrupar por Estado e somar o PIB dos municípios
    pib_por_estado = df.groupby('Estado')['PIB'].sum()
    
    # Calcular a participação percentual de cada estado no PIB total do Brasil
    pib_total_brasil = pib_por_estado.sum() #PIB total do brasil (somando todos os estados)
    pib_por_estado_percentual = (pib_por_estado / pib_total_brasil) * 100 #calculando a participação de cada estado no PIB total

    pib_por_estado_percentual = pib_por_estado_percentual.sort_values(ascending=False)#Ordenar do Maior para o Menor
    
    # Criar gráfico de barras horizontais
    plt.figure(figsize=(8, 5))
    sns.barplot(x=pib_por_estado_percentual, y=pib_por_estado_percentual.index,color='orange')
    plt.xlabel('Participação no PIB (%)')
    plt.ylabel('Estado')
    plt.title('Participação de Cada Estado no PIB Total do Brasil')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    
    # Adicionar rótulos com os valores percentuais
    for index, value in enumerate(pib_por_estado_percentual):
        plt.text(value + 2, index, f"{value:.1f}%", 
        va="center", 
        ha="right",
        fontsize=8
        )

#Distruibuição de PIB por Estado (Matriz)
def distribuicao_PibUF():
    # Definir a localidade para o Brasil (pt_BR)
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    # Separar o estado da coluna 'Municípios e respectivas Unidades da Federação'
    df['Estado'] = df['Municípios e respectivas\nUnidades da Federação'].str.extract(r'\((\w+)\)')

    # Limpar e converter a coluna de PIB para número (removendo espaços e convertendo para inteiro)
    df['PIB'] = df['Produto Interno Bruto\na preços correntes\n(1 000 R$)'].str.replace(' ', '').astype(int)

    # Agrupar o PIB total por estado
    pib_por_estado = df.groupby('Estado')['PIB'].sum().sort_values(ascending=False)

    # Criar a matriz (DataFrame) com o PIB por estado
    matriz = pd.DataFrame({
        'Estado': pib_por_estado.index,
        'PIB (milhares de R$)': pib_por_estado.values
    })

    # Estilizando a matriz e aplicando a formatação de moeda com a localidade
    styled_matriz = matriz.style.format({
        'PIB (milhares de R$)': lambda x: locale.currency(x, grouping=True)  # Formatação de moeda brasileira
    })

    # Alterando o estilo para colorir as linhas alternadas
    styled_matriz = styled_matriz.set_table_styles([
        {'selector': 'thead th', 'props': [('background-color', '#2c3e50'), ('color', 'white')]},  # Cor de fundo do cabeçalho
        {'selector': 'tbody tr:nth-child(odd)', 'props': [('background-color', '#ecf0f1')]},  # Cor de fundo para linhas ímpares
        {'selector': 'tbody tr:nth-child(even)', 'props': [('background-color', '#bdc3c7')]},  # Cor de fundo para linhas pares
        {'selector': 'tbody tr:hover', 'props': [('background-color', '#95a5a6')]},  # Cor de fundo ao passar o mouse
        {'selector': 'td, th', 'props': [('padding', '8px'), ('border', '1px solid #ccc')]},  # Bordas e espaçamento
    ])
    
    return styled_matriz  # Retorne o styled_matriz para exibição ou uso

#chamando as funções
top10_municipios()
top5_estados()
part_estado()
distribuicao_PibUF()

