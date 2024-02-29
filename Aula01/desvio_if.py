
numero = input("digite um numero:")
# É necessário realizar a conversão de texto para
# número, pois a função input sempre retorna o valor
# em formato de texto. Então, utilizamos a função
# int para converter a variável numero em valor
# numérico inteiro e assim realizar os cálculos
# necessários
numero = int(numero)

if(numero % 2 == 0):
    print(" o numero digitado é par")
else:
    print("o numero digitado é impar")