idade = int(input("Digite sua idade: "))
classificacao = ""
if idade < 10:
    classificacao = "criança"
elif idade < 15:
    classificacao = "juvenil"
elif idade < 18:
    classificacao = "adolescente"
else:
    classificacao = "adulto"

print(f"Com {idade} anos, você é classificado como: {classificacao}.")