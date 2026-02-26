def Maioridade(idade):
    if idade >= 65:
        return "Idoso"
    elif idade >= 18:
        return "Adulto"
    elif idade > 12:
        return "Adolescente"
    else:
        return "Infantil"