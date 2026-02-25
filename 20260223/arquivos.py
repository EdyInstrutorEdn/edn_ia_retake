with open('20260223/agenda2.txt','w') as arquivo:
    arquivo.write("juliana\n")
    arquivo.write("Allyson\n")
    arquivo.write("Thais\n")
    arquivo.write("Terence\n")
    arquivo.close()
    
with open('20260223/agenda2.txt','r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha)
