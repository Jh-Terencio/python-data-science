notas_turma = ['João', 8.0, 9.0, 10.0, 'Maria', 9.0, 7.0, 6.0, 'José', 3.4, 7.0, 7.0, 'Marcos', 5.5, 6.6, 8.0, 'Ana', 6.0, 10.0, 9.5]

# * Dividir a lista em 2
nomes = []
notas_juntas = []

for i in range(len(notas_turma)):
    if i % 4 == 0:
        nomes.append(notas_turma[i])
    else: 
        notas_juntas.append(notas_turma[i])
        
# * Criando uma lista de lista de notas

notas = []

# ? Nesse for quremos pegar o parâmetro de início, por isso botamos esse 0, depois passamos o comprimento e esse 3 é para pular de 3 em 3
for i in range(0, len(notas_juntas), 3):
    notas.append([notas_juntas[i], notas_juntas[i+1], notas_juntas[i+2]])

print(notas)