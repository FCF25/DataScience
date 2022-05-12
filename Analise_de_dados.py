from tkinter.tix import DisplayStyle
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# ANALISANDO AS NOTAS EM GERAL

# Atribuimos todos os dados para a variavél notas. com isso podemos ajustar para apresentar apenas a quantidade que queremos.
pd.set_option('display.max_rows', 1000)
# Se colocarmos desta maneira irá mostrar todos nosso arquivo .csv print(pd.read_csv('dados/ratings.csv'))

notas = pd.read_csv('dados/ratings.csv')

#  HEAD() irá nos mostrar todos os 5 primeiros itens como o proprio nome  já diz é um cabeçalho.
print(notas.head())

# SHAPE vai nos mostrar a quantidade de linhas e colunas que tem nosso arquivo.
print(notas.shape)

# Alterando os nomes das colunas para portugues. Coloca,tudo dentro de uma lista
notas.columns = ["usuarioID", "filmeId", "nota", "Momento"]
print(notas.head())

# Irá acessar apenas a coluna que escolhemos e irá nos mostrar.
print(notas['nota'])

# UNIQUE vai nos mostrar todos os valores unicos e assim entendemos que as notas deste arquivo vai de 0,5 até 5 .
print(notas['nota'].unique())

# Value_Count vai nos contar a quantidade de valores repetidos.
print(notas['nota'].value_counts())

# MEAN() é a média e com ele podemos descobrir a média.
print(notas['nota'].mean())

# Podemes utilizar apenas o nome notas.nota para mostrar nossos dados.
print(notas.nota)

# PLOT() é para ser criado um gráfico e com isso conseguimos ver todas as notas dentro do nosso grafico.
notas.nota.plot(kind='hist')
plt.show()

# MEDIAN() ele pega a metade de cima e a metade de baixo e gera um resultado, mas é diferente da média.
print(notas.nota.median())

# DESCRIBE() vai nos mostrar todos os dados de nossas notas - como a contagem total, maximo e minimo o padrão e 25,50 e 70% das notas.
print(notas.nota.describe())


# AGORA NOS VAMOS BAIXAR O SEABORN que é uma ferramenta para DATA SCIENCE, para utilização de graficos.
# import seaborn as sns

# usando o SNS.BOXPLOT(Notas.nota) conseguimos verificar o exato logal aonde mostra a mediana no grafico.
sns.boxplot(notas.nota)
plt.show()


# ANALISAR OS NOMES DOS FILMES NO OUTRO ARQUIVO CSV.

filmes = pd.read_csv('dados/movies.csv')
filmes.columns = ["filmeId", "titulo", "genero"]
print(filmes.titulo.head())
print(notas.query("filmeId == 1")) # Utilizando o QUERY ele vai estar perguntando para o CSV todas as notas que foram dadas para o ID1 que é o Filme Toy Story.
print(notas.query("filmeId == 1").nota) # Agora ele irá nos mostrar apenas as notas dada para o Filme do ID 1
print(notas.query("filmeId == 1").nota.mean()) # Usando no final .NOTA.MEAN() ele irá nos retornar as médias do filme de ID1 que colocamos.

# Como usamos o framework Pandas podemos agrupar por fimes, utilizando o .GROUPBY(filmes)
print(notas.groupby("filmeId").nota.mean()) # Agrupamos e o resultado será a média de cada id de filme.
print(notas.groupby("filmeId").mean()) # Como não colocamos nota apenas ele irá nos retornar todos as colunas com suas média, porém como exemplo a coluna de usuário ela não serve para nada.
print(notas.groupby("filmeId").mean()["nota"])# Podemos fazer o agrupamento apenas das notas com suas média.
medias_por_filme = notas.groupby("filmeId").mean()["nota"]  # Atribuimos em uma variável os dados das notas com suas médias
print(medias_por_filme.head())

medias_por_filme.plot(kind='hist') # usando o Matplotlib para mostrar o grafico.
sns.set()  # Colocando o SNS.SET() colocamos o fundo cinza e com isso fica uma melhor visualização dos graficos.
plt.figure(figsize=(5, 8))  # Configurando para aparecer o grafico no tamanho 5 por 8
sns.boxplot(y=medias_por_filme)# O grafico vai ficar na vertical pois colocamos no eixo Y
sns.boxplot(medias_por_filme)  # Utilizando o Seaborn para gerar o grafico.
sns.displot(medias_por_filme)  # DISPLOT é uma forma de mostrar o grafico mais detalhado.
sns.displot(medias_por_filme, bins=10)  # o parametro bins = 10 irá nos mostrar um grafico com 10 colunas/Barras.
sns.displot(medias_por_filme, kde= True)#Utilizando o KDE = TRUE ele irá colocar uma linha  de aproximação em nosso Grafico, ficando mais facil de analisar tanto visulmente quanto mais bonito.

plt.title("Histograma das médias dos filmes")  # conseguimos configurar o título de nosso grafico.
plt.show()  # Serve para mostrar o nosso grafico na tela, pois sem isso ele não será mostrado.
print(medias_por_filme.describe())

