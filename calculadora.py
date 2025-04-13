num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
op = input("Escolha a operação (+, -, *, /): ")

if op == '+':
    print("Resultado:", num1 + num2)
elif op == '-':
    print("Resultado:", num1 - num2)
elif op == '*':
    print("Resultado:", num1 * num2)
elif op == '/':
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Erro: divisão por zero.")
else:
    print("Operação inválida.")
