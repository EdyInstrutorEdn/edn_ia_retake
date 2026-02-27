def Escolaridade(idade):
    if idade >= 18:
        return "Ensino Superior"
    elif idade >= 15 and idade < 18:
        return "Ensino Médio"
    elif idade >= 10 and idade < 14:
        return "Ensino Fundamental II"
    elif idade >= 6 and idade < 10:
        return "Ensino Fundamental I"
    else:
        return "Educação Infantil"
