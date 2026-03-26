notas = int(input("Digite a nota: "))

if 9 <= notas <= 10:
    Nota = chr(65)
    print(Nota)
elif notas >=7:
    Nota = chr(66)
    print(Nota)
elif notas >=5:
    Nota = chr(67)
    print(Nota)
elif notas >=3:
    Nota = chr(68)
    print(Nota)
elif notas >= 0:
    Nota = chr(69)
    print(Nota)
else:
    print("Nota inválida.")