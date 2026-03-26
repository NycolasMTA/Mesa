hora = int(input("Digite as horas: "))
minuto = int(input("Digite os minitos: "))
segundos = int(input("Digite os segundos: "))

if 0 <= hora < 24 and 0 <= minuto < 60 and 0 <= segundos < 60:
    print("Hora válida!")
else:
    print("Hora inválida.")