idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Seu voto é Obrigatório")
elif idade >= 16:
    print("Seu voto é Facultativo")
else:
    print("Você não é eleitor.")