import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('download/covid19_brics.csv', sep=',')
df['data'] = pd.to_datetime(df['data'])


def grafico_mortes_por_tempo():
    sns.set_theme(style="whitegrid")
    sns.lineplot(data=df, x='data', y='mortes_totais', hue='pais', palette="flare")
    plt.xlabel("Ano-Mês")
    plt.ylabel("Mortes Totais")
    plt.title("Acumulado de mortes ao longo do tempo.")
    plt.show()


def grafico_casos_total():
    sns.set_theme(style="darkgrid")
    grap = sns.lineplot(data=df, x='data', y='casos_totais', hue='pais')

    # Criando unidade Mi(milhão) no eixo Y
    from matplotlib.ticker import FuncFormatter
    f = lambda x, pos: f'{x / 10 ** 6:,.0f} Mi'
    grap.yaxis.set_major_formatter(FuncFormatter(f))

    plt.xlabel("Ano-Mês")
    plt.ylabel("Casos Totais")
    plt.title("Acumulado de casos ao longo do tempo.")
    plt.show()


def grafico_novos_casos():
    sns.set_theme(style="darkgrid")

    # Alterando coluna 'data' para somente Ano-Mês
    df['data'] = df['data'].dt.to_period('M').apply(str)
    # Agrupando paises por mês e fazendo a média de novos casos
    df_grouped = df.groupby(['data', 'pais']).mean('novos_casos').round(2)

    # Inserindo a paleta CMRmap para os 5 países do gráfico
    palette = sns.color_palette("CMRmap", 5)
    sns.lineplot(data=df_grouped, x='data', y='novos_casos', hue='pais', palette=palette)

    plt.xlabel("Ano-Mês")
    plt.ylabel("Novos casos")
    plt.title("Média mensal de novos casos registrados")
    plt.show()


def grafico_relacao_casos_x_mortes():
    sns.set_theme(style="whitegrid")

    df2 = df.filter(['pais', 'data', 'total_mortes_por_milhao', 'total_casos_por_milhao'])

    # Alterando coluna 'data' para somente Ano-Mês
    df2['data'] = df2['data'].dt.to_period('M').apply(str)
    # Agrupando paises por mês e fazendo a média de novos casos
    df_grouped = df2.groupby(['data', 'pais']).mean(['total_mortes_por_milhao', 'total_casos_por_milhao']).round(2)

    sns.scatterplot(data=df_grouped, x='total_mortes_por_milhao', y='total_casos_por_milhao', hue='pais')

    plt.xlabel("Mortes por milhão")
    plt.ylabel("Casos por milhão")
    plt.title("Relação Casos x Mortes")
    plt.show()


def grafico_relacao_pib_x_mortes():
    df = pd.read_csv('download/covid19.csv', sep=',')
    df['data'] = pd.to_datetime(df['data'])

    df2 = df.sort_values(by='pib_per_capita')
    df2 = df2.loc[df2['data'] == max(df2['data'])]
    df2 = df2.filter(['pais', 'pib_per_capita', 'total_mortes_por_milhao', 'continente'])

    sns.set_theme(style="darkgrid")
    sns.scatterplot(data=df2, x='pib_per_capita', y='total_mortes_por_milhao', hue='continente')

    plt.xlabel("PIB per capita")
    plt.ylabel("Mortes por milhão de habitantes")
    plt.title("Relação entre milhão de mortos e PIB do pais - Agrupados por continente")
    plt.show()

grafico_relacao_pib_x_mortes()