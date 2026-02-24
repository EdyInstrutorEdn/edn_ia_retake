try:
    idade = int(input("Digite a sua idade: "))
    classificação = ""
    if idade > 17:
        classificação = "maior de idade"
    elif idade > 14:
        classificação = "adolescente"
    elif idade > 9:
        classificação = "juvenil"
    else:
        classificação = "criança"
    print(f"Com {idade} anos, você é {classificação}.")
except ValueError as error:
    print(f"Por favor, insira apenas números. Erro: {error}")