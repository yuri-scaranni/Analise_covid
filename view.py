import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

"""
SA - SOUTH AMÉRICA
"""

def sa_mortes_total_por_mes():
    dataframe = pd.read_csv('download/covid19_SA.csv', sep=',')
    dataframe['data'] = pd.to_datetime(dataframe['data']).apply(lambda x: x.strftime('%Y-%m'))
    dataframe = dataframe.query('pais == ["Brazil", "Argentina", "Paraguay", "Uruguay", "Bolivia"]')
    sns.set_theme(style="whitegrid")
    sns.lineplot(data=dataframe, x='data', y='mortes_totais', hue='pais', palette="flare")
    plt.xlabel("Ano-Mês")
    plt.ylabel("Mortes Totais")
    plt.title("Acumulado de mortes ao longo do tempo.")
    plt.show()


def sa_casos_total_por_mes():
    dataframe = pd.read_csv('download/covid19_SA.csv', sep=',')
    dataframe['data'] = pd.to_datetime(dataframe['data']).apply(lambda x: x.strftime('%Y-%m'))
    dataframe = dataframe.query('pais == ["Brazil", "Argentina", "Paraguay", "Uruguay", "Bolivia"]')
    sns.lineplot(data=dataframe, x='data', y='casos_totais', hue='pais')
    plt.xlabel("Ano-Mês")
    plt.ylabel("Casos Totais")
    plt.title("Acumulado de casos ao longo do tempo.")
    plt.show()


def sa_mortes_por_milhao():
    dataframe = pd.read_csv('download/covid19_SA.csv', sep=',')
    dataframe['data'] = pd.to_datetime(dataframe['data']).apply(lambda x: x.strftime('%Y-%m'))
    dataframe = dataframe.query('pais == ["Brazil", "Argentina", "Paraguay", "Uruguay", "Bolivia"]')
    sns.lineplot(data=dataframe, x='data', y='total_mortes_por_milhao', hue='pais')
    plt.show()