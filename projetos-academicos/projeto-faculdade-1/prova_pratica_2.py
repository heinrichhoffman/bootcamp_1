# Prova Prática 2 - PP2
# Heinrich Hoffman

# 1
"""

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Digite + para Somar, - para Subtrair, * para Multiplicar e / para Dividir: ")

if operacao == "+":
  resultado = num1 + num2

elif operacao == "-":
  resultado = num1 - num2

elif operacao == "*":
  resultado = num1 * num2

elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero!"

else:
    resultado = "Operação Inválida"

print("O resultado da Operação é: ", resultado)


"""

#2
"""
ctd = 0
soma = 0
ctd_20 = 0

while True:
    valor = float(input("Digite um valor (0 para sair): "))
    
    if valor == 0:
        break  
        
    ctd += 1
    soma += valor 
    
    if valor > 20:
        ctd_20 += 1


if ctd > 0:
    media = soma / ctd
    print(f"Quantidade de valores digitados: {ctd}")
    print(f"Soma total: {soma:.2f}")
    print(f"Média dos valores: {media:.2f}")
    print(f"Quantidade de valores maiores que 20: {ctd_20}")
else:
    print("Nenhum valor válido foi digitado.")
"""
#3

"""
total_alunos = 0
aprovados = 0
reprovados = 0
soma_notas = 0

print("--- Digite uma nota negativa para encerrar ---")

while True:
    nota = float(input(f"Digite a nota do aluno {total_alunos + 1}: "))
    if nota < 0:
        break
    
    total_alunos += 1
    soma_notas += nota
    
    if nota >= 5:
        aprovados += 1
    else:
        reprovados += 1

if total_alunos > 0:
    media_turma = soma_notas / total_alunos
    
    print("---------------")
    print("RESUMO DA TURMA")
    print("---------------")
    print(f"Total de alunos:{total_alunos}")
    print(f"Alunos aprovados: {aprovados}")
    print(f"Alunos reprovados:{reprovados}")
    print(f"Média da turma:{media_turma:.2f}")
else:
    print("\nNenhuma nota foi registrada.")

"""
#4

"""
ctd = 0
ctd_par = 0
ctd_impar = 0
soma_total = 0
soma_pares = 0
soma_impares = 0

while True:
    valor = float(input("Digite um valor (0 para sair): "))

    if valor == 0:
        break
    
    ctd += 1
    soma_total += valor

    if valor % 2 == 0:
        soma_pares += valor
        ctd_par += 1

    else:
        soma_impares += valor
        ctd_impar += 1

media_par = soma_pares / ctd_par
media_impar = soma_impares / ctd_impar

print("---------------")
print("RESUMO DOS VALORES")
print("---------------")
print(f"Total de valores digitados: {ctd}")
print(f"Média dos valores pares: {media_par:.2f}")
print(f"Média dos valores ímpares: {media_impar:.2f}")
print(f"Soma total dos valores: {soma_total}")

"""