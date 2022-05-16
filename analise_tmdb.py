import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

tmdb = pd.read_csv('dados/tmdb_5000_movies.csv')
# tmdb.columns = ['orcamento', 'genero', 'homepage', 'id', 'keywords', 'lingua_original','titulo_original', 'overview', 'popularidade', 'production_companies','production_countries', 'release_date', 'revenue', 'runtime','spoken_languages', 'status', 'tagline', 'title', 'vote_average', 'vote_count']
print(tmdb.columns)
print(tmdb.original_language.unique()) # retorna os valores unicos das linguas dos filmes sem repetir.
print(tmdb.original_language.value_counts().to_frame()) # To_frame() = Vamos ter o indice e uma colona
print(tmdb.original_language.value_counts().reset_index())# reset_index() = Desta maneira vamos ter duas colunas pois tiramos o index. 1 lingua e 2 quantidade de vezes que foi escrita.
contagem_de_lingua = tmdb.original_language.value_counts().reset_index()  # colocamos dentro de uma variável o nosso resultado das linguas e suas contagens.
contagem_de_lingua.columns = ["original_language","total"]  # colocamos um nome em cada celula, no caso colocamos um titulo em cada uma.
print(contagem_de_lingua.head())

# #Criando um grafico com as informações:
sns.set()
# #BARPLOT é um grafico de baixo nivel, onde que com ele conseguimos ter mais controle do que queremos fazer
sns.barplot(x="original_language", y="total", data=contagem_de_lingua) # Criamos um grafico com as linguas na horizontal e na vertical colocamos as quantidades que foram colocadas nos dados.
#
# #CATPLOT é um grafico de alto nivel, onde ele tem maneiras automaticas e configuraveis de carregar o grafico.
sns.catplot(x="original_language", kind = "count" , data=tmdb) # ele gera o grafico, mas não é de forma ordenada conforme o outro grafico, pois no barplot nós fizemos o separamento de tudo e no catplot nós pegamos os dados crus.
#
# #GRAFICO DE PIZZA
plt.pie(contagem_de_lingua["total"], labels= contagem_de_lingua["original_language"]) # O grafico é muito ruim para se trabalhar com bastante dados. Raramente usaremos.
plt.show()

# isolando os dados.
total_por_lingua = tmdb["original_language"].value_counts() # irá nos retornar a lingua e sua contagem
total_geral = total_por_lingua.sum()#SUM vai somar todos os valores e nos dar um total.
total_de_ingles = total_por_lingua.loc["en"]#LOC["EN"] vai localizar em nossa lista apenas a lingua INGLES e sua quantidade.
total_do_resto = total_geral - total_de_ingles# Vai pegar o total de linguas menos a lingua inglesa.
print(total_do_resto)

#Criamos um dicionario com os dados para que fiquem separados e assim consigamos colocar em um grafico a diferença entre o ingles e todos os outros.
dados = {
    'lingua': ['ingles','outros'],
    'total':[total_de_ingles,total_do_resto]
}
dados = pd.DataFrame(dados)
print(dados)
sns.barplot(x="lingua", y="total", data= dados) # Grafico de barra com os dois valores
plt.pie(dados["total"], labels= dados["lingua"])# Grafico de pizza/torta com os dois valores
plt.show()

#Buscar coisas dentro do dataframe = Query ()
total_de_lingua_de_outros_filmes = tmdb.query("original_language != 'en'").original_language.value_counts() # irá nos mostrar a contagem de todas as linguas menos o ingles.
print(total_de_lingua_de_outros_filmes)

filmes_sem_lingua_original_em_ingles = tmdb.query("original_language != 'en'")
sns.catplot(x = "original_language", kind="count", data= filmes_sem_lingua_original_em_ingles, aspect = 2 )# Catplot é uma função de alto nível. com isso podemos usar um parametro chamado ASPECT que com ele podemos aumentar a visualização do grafico.
sns.catplot(x = "original_language", kind="count", data= filmes_sem_lingua_original_em_ingles, aspect = 2 , order = total_de_lingua_de_outros_filmes.index)# Podemos usar um parametro chamado ORDER para ordenar nosso grafico do maior para o menor.
sns.catplot(x = "original_language", kind="count", data= filmes_sem_lingua_original_em_ingles, aspect = 2 , order = total_de_lingua_de_outros_filmes.index, palette = "GnBu_d")# Podemos usar um parametro chamado PALETTE para que seja alterada a cor de nosso grafico.
plt.title("Linguas Originail de filmes")
plt.show()




# ANALISAR OS NOMES DOS FILMES NO OUTRO ARQUIVO MOVIES.CSV E RATINGS.CSV.

filmes = pd.read_csv('dados/movies.csv')
filmes.columns = ["filmeId", "titulo", "genero"]
notas = pd.read_csv('dados/ratings.csv')
notas.columns = ["usuarioID", "filmeId", "nota", "Momento"]
print(filmes.titulo.head(2))
print(filmes.columns)
print(notas.head())
notas_do_toy_story = notas.query("filmeId==1")
notas_do_jumanji = notas.query("filmeId==2")
print(len(notas_do_toy_story),len( notas_do_jumanji))
print("nota média do Toy Story %.2f" % notas_do_toy_story.nota.mean()) # Utilizando o "%.2f" % ele vai interpolar a string com o numero e o numero será apenas de duas casas decimais.
print("nota média do Toy Story %.2f" % notas_do_jumanji.nota.mean()) # Utilizando o "%.2f" % ele vai interpolar a string com o numero e o numero será apenas de duas casas decimais.

sns.barplot(notas_do_toy_story.nota)
sns.barplot(notas_do_jumanji.nota)

plt.boxplot([notas_do_toy_story.nota, notas_do_jumanji.nota])
sns.boxplot(x="filmeId", y="nota", data=notas.query("filmeId in [1,2]"))
plt.show()

#Colocando dois graficos dentro de um apanes.
