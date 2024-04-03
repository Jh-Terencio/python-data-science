
# * 1. Escreva um código que lê a lista abaixo e faça:
    # * A leitura do tamanho da lista
    # * A leitura do maior e menor valor
    # * A soma dos valores da lista
    
# lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
# print(f"Tamanho da lista {len(lista)}\nMaior valor {max(lista)}\nMenor valor {min(lista)}\nSoma dos valores {sum(lista)}")

# * 2. Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 7, a tabuada deve ser mostrada no seguinte formato:

# numero = int(input("Digite o número que deseje saber a tabuada: "))

# def tabuada(num):
#     contador = 0
#     print(f"\nTabuada do {num}:")
#     # ? Outro opção de loop: for i in range(11)
#     while contador < 11:
#         multiplicacao = num * contador
#         print(f"{num} X {contador} = {multiplicacao}")
#         contador += 1

# tabuada(numero)

# * 3. Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3

# lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
# mult_3 = []

# def multiplo_tres(lista):
#     for i in lista:
#         if i % 3 == 0:
#             mult_3.append(i)
#     return mult_3

# resultado = multiplo_tres(lista)
# print(resultado)

# * 4. Crie uma lista dos quadrados dos números da seguinte lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Lembre-se de utilizar as funções lambda e map() para calcular o quadrado de cada elemento da lista.

# numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# quadrado = lambda x: x ** 2
# resultado = list(map(quadrado, numero))
# print(resultado)

# * 5. Você foi contratado(a) como cientista de dados de uma associação de skate. Para analisar as notas recebidas de skatistas em algumas competições ao longo do ano, você precisa criar um código que calcula a pontuação dos(as) atletas. Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.

# * Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior e a menor pontuação dentre as 5 notas e tirar a média das 3 notas que sobraram. Retorne a média para apresentar o texto:

# notas_manobra = []
# for i in range(1, 6):
#     N1 = float(input(f"Nota do {i}° jurado: "))
#     notas_manobra.append(N1)
    
# def calcula_nota_manobra(lista):
#     # ? Outra forma lista.remove(max(lista))
#                 # ? lista.remove(min(lista))
#     maior_nota = max(lista)
#     index = lista.index(maior_nota)
#     lista.pop(index)
#     menor_nota = min(lista)
#     index = lista.index(menor_nota)
#     lista.pop(index)
        
#     media = sum(lista) / len(lista)
#     return media

# resultado = calcula_nota_manobra(notas_manobra)
# print(f"Nota da manobra {resultado}")

# * 6. Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) estudantes, você precisa criar uma função que receba uma lista de 4 notas e retorne:
    # * maior nota
    # * menor nota
    # * média
    # * situação (Aprovado(a) ou Reprovado(a))
    
# notas_aluno = [6.0, 7.0 , 9.0, 5.5]

# def calcula_situacao(lista):
#     maior_nota = max(lista)
#     menor_nota = min(lista)
#     media = sum(lista) / len(lista)
    
#     if media >= 7:
#         situacao = "Aprovado"
#     elif media >= 3:
#         situacao = "De prova final"
#     else:
#         situacao = "Reprovado"
    
#     return maior_nota, menor_nota, media, situacao

# maior_nota_aluno, menor_nota_aluno, media_aluno, situacao_aluno = calcula_situacao(notas_aluno)
# print(f"O(a) estudante obteve uma média de {media_aluno}, com a sua maior nota de {maior_nota_aluno} pontos e a menor nota de {menor_nota_aluno} pontos e foi {situacao_aluno}")

# * 7. Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as para apresentar seus nomes completos na forma Nome Sobrenome.
# # Nomes dos estudantes
# nomes = ["joão", "MaRia", "JOSÉ"]
# sobrenomes = ["SILVA", "souza", "Tavares"]

# # Função lambda que recebe duas listas e itera em cada uma concatenando seu nome e sobrenome
# # na forma desejada
# nome_completo = map(lambda nome, sobrenome: f'{nome.title()} {sobrenome.title()}', nomes, sobrenomes)

# # Leitura do objeto mapa(iterável)
# for n in nome_completo:
#   print(f'Nome completo: {n}')


# * 8. Como cientista de dados em um time de futebol, você precisa implementar novas formas de coleta de dados sobre o desempenho de jogadores e do time como um todo. Sua primeira ação é criar uma forma de calcular a pontuação do time no campeonato nacional a partir dos dados de gols marcados e sofridos em cada jogo.

