"""
    LOAD
    Com a biblioteca sqlalchemy + pymysql abrimos conexão com um banco de dados MySQL e inserimos os dados dentro de uma
    tabela neste banco, caso as tabelas/schema não existam nós criamos.
"""
from sqlalchemy import create_engine
import pandas as pd

# Dados de conexão local
conn = {'host': 'localhost', 'user': 'root', 'pass': '', 'database': 'analise_covid'}

# Criando conexão
engine = create_engine(f'mysql+pymysql://{conn["user"]}:{conn["pass"]}@{conn["host"]}/{conn["database"]}')

# Abrindo arquivo de dados transformados
data = pd.read_csv('download/covid19_SA.csv', sep=',', encoding='utf-8', index_col=False)

# Insere os dados
data.to_sql(name='covid_19', con=engine, schema=conn["database"], if_exists='replace', index=False)

