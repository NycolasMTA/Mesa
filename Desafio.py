import random

lista = [1, 2, 3, 5, 6, 7, 8, 9, 10]

numeroAleatorio = random.choice(lista)

tentativa1 = int(input("Digite um número ente 1 e 10: "))

if tentativa1 == numeroAleatorio:
    print("Parabéns você acertou!!")
else:
    if tentativa1 < numeroAleatorio:
        print("O número é maior que esse!")
    else:
        print("O número é menor.")
    
    tentativa2 = int(input("Tente novamente: "))
    
    if tentativa2 == numeroAleatorio:
        print("Parabéns! Você acertou!")
    else:
        print("Que pena! Você errou. O número era:", numeroAleatorio)