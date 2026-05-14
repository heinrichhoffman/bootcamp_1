#1
"""
lista_pares = []
lista_impares = []

print("Vamos calcular a média aritmética dos números pares e ímpares digitados. Digite 0 para sair")
while True:
  valor = input(input("Digite um valor: "))
  if valor == 0:
    break
  if valor % 2 == 0:
    lista_pares.append(valor)
  else:
    lista_impares.append(valor)

media_pares = sum(lista_pares) / len(lista_pares) if len(lista_pares) > 0 else 0
qtd_pares = len(lista_pares)
media_impares = sum(lista_impares) / len(lista_impares) if len(lista_impares) > 0 else 0
qtd_impares = len(lista_impares)

print(f"Média dos números pares: {media_pares}")
print(f"Quantidade de números pares: {qtd_pares}")
print(f"Média dos números ímpares: {media_impares}")
print(f"Quantidade de números ímpares: {qtd_impares}")


"""

#2 

'''
lista = []

print("Digite 0 para sair")

while True:
  valor = float(input("Digite um valor: "))
  if valor == 0:
    break
  lista.append(valor)

qtd = len(lista)
soma = sum(lista)
media = soma / qtd
maior_valor = max(lista)
menor_valor = min(lista)
qtd_valor_acima_50 = len([valor for valor in lista if valor > 50])


print("Quantidade de valores: ", qtd)
print("Soma dos valores: ", soma)
print("Média dos valores: ", media)
print("Maior valor: ", maior_valor)
print("Menor valor: ", menor_valor)
print("Quantidade de valores acima de 50: ", qtd_valor_acima_50)

'''

#3

"""

lista = []
print("Bem vindo à Urna Digital\nVote 0 para Sair")

while True:
  voto = int(input("Digite seu voto: "))
  if voto == 0:
    break

  if voto == 1 or voto == 2 or voto == 3 or voto == 5 or voto == 6:
    lista.append(voto)
  else:
    print("Voto inválido")

  A = lista.count(1)
  B = lista.count(2)
  C = lista.count(3)
  nulo = lista.count(5)
  branco = lista.count(6)

print("-"*20)
print("Quantidade de votos:")
print("-"*20)
print("Candidato A: ", A)
print("Candidato B: ", B)
print("Candidato C: ", C)
print("Votos nulos: ", nulo)
print("Votos em branco: ", branco)

"""

#4
"""
faixa_baixa = 0   
faixa_media = 0   
faixa_alta = 0    
total_folha = 0  


salario_minimo = float(input("Informe o valor do salário mínimo: "))

print("\nDigite os salários dos funcionários (0 para Sair):")

while True:
    salario = float(input("Salário do funcionário: "))
    
   
    if salario == 0:
        break
    total_folha += salario
    proporcao = salario / salario_minimo
    
    if proporcao < 5:
        faixa_baixa += 1
    elif 5 <= proporcao < 10:
        faixa_media += 1
    else:
        faixa_alta += 1


print("-" * 20)
print("RELATÓRIO")
print("-" * 20)
print(f"Menos de 5 salários mínimos: {faixa_baixa} funcionário(s)")
print(f"De 5 a menos de 10 salários: {faixa_media} funcionário(s)")
print(f"10 ou mais salários mínimos: {faixa_alta} funcionário(s)")
print("-" * 20)
print(f"Valor total da folha de pagamento: R$ {total_folha:.2f}")

"""