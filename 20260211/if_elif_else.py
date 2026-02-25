idade = int(input("Digite sua idade: "))
classificacao = ""
if idade > 18:
    print("Você é maior de idade.")
elif idade > 14:
    print("Você é adolescente.")
else:
    print("Você é criança.")