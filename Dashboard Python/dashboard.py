import pandas as pd
import matplotlib.pyplot as plt
import locale
import seaborn as sns


# Lendo df com Pandas
df = pd.read_csv(r"C:\Users\mathe\Documents\GitHub\Python\Dashboard Python\Municipios_brasileiros2020.csv")

# Configurar o local para Brasil (pt_BR)
try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')

# Pré-processamento dos dados
df['PIB'] = df['Produto Interno Bruto\na preços correntes\n(1 000 R$)'].str.replace(' ', '').astype(int)
df['Estado'] = df['Municípios e respectivas\nUnidades da Federação'].str.extract(r'\((\w{2})\)')

# Agrupar PIB por Estado
pib_por_estado = df.groupby('Estado')['PIB'].sum().sort_values(ascending=False)

# 1º Gráfico: Top 10 municípios com maior PIB
def top10_municipios():
    top_10 = df.sort_values(by='PIB', ascending=False).head(10)

    plt.figure(figsize=(10, 6))
    bars = plt.barh(top_10['Municípios e respectivas\nUnidades da Federação'], top_10['PIB'], color='orange')
    plt.xlim(0, top_10['PIB'].max() * 1.1)

    for bar in bars:
        formatted_value = locale.currency(bar.get_width(), grouping=True)
        plt.text(bar.get_width() + (top_10['PIB'].max() * 0.05),
                 bar.get_y() + bar.get_height() / 2,
                 formatted_value,
                 ha='left',
                 va='center',
                 color='black',
                 fontsize=8)

    plt.xlabel('PIB (em milhares de R$)')
    plt.ylabel('Municípios')
    plt.title('Top 10 Municípios com Maior PIB no Brasil')
    plt.gca().invert_yaxis()
    plt.show()

# 2º Gráfico: Top 5 Estados com maior PIB
def top5_estados():
    top_5_estados = pib_por_estado.head(5)

    plt.figure(figsize=(9, 5))
    bars_top5 = plt.barh(top_5_estados.index, top_5_estados.values, color='orange')

    for bar in bars_top5:
        plt.text(bar.get_width() + 10, bar.get_y() + bar.get_height() / 2,
                 f'{bar.get_width():,}M',
                 ha='left',
                 va='center',
                 fontsize=8)

    plt.xlabel('PIB (em milhões de R$)')
    plt.ylabel('Estados')
    plt.title('Top 5 Estados com Maior PIB no Brasil')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

# 3º Gráfico: Participação de cada Estado no PIB Nacional
def part_estado():
    pib_total_brasil = pib_por_estado.sum()
    pib_por_estado_percentual = (pib_por_estado / pib_total_brasil) * 100

    plt.figure(figsize=(8, 5))
    sns.barplot(x=pib_por_estado_percentual, y=pib_por_estado_percentual.index, color='orange')

    plt.xlabel('Participação no PIB (%)')
    plt.ylabel('Estado')
    plt.title('Participação de Cada Estado no PIB Total do Brasil')
    plt.grid(axis='x', linestyle='--', alpha=0.7)

    for index, value in enumerate(pib_por_estado_percentual):
        plt.text(value + 0.5, index, f"{value:.1f}%", va="center", ha="left", fontsize=8)

    plt.tight_layout()
    plt.show()

# 4º Gráfico: Distribuição de PIB por Estado (Matriz)
def distribuicao_PibUF():
    matriz = pd.DataFrame({
        'Estado': pib_por_estado.index,
        'PIB (milhares de R$)': pib_por_estado.values
    })

    styled_matriz = matriz.style.format({
        'PIB (milhares de R$)': lambda x: locale.currency(x, grouping=True)
    })

    styled_matriz = styled_matriz.set_table_styles([
        {'selector': 'thead th', 'props': [('background-color', '#2c3e50'), ('color', 'white')]},
        {'selector': 'tbody tr:nth-child(odd)', 'props': [('background-color', '#ecf0f1')]},
        {'selector': 'tbody tr:nth-child(even)', 'props': [('background-color', '#bdc3c7')]},
        {'selector': 'tbody tr:hover', 'props': [('background-color', '#95a5a6')]},
        {'selector': 'td, th', 'props': [('padding', '8px'), ('border', '1px solid #ccc')]},
    ])

    return styled_matriz

# Chamando as funções
top10_municipios()
top5_estados()
part_estado()

distribuicao_PibUF()