# * Escreva uma função chamada calcula_pontos que recebe como parâmetros duas listas de números inteiros, representando os gols marcados e sofridos pelo time em cada partida do campeonato. A função deve retornar a pontuação do time e o aproveitamento em percentual, levando em consideração que a vitória vale 3 pontos, o empate vale 1 ponto e a derrota 0 pontos.

# * Observação: se a quantidade de gols marcados numa partida for maior que a de sofridos, o time venceu. Caso seja igual, o time empatou e se for menor, o time perdeu. Para calcular o aproveitamento devemos fazer a razão entre a pontuação do time pela pontuação máxima que ele poderia receber.

# gols_marcados = [2, 1, 3, 1, 0]
# gols_sofridos = [1, 2, 2, 1, 3]

# def calcula_pontos(qntdMarcado, qndtSofrido):
#     resultados = list(map(lambda marcado, sofrido: marcado - sofrido, qntdMarcado, qndtSofrido))
#     pontuacao = 0
#     pontuacao_max = 3 * len(resultados)
#     for resultado in resultados:
#         if resultado > 0:
#             pontuacao += 3
#         elif resultado == 0:
#             pontuacao += 1
#     aproveitamento = (pontuacao / pontuacao_max) * 100
#     print(f"A pontuação do time foi de {pontuacao} e seu aproveitamento foi de {round(aproveitamento)}%")
    
# calcula_pontos(gols_marcados, gols_sofridos)

# * 9. Você recebeu o desafio de criar um código que calcula os gastos de uma viagem para um das quatro cidades partindo de Recife, sendo elas: Salvador, Fortaleza, Natal e Aracaju.

# * O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina na viagem de carro é de 14 km/l, sendo que o valor da gasolina é de 5 reais o litro. O gastos com passeios e alimentação a se fazer em cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.

# * Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente [850, 800, 300, 550] km, crie três funções nas quais: a 1ª função calcule os gastos com hotel (gasto_hotel), a 2ª calcule os gastos com a gasolina (gasto_gasolina) e a 3ª os gastos com passeio e alimentação (gasto_passeio).

# * Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. Considere a viagem de ida e volta de carro.

# def gastos_hotel(qntdDias):
#     total_hotel = 150 * qntdDias
#     return total_hotel

# def gasto_gasolina(cidade_destino):
#     ditancia_cidades = {'Salvador': 850, 'Fortaleza': 800, 'Natal': 300, 'Aracaju': 550}
#     distancia = ditancia_cidades[cidade_destino]
#     # * É vezes 2 por que é ida e volta
#     total_gasolina = ((distancia / 14) * 5) * 2
#     return total_gasolina

# def gasto_alimentacao(cidade_destino, qntdDias):
#     custo_cidades = {'Salvador': 200, 'Fortaleza': 400, 'Natal': 250, 'Aracaju': 300}    
#     custo = custo_cidades[cidade_destino] * qntdDias
#     return custo

# quantidade_dias = int(input("Digite a quantidade de dias de viagem: "))
# destino = input("Digite qual a cidade de destino, opções:\n\tSalvador\n\tFortaleza\n\tNatal\n\tAracaju\n")

# hotel = gastos_hotel(quantidade_dias)
# gasolina = gasto_gasolina(destino)
# alimentacao = gasto_alimentacao(destino, quantidade_dias)
# total = hotel + gasolina + alimentacao

# print(f"Para a sua viagem com destino a {destino} você gastará de hotel R${hotel}, de gasolina R${round(gasolina, 2)} e de alimentação R${alimentacao}. Totalizando R${round(total, 2)}")

# * 10. Você iniciou um estágio em uma empresa que trabalha com processamento de linguagem natural (NLP). Sua líder requisitou que você criasse um trecho de código que recebe uma frase digitada pela pessoa usuária e filtre apenas as palavras com tamanho maior ou igual a 5, exibindo-as em uma lista. Essa demanda é voltada para a análise do padrão de comportamento de pessoas na escrita de palavras acima dessa quantidade de caracteres.

# Requisitando uma frase e separando-a pelos espaços. Usando replace para trocar
# pontuações por espaço.
frase = input("Digite uma frase: ")
frase = frase.replace(',',' ').replace('.',' ').replace('!',' ').replace('?',' ').split()

# Filtrando a frase no formato de lista, passando para a lista tamanho
# apenas as palavras com 5 ou mais caracteres e imprimindo-a na tela
frase_filtrada = list(filter(lambda x: len(x) >= 5, frase))
print(frase_filtrada)


