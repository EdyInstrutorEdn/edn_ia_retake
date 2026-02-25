linhas = ["Linha1\n","Linha2\n","Linha3\n","Linha4\n"]

with open("20260223/Agendalinhas.txt","w") as arquivo:
    arquivo.writelines(linhas)

with open("20260223/Agendalinhas.txt","r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha)