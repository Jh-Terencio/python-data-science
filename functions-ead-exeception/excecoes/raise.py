
# * raise que permitirá que lancemos uma exceção.
  # ? raise ValueError("A lista de notas deve possuir dez elementos")

# * Você criou uma função para calcular a média de um estudante em uma dada matéria passando em uma lista as notas deste estudante. Você pretende tratar 2 situações:
  # * Se a lista possuir um valor não numérico o cálculo de média não serà executado e uma mensagem de "Não foi possível calcular a média do(a) estudante. Só são aceitos valores numéricos!" será exibida.
  # * Caso a lista tenha mais de 4 notas, será lançada uma exceção do tipo ValueError informando que "A lista não pode possuir mais de 4 notas."

def media(lista: list=[0]) -> float:
  calculo = sum(lista) / len(lista)

  if len(lista) > 4:
    raise ValueError("A lista não pode possuir mais de 4 notas")

  return calculo

try: 
  notas = [6, 7, 8, 8, "5"]
  resultado = media(notas)
except TypeError:
  print("Não foi possível calcular a média. Só são aceitos valores numéricos")
except ValueError as e:
  print(e)
else: 
  print(resultado)
finally:
  print("Consulta foi encerrada")