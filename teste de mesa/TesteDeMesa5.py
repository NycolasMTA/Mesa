idade1 = int(input("Digite a primeira idade: "))
idade2 = int(input("Digite a segunda idade: "))
idade3 = int(input("Digite a terceira idade: "))
lista = [idade1, idade2, idade3]

maior = max(lista)
menor = min(lista)

print(f"A mais velho entre vocês é: {maior} e o menor: {menor}")