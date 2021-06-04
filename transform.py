import pandas as pd

campos_nome = {
"iso_code":"codigo_iso",
"continent":"continente",
"location":"pais",
"date":"data",
"total_cases":"casos_totais",
"new_cases":"novos_casos",
"total_deaths":"mortes_totais",
"new_deaths":"novas_mortes",
"total_cases_per_million":"total_casos_por_milhao",
"new_cases_per_million":"novos_casos_por_milhao",
"total_deaths_per_million":"total_mortes_por_milhao",
"new_deaths_per_million":"novas_mortes_por_milhao",
"reproduction_rate":"taxa_transmissao",
"new_tests":"novos_testes",
"total_tests":"total_testes",
"total_tests_per_thousand":"total_testes_por_mil",
"new_tests_per_thousand":"novos_testes_por_mil",
"total_vaccinations":"total_vacinas",
"people_vaccinated":"pessoas_vacinadas",
"people_fully_vaccinated":"pessoas_vacinadas_dose_completa",
"new_vaccinations":"novas_vacinas_aplicadas",
"total_vaccinations_per_hundred":"total_vacinacao_por_centena",
"people_vaccinated_per_hundred":"pessoas_vacinadas_por_centena",
"people_fully_vaccinated_per_hundred":"pessoas_vacinadas_dose_completa_por_centena",
"population":"populacao",
"population_density":"densidade_populacional",
"median_age":"media_idade",
"aged_65_older":"idade_acima_65",
"aged_70_older":"idade_acima_70",
"gdp_per_capita":"pib_per_capita",
"extreme_poverty":"pobreza_extrema",
"life_expectancy":"expectativa_vida"
}

df = pd.read_csv(f'download/covid19.csv', sep=',', encoding='utf-8')
df = df.filter(campos_nome.keys())
df = df.rename(columns=campos_nome)
df.to_csv('download/covid19_renamed.csv', sep=',', index=False)
