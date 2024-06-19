
# * lambda functions AKA anonymous functions, are functions that dont need to be defined. They are just a single line of commands that we want to apply

nota = float(input("Digite a nota do estudante: "))

qualitativo = lambda x: x + 0.5

print(qualitativo(nota))

# ? Exercício
N1 = float(input("Digite a 1° nota do estudante: "))
N2 = float(input("Digite a 2° nota do estudante: "))
N3 = float(input("Digite a 3° nota do estudante: "))

media_ponderada = lambda x, y, z: (x * 3 + y * 2 + z * 5)/10

media_estudante = media_ponderada(N1, N2, N3)
print(media_estudante)

# ? Exercício 2
notas = [6.0, 7.0 , 9.0, 5.5, 8.0]
qualitativo = 0.5

notas_atualizadas = map(lambda x: x + qualitativo, notas)
# ! Quando fazemos o map ele cria um objeto do tipo map, mas para visualizarmos precisamos transormá-lo em lista
notas_atualizadas = list(notas_atualizadas)
print(notas_atualizadas)
