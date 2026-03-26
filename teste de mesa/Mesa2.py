nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >=9:
    resultado = "Exelente"
elif media >= 7:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"
    print("Média: ", media)
    print("Resultado: ", resultado)