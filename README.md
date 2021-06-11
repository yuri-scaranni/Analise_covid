# Modelo simples de ETL

Autor: **Yuri C. de Brito Scaranni**               
*19 de março, 2021*

 
**Resumo**:
*Como parte integrante do trabalho de conclusão de curso apresento esta abordagem didática sobre o funcionamento de um projeto ETL. O objetivo é realizar a coleta de dados referentes ao coronavirus no Brasil  no site [Our World In Data](https://ourworldindata.org/coronavirus-source-data) e através de scripts em Python, com um pouco de SQL, organizar uma estrutura que possibilite a análise desses dados.*
> Este trabalho foi desenvolvido utilizando python na versão 3.6.8.

# 1 - Extração
Extrair dados referentes ao COVID-19 e armazená-los em uma tabela dentro do banco de dados MySQL é o nosso objetivo, além disso precisamos garantir que somente dados novos sejam inseridos, sem duplicidade.

Para iniciar a extração precisamos da biblioteca ***requests***:  `pip install requests`. Com ela instalada podemos executar o código [extração](https://github.com/yuri-scaranni/Ciencia_de_dados/blob/main/extract.py "extract.py").
> python extract.py

Dentro do diretório `/download`estará o arquivo **covid19.csv**.

# 2 - Transformação

 A etapa de transformação serve para ajustarmos detalhes dos dados, corrigir falhas, excluir ou adicionar colunas, entre outras abordagens que podem ser necessárias para melhorar a análise. Para isso utilizaremos a biblitoeca ***pandas***, para isso antes vamos instalar a biblioteca: `pip install pandas`. Após a instalação podemos executar o script de [transformação](https://github.com/yuri-scaranni/Ciencia_de_dados/blob/main/transform.py "transform.py").
 > python transform.py

Dentro do diretório padrão estará o arquivo **covid19_brasil.csv**.
# 3 - Carga

O terceiro passo do processo é carregar os dados obtidos para uma base de dados relacional a fim de conseguirmos boas análises com *Query's* simples.
> Utilizamos neste trabalho o aplicativo **Wamp Server** para criar um servidor local com um banco de dados MySQL já instalado.
> **Wamp Server** pode ser obtido através do [link](https://www.wampserver.com/en/).

Precisamos de duas bibliotecas para isso:
 1. Instalar biblioteca SQLAlchemy `pip install sqlalchemy`.
 2. Instalar biblioteca PyMySQL `pip install pymysql`.

> Neste passo precisaremos que uma base de dados esteja disponível para uso, caso não exista, podemos criar através do comando `CREATE DATABASE estudo;` acessando o endereço `localhost` através do browser e posteriormente com o *PhpMyAdmin* disponibilizado pela ferramenta **Wamp Server**.

Com tudo instalado podemos executar o script de [Carga](https://github.com/yuri-scaranni/Ciencia_de_dados/blob/main/load.py "load.py").
> python load.py

# 4 - Visualização

O último script diz respeito a visualização gráfica utilizando **Seaborn** no **Python**, nele eu apresento 3 análises, os 30 países com maior número de óbitos por covid19 e após isso faço uma análise de casos e taxa de transmissão sobre os primeiros 5 países do gráfico de óbitos, sendo esses países EUA, Brasil, India, México e Reino Unido.
