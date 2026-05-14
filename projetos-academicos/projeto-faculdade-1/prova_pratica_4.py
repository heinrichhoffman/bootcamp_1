# Questão 1

"""
ctd = 0
valor_final = int(input("Digite o valor final: "))

for i in range(0, valor_final + 1):
    print(i)
    ctd += 1

print(f"Quantidade de números impressos: {ctd}")

"""

# Questão 2
""""
ctd = 0
valor_inicial = int(input("Digite o valor inicial: "))

for i in range(valor_inicial, -1, -1):
    print(i)
    ctd += 1

print(f"Quantidade de números impressos: {ctd}")

"""

# Questão 3


"""
soma = 0
for i in range(1, 501):
    soma = soma + i

print(f"A soma dos números de 1 a 500 é: {soma}")    

"""

#Questão 4

"""
soma = 0

for i in range(1, 501):
    if i % 3 == 0 and i %2 != 0:
        soma = soma + i


print(f"A soma dos números de 1 a 500, ímpares e multiplos de 3  é: {soma}")    

"""

#Questão 5

"""
for i in range(7):
   
    for j in range(7):
        print(f"[{i}|{j}]")

"""

#Questão 6

"""

for i in range(7):
    for j in range(i, 7):
        print(f"[{i}|{j}]")

"""