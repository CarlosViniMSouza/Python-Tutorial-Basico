import pandas as pd
import numpy as np

table = {
    'Conforto': np.random.randint(6, 10, 10),
    'Desempenho': np.random.randint(6, 10, 10),
    'Satisfacao': np.random.randint(6, 10, 10),
    'Unid. Vendidas': (96.139, 64.925, 57.137, 54.954, 59.480, 44.771, 43.642, 43.691, 41.121, 40.817),
    'Nome Carro': ('Ford Fiesta', 'Vauxhall Corsa', 'Ford Focus', 'Volkswagen Golf', 'Nissan Qashqai', 'Vauxhall Astra', 'Volkswagen Polo', 'MINI Cooper', 'Mercedes C-Class', 'Audi A3')
}  # aqui, fizemos uso do dicionario e da tupla para construir nosso DataFrame(Tabela)

table = pd.DataFrame(table)

print(table)

result = table.to_csv('result.csv')

data = pd.read_csv('result.csv')

"""
output:

   Conforto  Desempenho  Satisfacao  Unid. Vendidas        Nome Carro
0         7           7           6          96.139       Ford Fiesta
1         7           6           9          64.925    Vauxhall Corsa
2         9           7           6          57.137        Ford Focus
3         7           8           8          54.954   Volkswagen Golf
4         8           7           8          59.480    Nissan Qashqai
5         7           8           9          44.771    Vauxhall Astra
6         8           6           8          43.642   Volkswagen Polo
7         7           6           8          43.691       MINI Cooper
8         9           8           9          41.121  Mercedes C-Class
9         9           9           6          40.817           Audi A3
"""

# obs.: as colunas 'Conforto', 'Desempenho' e 'Satisfacao' sao compostas de valores randomicos!

# Bem, criamos a tabela, agora vamos criar um arquivo python para o calculo de Naive Bayes (naiveBayes.py)
