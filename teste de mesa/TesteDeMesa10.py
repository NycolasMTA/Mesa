nota1 = float(input("A primeira nota sua foi: "))
nota2 = float(input("A segunda nota sua foi: "))
nota3 = float(input("A terceira nota sua foi: "))
list = [nota1, nota2, nota3]

media = nota1 + nota2 + nota3 / 3
baixaN = min(list)

print(f"Sua média é:{media} e sua menor nota foi:{baixaN} ")