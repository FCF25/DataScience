import pandas as pd

# Atribuimos todos os dados para a variavél notas. com isso podemos ajustar para apresentar apenas a quantidade que queremos.

# Se colocarmos desta maneira irá mostrar todos nosso arquivo .csv print(pd.read_csv('dados/ratings.csv'))

notas = pd.read_csv('dados/ratings.csv')

#  HEAD() irá nos mostrar todos os 5 primeiros itens como o proprio nome  já diz é um cabeçalho.
# print(notas.head())

# SHAPE vai nos mostrar a quantidade de linhas e colunas que tem nosso arquivo.
# print(notas.shape)

# Alterando os nomes das colunas para portugues. Coloca,tudo dentro de uma lista
notas.columns = ["usuarioID", "filmeId", "nota", "Momento"]
# print(notas.head())

# Irá acessar apenas a coluna que escolhemos e irá nos mostrar.
# print(notas['nota'])

# UNIQUE vai nos mostrar todos os valores unicos e assim entendemos que as notas deste arquivo vai de 0,5 até 5 .
# print(notas['nota'].unique())


#Value_Count vai nos contar a quantidade de valores repetidos.
# print(notas['nota'].value_counts())

# MEAN() é a média e com ele podemos descobrir a média.

print(notas['nota'].mean())