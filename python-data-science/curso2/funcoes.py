
# * Built-in functions

# ? Forma sem built-in para somar notas e fazer a média
notas = {'1° trimestre': 8.5, '2° trimestre': 9.5, '3° trimestre': 7}
print(notas)

soma = 0
contador = 0

for nota in notas.values():
    soma += nota
    contador += 1
    
print(soma)

media = soma / contador
print(media)

# ? Forma com built-in para somar notas e fazer a média
soma2 = sum(notas.values())
print(soma2)

media = soma2 / len(notas)
print(media)

# ! O help também é uma bult-in function, ele te auxilia a descobrir informações de outras built-in functions
help(round)

media_arredondada = round(media, 1)
print(media_arredondada)