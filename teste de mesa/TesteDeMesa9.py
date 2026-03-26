decimal1 = int(input("Digite um número com casas decimais: "))
op = input("Digite a operação (+, -, *, /): ")
decimal2 = int(input("Digite outro número com casas decimais: "))

if op == "+":
    resultado = decimal1 + decimal2
elif op == "-":
    resultado = decimal1 - decimal2
elif op == "*":
    resultado = decimal1 * decimal2
elif op == "/":
    resultado = decimal1 / decimal2
else:
    resultado = "Operação Inválida"

print("Resultado:", resultado)