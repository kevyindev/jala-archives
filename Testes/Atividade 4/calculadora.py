print("\n******************* Python Calculator *******************")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def raiz(x):
    return x ** 0.5

print("\nSelecione o número da operação desejada: \n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Raiz quadrada")

escolha = input("\nDigite sua opção (1/2/3/4/5): ")

num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))
print("\n")
print("******************* Resultado *******************")

if escolha == '1':
    print("\n")
    print(num1, "+", num2, "=", add(num1, num2))
    print("\n")

elif escolha == '2':
    print("\n")
    print(num1, "-", num2, "=", subtract(num1, num2))
    print("\n")

elif escolha == '3':
    print("\n")
    print(num1, "*", num2, "=", multiply(num1, num2))
    print("\n")

elif escolha == '4':
    print("\n")
    print(num1, "/", num2, "=", divide(num1, num2))
    print("\n")

elif escolha == '5':
    print("\n")
    print("A raiz quadrada de", num1, "é", raiz(num1))
    print("\n")

else:
    print("\nOpção inválida!")
    print("\n")