
# * A List comprehension é uma forma simples e concisa de criar listas, sendo que essas listas seguirão alguns padrões, via condicionais, laços e outras expressões.

# * Recebemos a demanda de criar uma lista com as médias dos estudantes da lista de listas que criamos na Situação 6. Lembrando que cada lista da lista de listas possui as três notas de cada estudante.

notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]

def media(lista: list=[0]) -> float:
    calculo = sum(lista) / len(lista)
    return calculo

media = [round(media(nota), 1) for nota in notas]
print(media)

# * Agora, precisamos utilizar as médias calculadas no exemplo anterior, pareando com o nome dos estudantes. Isto será necessário para gerar uma lista que selecione aqueles estudantes que possuam uma média final maior ou igual a 8 para concorrer a uma bolsa para o próximo ano letivo.

# * Os dados recebidos correspondem a uma lista de tuplas com os nomes e códigos dos estudantes e a lista de médias calculadas logo acima.

nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

nomes = [nome[0] for nome in nomes]
print(nomes)

# ? O zip() recebe um ou mais iteráveis (lista, string, dict, etc.) e retorna-os como um iterador de tuplas onde cada elemento dos iteráveis são pareados.
alunos = list(zip(nomes, medias))
print(alunos)

candidatos = [aluno[0] for aluno in alunos if aluno[1] >= 8]
print(candidatos)

# * Recebemos duas demandas a respeito desse projeto com as notas dos estudantes:

# * Criar uma lista da situação dos estudantes em que caso sua média seja maior ou igual a 6 receberá o valor "Aprovado" e caso contrário receberá o valor "Reprovado".

# * Gerar uma lista de listas com:

# * Lista de tuplas com o nome dos estudantes e seus códigos.

# * Lista de listas com as notas de cada estudante.

# * Lista com as médias de cada estudante.

# * Lista da situação dos estudantes de acordo com as médias.

# * Os dados que utilizaremos são os mesmos que geramos nas situações anteriores (nomes, notas, medias).