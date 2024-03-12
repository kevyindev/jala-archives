#Dado um inteiro n, determine se o número é par ou ímpar, se for par, imprima "O número é par" ou "The number is even"

number = 9

if number % 2 == 0:
    print(f"O número {number} é par")
    print(f"The number {number} is even")
else:
    print(f"O número {number} é ímpar")
    print(f"The number {number} is odd")
