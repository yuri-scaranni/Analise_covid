import seaborn as sns
from datetime import timedelta
import pandas as pd
import matplotlib.pyplot as plt


def mortes_covid_top_50():
    # Abrindo arquivo e estabelecendo 'data' como tipo datetime
        df = pd.read_csv('download/covid19_renamed.csv', sep=',')
        df['data'] = pd.to_datetime(df['data'])
    # Extraindo somente o último dia disponível
        yesterday = max(df['data']) - timedelta(days=1)
        df = df.loc[df['data'] == yesterday]
    # Removendo linhas onde o continente
    # Não está preenchido
        df = df.dropna(subset=['continente'])
    # Ordenando pelo campo 'mortes_totais' e limitando
    # Aos 50 primeiros registros
        df = df.sort_values(by='mortes_totais', ascending=False).head(50)
    # Plotagem do gráfico de barras
        sns.set_theme(style="darkgrid")
        palette = sns.color_palette("Wistia", 50)
        sns.barplot(data=df,
                    x='pais',
                    y='mortes_totais',
                    palette=palette)

        plt.xlabel("Países")
        plt.ylabel("Mortes totais")
        plt.title("Ranking mortes covid")
        plt.xticks(rotation=90)
        plt.show()


def casos_totais_ao_longo_do_tempo():
    # Abrindo arquivo e estabelecendo 'data' como tipo datetime
        df = pd.read_csv('download/covid19_renamed.csv', sep=',')
        df['data'] = pd.to_datetime(df['data'])
    # Removendo linhas onde o continente
    # Não está preenchido
        df = df.dropna(subset=['continente'])
    # Selecionando paises que até a data válida
    # mais próxima eram os top 5 recordistas de casos
        yesterday = max(df['data']) - timedelta(days=1)
        df_drop = df.loc[df['data'] == yesterday]
        df_drop = df_drop.sort_values(by='casos_totais', ascending=False).head(5)
        df_drop = df_drop['pais'].drop_duplicates()
        df = df[df['pais'].isin(df_drop)].sort_values(by='data')
    # Transformando data comum em apenas ano e mês
        df['data'] = df['data'].dt.to_period('M').apply(str)
    # Plotagem do gráfico de linhas
        sns.set_theme(style="whitegrid")
        grap = sns.lineplot(data=df, x='data', y='casos_totais', hue='pais')
    # Criando unidade Mi(milhões) no eixo Y
        from matplotlib.ticker import FuncFormatter
        f = lambda x, pos: f'{x / 10 ** 6:,.0f} Mi'
        grap.yaxis.set_major_formatter(FuncFormatter(f))
        plt.xlabel("Ano-Mês")
        plt.ylabel("Total de casos")
        plt.title("Linha temporal do total de casos de covid")
        plt.show()


def relacao_casos_x_mortes():
    # Abrindo arquivo e estabelecendo 'data' como tipo datetime
        df = pd.read_csv('download/covid19_renamed.csv', sep=',')
        df['data'] = pd.to_datetime(df['data'])
    # Removendo linhas onde o continente
    # Não está preenchido
        df = df.dropna(subset=['continente'])
    # Selecionando paises que até a data válida
    # mais próxima eram os top 5 recordistas de casos
        yesterday = max(df['data']) - timedelta(days=1)
        df_drop = df.loc[df['data'] == yesterday]
        df_drop = df_drop.sort_values(by='casos_totais', ascending=False)
        df_drop = df_drop['pais'].drop_duplicates()
        df = df[df['pais'].isin(df_drop)].sort_values(by='data')

    # Filtrando colunas
        yesterday = max(df['data']) - timedelta(days=1)
        df = df.loc[df['data'] == yesterday]
        df = df.filter(['data', 'pais', 'mortes_totais', 'casos_totais'])
    # Plotando relação
        sns.set_theme(style="ticks")
        grap = sns.scatterplot(data=df, x='mortes_totais', y='casos_totais')

    # Criando unidade Mi(milhões) no eixo Y
        from matplotlib.ticker import FuncFormatter
        f = lambda x, pos: f'{x / 10 ** 6:,.0f} Mi'
        grap.yaxis.set_major_formatter(FuncFormatter(f))

        plt.xlabel("Total de mortos")
        plt.ylabel("Total de casos")
        plt.title("Relação Casos x Mortes")
        plt.show()

relacao_casos_x_mortes()