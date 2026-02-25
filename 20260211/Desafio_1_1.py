idade = int(input("Digite sua idade: "))
classificacao = ""
if idade > 17:
    classificacao = "maior de idade"
elif idade > 14:
    classificacao = "adolescente"
elif idade > 9:
    classificacao = "juvenil"
else:
    classificacao = "criança"

print(f"Com {idade} anos, você é classificado como: {classificacao}.")