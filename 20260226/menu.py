import os
import maioridade
import escolaridade

def Opcao1():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("============================")
    print("Classificação por idade")
    print("============================")
    classification = int(input("Digite a sua idade: "))
    result = maioridade.Maioridade(classification)
    print("")
    print(f"Sua faixa etária é: {result}")
    print("")
    input("Pressione Enter para continuar...")

def Opcao2():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("============================")
    print("Classificação por escolaridade")
    print("============================")
    classification = int(input("Digite a sua idade: "))
    result = escolaridade.Escolaridade(classification)
    print("")
    print(f"Sua escolaridade ideal é: {result}")
    print("")
    input("Pressione Enter para continuar...")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("===== Menu Principal =====")
    print("1. Mairoridade")
    print("2. Escolaridade")
    print("0. Exit")
    print("==========================")
    choice = input("Escolha uma opção: ")
    

    try:
        choice = int(choice)
    except ValueError:
        print("Opção inválida. Por favor, tente novamente.")
        print("")
        input("Pressione Enter para continuar...")
        continue

    if choice == 1:
        Opcao1()
    elif choice == 2:
        Opcao2()
    elif choice == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Obrigado por usar o programa.")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
        print("")
        input("Pressione Enter para continuar...")        
