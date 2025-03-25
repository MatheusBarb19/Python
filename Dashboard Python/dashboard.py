import pandas as pd
import matplotlib.pyplot as plt
import locale

#Lendo df com Pandas
df = pd.read_csv(r"C:\Users\importacao7\Desktop\Projetos\Projetos Python\Gráficos  Python\Municipios_brasileiros2020.csv")

# Configurar o local para Brasil (pt_BR)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

#1º Gráfico: Top 10 municipios com maior Pib
def top10_municipios(): #Cria um gráfico com o Top 10 municipios com maior PIB
    
    #REmove espaços em branco da coluna "Produto Interno Bruto" e converte para int
    df['PIB'] = df['Produto Interno Bruto\na preços correntes\n(1 000 R$)'].str.replace(' ', '').astype(int)

    # Ordenar pelos maiores PIBs e pegar o Top 10
    top_10 = df.sort_values(by='PIB', ascending=False).head(10)

    # Criar o gráfico de barras horizontais
    plt.figure(figsize=(9, 5))
    bars = plt.barh(top_10['Municípios e respectivas\nUnidades da Federação'], top_10['PIB'], color='royalblue')

    # Ajustar limite do eixo X para garantir espaço para os rótulos
    plt.xlim(0, top_10['PIB'].max() * 1.1)

    # Adicionar rótulos ao lado direito das barras
    for bar in bars:
        formatted_value = locale.currency(bar.get_width(), grouping=True)  # Formatar o valor como moeda brasileira
        plt.text(
            bar.get_width() + (top_10['PIB'].max() * 0.01),  # Coloca o rótulo um pouco além da barra
            bar.get_y() + bar.get_height() / 2,  # Centraliza verticalmente
            formatted_value,  # Exibe o valor formatado como moeda
            ha='left',  # Alinha o texto à esquerda
            va='center',  # Centraliza o rótulo verticalmente
            color='black',  # Define o texto preto para boa visibilidade
            fontweight='bold'  # Deixa o rótulo mais destacado
        )
        
    #configurar título e eixos
    plt.xlabel('PIB (em milhares de R$)') #define o nome do eixo X
    plt.ylabel('Municípios') #define o nome do eixo y
    plt.title('Top 10 Municípios com Maior PIB no Brasil') #define o título do gráfico
    plt.gca().invert_yaxis()  # Inverte o eixo Y para mostrar o maior no topo

    plt.show() #Exibe o gráfico 


#Distruibuição de PIB por Estado (Matriz)

def distr_PibUF():
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
distr_PibUF()
