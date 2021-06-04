import seaborn as sns
from datetime import timedelta
import pandas as pd
import matplotlib.pyplot as plt


def mortes_covid_top_30():
    df = pd.read_csv('download/covid19_renamed.csv', sep=',')
    df['data'] = pd.to_datetime(df['data'])
    df = df.dropna(subset=['continente'])
    yesterday = max(df['data']) - timedelta(days=1)
    df = df.loc[df['data'] == yesterday]
    df = df.sort_values(by='mortes_totais', ascending=False).head(30)
    sns.set_theme(style="darkgrid")
    palette = sns.color_palette("Wistia", 30)
    sns.barplot(data=df,
                x='mortes_totais',
                y='pais',
                orient='h',
                palette=palette)
    plt.xlabel("Óbitos totais")
    plt.ylabel("Países")
    plt.title("Ranking óbitos covid")
    plt.xticks(rotation=90)
    plt.show()


def casos_totais_ao_longo_do_tempo():
    df = pd.read_csv('download/covid19_renamed.csv', sep=',')
    df['data'] = pd.to_datetime(df['data'])
    df = df.dropna(subset=['continente'])
    paises_selecionados = ['United States', 'Brazil', 'India', 'Mexico', 'United Kingdom']
    df = df.loc[df['pais'].isin(paises_selecionados)]
    sns.set_theme(style="darkgrid")
    grap = sns.lineplot(data=df,
                        x='data',
                        y='casos_totais',
                        hue='pais',
                        palette="CMRmap_r")
    from matplotlib.ticker import FuncFormatter
    f = lambda x, pos: f'{x / 10 ** 6:,.0f} Mi'
    grap.yaxis.set_major_formatter(FuncFormatter(f))
    plt.xlabel("Ano-Mês")
    plt.ylabel("Total de casos")
    plt.title("Linha temporal do total de casos de covid")
    plt.show()


def indice_reproducao():
    df = pd.read_csv('download/covid19_renamed.csv', sep=',')
    df['data'] = pd.to_datetime(df['data'])
    df = df.dropna(subset=['continente'])
    paises_selecionados = ['United States', 'Brazil', 'India', 'Mexico', 'United Kingdom']
    df = df.loc[df['pais'].isin(paises_selecionados)]
    sns.set_theme(style='darkgrid')
    sns.lineplot(data=df,
                 x='data',
                 y='taxa_transmissao',
                 hue='pais',
                 linewidth=1.1,
                 palette='tab10')
    plt.xlabel("Ano-Mês")
    plt.ylabel("Taxa de reprodução")
    plt.title("Taxa de transmissão ao longo do temppo")
    plt.show()
