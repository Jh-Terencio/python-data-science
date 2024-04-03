# * Nesta nova demanda, precisamos gerar uma lista de tuplas com os nomes dos estudantes e o código ID de cada um para a plataforma de análise dos dados. A criação do código consiste em concatenar a primeira letra do nome do estudante a um número aleatório de 0 a 999. Os dados recebidos correspondem a uma lista dos nomes de cada estudante.

from random import randint

estudantes = ["João", "Maria", "José", "Cláudia", "Ana"]

def gera_codigo():
    return str(randint(0, 999))

codigo_estudantes = []

for i in range(len(estudantes)):
    # * Para a criação de lista de tuplas usamos () e para lista de listas []
    # ? Explicando o estudantes [i][0]. Como queremos pegar a inicial do nome de cada estudantes passamos primeiro o [i] que irá pegar o nome completo do estudante e depois o [0] que pegerá a inicial, pois uma string também é interável
    codigo_estudantes.append((estudantes[i], estudantes[i][0] + gera_codigo()))

print(codigo_estudantes)