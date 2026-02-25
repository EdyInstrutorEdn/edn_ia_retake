def calcula_gorjeta(total, porcentagem):
    gorjeta = total * (porcentagem / 100)
    return gorjeta

valor_total = float(input("Digite o valor total da conta: R$"))
porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta que deseja: "))
valor_gorjeta = calcula_gorjeta(valor_total, porcentagem_gorjeta)
print(f"O Valor da gorjeta para uma conta de R${valor_total}")
print(f"com {porcentagem_gorjeta}%")
print(f"é de R${valor_gorjeta:.2f}")