peso = float(input("Digite um peso: "))
Altura = float(input("Digite uma altura: "))
Altura2 = float(input("Digite a altura ao quadrado: "))

Quadrado = Altura2 * Altura2
imc = peso / (Altura * Altura2)

if imc >= 40:
    print("Obsidade Mórbida")
elif imc >= 35:
 print("Obsidade Mórbida")
elif imc >=30:
   print("Obsidade")
elif imc >= 25:
   print("Sobrepeso")
elif imc >18.5:
   print("Normal")
else:
   print("Baixo peso")

