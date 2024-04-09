
# * 1. Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na seguinte lista:

# lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]

# soma_lista = [sum(numero) for numero in lista_de_listas]
# print(soma_lista)

# ? Jeito professor:
# for lista in lista_de_listas:
#     print(sum(lista))


# * 2. Crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla contida na seguinte lista de tuplas:

# lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

# armazena_terceiro_elemento = [lista_de_tuplas[i][2] for i in range(len(lista_de_tuplas))]
# print(armazena_terceiro_elemento)

# ? Jeito professor:
# lista = []
# for tupla in lista_de_tuplas:
#     lista.append(tupla[2])
# print(lista)

# * 3. A partir da lista: lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo'], crie um código para gerar uma lista de tuplas em que cada tupla tenha o primeiro elemento como a posição do nome na lista original e o segundo elemento sendo o próprio nome.

# lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']
# lista_nova = []

# for i in range(len(lista)):
#   lista_nova.append((i, lista[i]))
  
# print(lista_nova)

# * 4. Crie uma lista usando o list comprehension que armazena somente o valor numérico de cada tupla caso o primeiro elemento seja 'Apartamento', a partir da seguinte lista de tuplas:

# aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

# aluguel_apartamento = [tipo[1] for tipo in aluguel if tipo[0] == "Apartamento"]
# print(aluguel_apartamento)

# * 5. Crie um dicionário usando o dict comprehension em que as chaves estão na lista meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'] e os valores estão em despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360].

# meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

# despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]

# despesas_por_mes = {meses[i]: despesa[i] for i in range(len(meses))}
# print(despesas_por_mes)

# * 6. Uma loja possui um banco de dados com a informação de venda de cada representante e de cada ano e precisa filtrar somente os dados do ano 2022 com venda maior do que 6000. A loja forneceu uma amostra contendo apenas as colunas com os anos e os valores de venda para que você ajude a realizar a filtragem dos dados a partir de um código. Crie uma lista usando list comprehension para filtrar os valores de 2022 e que sejam maiores que 6000.

# vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]

# filtro_vendas = [venda for venda in vendas if venda[0] == '2022' and venda[1] > 6000]
# print(filtro_vendas)

# * 7. Uma clínica analisa dados de pacientes e armazena o valor numérico da glicose em um banco de dados e gostaria de rotular os dados da seguinte maneira:

  # * Glicose igual ou inferior a 70: 'Hipoglicemia'
  # * Glicose entre 70 a 99: 'Normal'
  # * Glicose entre 100 e 125: 'Alterada'
  # * Glicose superior a 125: 'Diabetes'
# * A clínica disponibilizou parte dos valores e sua tarefa é criar uma lista de tuplas usando list comprehension contendo o rótulo e o valor da glicemia em cada tupla.

# glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

# classificacao = ["Diabetes" if nivel > 125 else "Alterada" if nivel > 99 else "Normal" if nivel > 69 else "Hipoglicemia" for nivel in glicemia]

# glicemia_rotulada = list(zip(classificacao, glicemia))
# print(glicemia_rotulada)

# * 8. Um e-commerce possui as informações de id de venda, quantidade vendida e preço do produto divididos nas seguintes listas. O e-commerce precisa estruturar esses dados em uma tabela contendo o valor total da venda, que é obtida multiplicando a quantidade pelo preço unitário. Além disso, a tabela precisa conter um cabeçalho indicando as colunas: 'id', 'quantidade', 'preco' e 'total'. O e-commerce precisa estruturar esses dados em uma tabela contendo o valor total da venda, que é obtida multiplicando a quantidade pelo preço unitário. Além disso, a tabela precisa conter um cabeçalho indicando as colunas: 'id', 'quantidade', 'preco' e 'total'.

# id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
# preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

# tabela = [('id', 'quantidade', 'preco', 'total')]
# tabela += [(id[i], quantidade[i], preco[i], quantidade[i]*preco[i]) for i in range(len(id))]
# print(tabela)

# * 9. Uma empresa possui filiais espalhadas nos Estados da região Sudeste do Brasil. Em uma das tabelas de cadastro das filiais há uma coluna contendo a informação de qual é o Estado a que pertence: estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG'].

# * A empresa sempre está abrindo novas filiais, de modo que a tabela está constantemente recebendo novos registros e o gestor gostaria de possuir a informação atualizada da quantidade de filiais em cada Estado.

# * A partir da coluna com a informação dos Estados, crie um dicionário usando dict comprehension com a chave sendo o nome de um Estado e o valor sendo a contagem de vezes em que o Estado aparece na lista.

estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']

# estados_sp = [estado for estado in estados if estado == "SP"]
# estados_rj = [estado for estado in estados if estado == "RJ"]
# estados_mg = [estado for estado in estados if estado == "MG"]
# estados_es = [estado for estado in estados if estado == "ES"]

# estado_organizado = []
# estado_organizado.append([estados_sp, estados_rj, estados_mg, estados_es])

# dicionario_estados = {
#     "SP": len(estados_sp),
#     "RJ": len(estados_rj),
#     "MG": len(estados_mg),
#     "ES": len(estados_es)
# }
# print(dicionario_estados)

# ? Jeito professor:
# # Armazenando os estados sem repetição de valor
# estados_unicos = list(set(estados))

# # Criando uma lista de listas com valores repetidos de cada estado
# lista_de_listas = []
# for estado in estados_unicos:
#     lista = [uf for uf in estados if uf == estado]
#     lista_de_listas.append(lista)
# print(lista_de_listas)

# # Criando um dicionário em que a chave é o nome de cada estado único e o valor é a contagem de elementos
# contagem_valores = {estados_unicos[i]: len(lista_de_listas[i]) for i in range(len(estados_unicos))}
# print(contagem_valores)

# * 10. Nessa mesma tabela de cadastro de filiais, há uma coluna com as informações da quantidade de pessoas colaboradoras e o(a) gestor(a) gostaria de ter um agrupamento da soma dessas pessoas para cada estado. As informações contidas na tabela são. A partir da lista de tuplas, crie um dicionário em que as chaves são os nomes dos Estados únicos e os valores são as listas com o número de colaboradores(as) referentes ao Estado. Crie também um dicionário em que as chaves são os nomes dos Estados e os valores são a soma de colaboradores(as) por Estado.

funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]

# Armazenando os estados sem repetição de valor
estados_unicos = list(set([tupla[0] for tupla in funcionarios]))


# Criando uma lista de listas com valores de funcionários de cada estado
lista_de_listas = []
for estado in estados_unicos:
    lista = [tupla[1] for tupla in funcionarios if tupla[0] == estado]
    lista_de_listas.append(lista)
print(lista_de_listas)

# Criando um dicionário com dados agrupados de funcionário por estado
agrupamento_por_estado = {estados_unicos[i]: lista_de_listas[i] for i in range(len(estados_unicos))}
print(agrupamento_por_estado)

# Criando um dicionário com a soma de funcionários por estado
soma_por_estado = {estados_unicos[i]: sum(lista_de_listas[i]) for i in range(len(estados_unicos))}
print(soma_por_estado)


  
