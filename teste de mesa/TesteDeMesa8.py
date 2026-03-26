valor1 = int(input("Digite o valor do primeiro lado: "))
valor2 = int(input("Digite o valor do segundo lado: "))
valor3 = int(input("Digite o valor do Terceiro lado: "))
valor4 = int(input("Digite o valor do quarto lado: "))

if (valor1 == valor2 == valor3 == valor4):
    print("Ele é um Quadrado")
elif (valor1 == valor2 != valor3 == valor4):
    print("Ele é um Retangulo")
else:
    print("Ele não e nunhum dos dois")
