
# * Dict comprehension é um forma simples de criar ou modificar um dicionário

# ? Formato padrão: {chave: valor for item in lista}

# * Agora, a nossa demanda consiste em gerar um dicionário a partir da lista de listas que criamos na Situação 10 para passá-la à pessoa responsável por construir as tabelas, possibilitando a análise dos dados.

  # * As chaves do nosso dicionário serão as colunas identificando o tipo de dado.

  # * Os valores serão as listas com os dados correspondentes àquela chave.
  
lista_completa = [[('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')],
                  [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]],
                  [9.0, 7.3, 5.8, 6.7, 8.5],
                  ['Aprovado', 'Aprovado', 'Reprovado', 'Aprovado', 'Aprovado']]

coluna = ["Notas", "Média Final", "Situação"]

cadastro = {coluna[i]: lista_completa[i+1] for i in range(len(coluna))}
print(cadastro)

# * Adicionando estudantes
cadastro["Estudante"] = [lista_completa[0][i][0] for i in range(len(lista_completa[0]))]
print(cadastro)
