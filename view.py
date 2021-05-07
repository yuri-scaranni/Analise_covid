import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('download/covid19.csv', sep=',')
df['data'] = pd.to_datetime(df['data'])


def indice_morte_milhao():
    #df2 = df.filter(['pais', 'data', 'total_mortes_por_milhao'])
    #
    # # Alterando coluna 'data' para somente Ano-Mês
    # df['data'] = df['data'].dt.to_period('M').apply(str)
    # # Agrupando paises por mês e fazendo a média de novos casos
    # df2 = df.groupby(['data', 'pais']).mean(['total_mortes_por_milhao']).round(2)

    print(df.columns)
    sns.set_theme(style='darkgrid')
    sns.barplot(data=df, x='data', y='total_mortes_por_milhao', hue='pais')
    plt.show()


def sa_mortes_total():
    df = pd.read_csv('download/covid19_SA.csv', sep=',')
    df['data'] = pd.to_datetime(df['data']).apply(lambda x: x.strftime('%Y-%m'))
    df = df.query('pais == ["Brazil", '
                  '"Argentina", '
                  '"Paraguay", '
                  '"Uruguay", '
                  '"Bolivia"]')
    sns.set_theme(style="darkgrid")
    sns.lineplot(data=df,
                 x='data',
                 y='mortes_totais',
                 hue='pais')
    plt.xlabel("Ano-Mês")
    plt.ylabel("Mortes Totais")
    plt.title("Acumulado de mortes ao longo do tempo.")
    plt.show()


def sa_casos_total():
    df = pd.read_csv('download/covid19_SA.csv', sep=',')
    df['data'] = pd.to_datetime(df['data']).apply(lambda x: x.strftime('%Y-%m'))
    df = df.query('pais == ["Brazil", '
                  '"Argentina", '
                  '"Paraguay", '
                  '"Uruguay", '
                  '"Bolivia"]')
    sns.lineplot(data=df, x='data', y='casos_totais', hue='pais')
    plt.xlabel("Ano-Mês")
    plt.ylabel("Casos Totais")
    plt.title("Acumulado de casos ao longo do tempo.")
    plt.show()


def sa_mortes_por_milhao():
    df = pd.read_csv('download/covid19_SA.csv', sep=',')
    df['data'] = pd.to_datetime(df['data']).apply(lambda x: x.strftime('%Y-%m'))
    df = df.query('pais == ["Brazil", '
                  '"Argentina", '
                  '"Paraguay", '
                  '"Uruguay", '
                  '"Bolivia"]')
    sns.lineplot(data=df,
                 x='data',
                 y='total_mortes_por_milhao',
                 hue='pais')
    plt.xlabel("Ano-Mês")
    plt.ylabel("Mortes")
    plt.title("Número de mortes por milhão de habitantes.")
    plt.show()


indice_morte_milhao()