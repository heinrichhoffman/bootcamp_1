#Questão 1
"""
def funcao(mensagem,numero):
    print(mensagem)
    print(numero)


texto = input("Digite uma mensagem: ")
num = int(input("Digite um número: "))

funcao(texto,num)    
"""

#Questão 2
"""

def soma(a,b,c):
    return a + b + c

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

resultado = soma(num1, num2, num3)
print("A soma dos três números é:", resultado)

"""
#Questão 3
"""
def idade(ano_nascimento):
    idade = 2026 - ano_nascimento
    return idade

ano = int(input("Digite o ano de nascimento: "))
print("A idade é:", idade(ano))

"""

#Questão 4:   CRIE UM PROGRAMA QUE PEÇA A QUANTIDADE DE HORAS QUE UM CARRO FICOU NO ESTACIONAMENTO DO CEUB E CALCULE O VALOR A PAGAR, SABENDO QUE O VALOR POR HORA É DE R$ 6,00.
"""
def calcular_valor(horas):
    valor_por_hora = 6.00
    valor_total = horas * valor_por_hora
    return valor_total  

horas_estacionamento = int(input("Digite a quantidade de horas que o carro ficou no estacionamento: "))
valor_a_pagar = calcular_valor(horas_estacionamento)
print(f"O valor a pagar é: R$ {valor_a_pagar:.2f}")

"""