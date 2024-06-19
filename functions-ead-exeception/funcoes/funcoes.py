def media():
    calculo = (10 + 9 + 8) / 3
    print(calculo)
    
media()

def media2(nota1, nota2, nota3):
    calculo = (nota1 + nota2 + nota3) / 3
    print(calculo)
    
media2(1, 2, 3)

# * exercício 1 

notas = [8.5, 9.0 , 6.0, 10.0]

def media_notas(lista):
    calculo = sum(lista) / len(lista)
    return calculo

resultado = media_notas(notas)
print(resultado)

# * exercício 2

notas2 = [8.5, 9.0 , 6.0, 10.0]

def boletim(lista):
    media = sum(lista) / len(lista)
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 3:
        situacao = "Prova final"
    else:
        situacao = "Reprovado"
    
    return (media, situacao)

media_aluno, situacao_aluno = boletim(notas2)
print(f"O estudante com a média {media_aluno} está {situacao_aluno}")