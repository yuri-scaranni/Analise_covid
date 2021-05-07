import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta


def mortes_covid_top_15():
    df = pd.read_csv('download/covid19.csv', sep=',')
    df['data'] = pd.to_datetime(df['data'])
    yesterday = max(df['data']) - timedelta(days=1)
    df = df.loc[df['data'] == yesterday]
    df = df.dropna(subset=['continente'])
    df = df.sort_values(by='mortes_totais', ascending=False).head(15)
    df = df.filter(['pais', 'mortes_totais'])

    sns.set_theme(style="darkgrid")
    palette = sns.color_palette("Wistia", 15)
    ax = sns.barplot(data=df, x='pais', y='mortes_totais', palette=palette)

    for p in ax.patches:
        ax.annotate('{}'.format(int(p.get_height())),
                    (p.get_x() + 0.12, p.get_height() + 2000),
                    size=10)

    plt.xlabel("Países")
    plt.ylabel("Mortes totais")
    plt.title("Ranking mortes covid")
    plt.xticks(rotation=45)
    plt.show()


def ranking_vacinados():
    df = pd.read_csv('download/covid19.csv', sep=',')
    df['data'] = pd.to_datetime(df['data'])
    yesterday = max(df['data']) - timedelta(days=1)
    df = df.loc[df['data'] == yesterday]
    df = df.dropna(subset=['continente'])
    df = df.sort_values(by=['total_vacinas'], ascending=False).head(15)
    df = df.filter(['pais', 'total_vacinacao_por_centena', 'total_vacinas'])



    ax = plt.subplots()

    ax = sns.barplot(data=df, x='pais', y='total_vacinacao_por_centena', color='b', label='Total de vacinados')
    ax = sns.barplot(data=df, x='pais', y='total_vacinas', color='r', label='Total de vacinas')
    # Criando unidade Mi(milhão) no eixo Y
    from matplotlib.ticker import FuncFormatter
    f = lambda x, pos: f'{x / 10 ** 6:,.0f} Mi'
    ax.yaxis.set_major_formatter(FuncFormatter(f))

    plt.xlabel("Países")
    plt.legend()
    plt.ylabel("")
    plt.title("Ranking de vacinas - Top 15")
    plt.xticks(rotation=45)
    plt.show()


ranking_vacinados()


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


