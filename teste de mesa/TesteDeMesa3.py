Qproduto = int(input("Digite a quantos produtos quer: "))
Vunidade = float(input("Digite o valor de cada produto: "))
valorInicial = Qproduto * Vunidade

if Qproduto >100:
    desconto = 0.1
    descontoU = Vunidade * desconto

    valorF = Qproduto * (Vunidade - desconto)

    print(f"O valor inicial: {valorInicial} \n Quantidade solicitada foi: {Qproduto} \n O desconto por unidade {desconto} \n Valor final: {valorF}")
elif Qproduto <= 100:

    desconto = 0.05

    descontoU = Vunidade * desconto

    valorF = Qproduto * (Vunidade - desconto)

    print(f"O valor inicial: {valorInicial} \n Quantidade solicitada foi: {Qproduto} \n O desconto por unidade {desconto} \n Valor final: {valorF}")