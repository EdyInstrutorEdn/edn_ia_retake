import os
import maioridade
import media

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
    
def Opcao3():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=========================")
    print("Cálculo da média")
    print("=========================")
    resultado = media.calcularmedia()
    print(f'A média final é {resultado:.2f}')
    print("")
    input("Pressione Enter para continuar...")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("===== Menu Principal =====")
    print("1. Mairoridade")
    print("3. Média")
    print("0. Exit")
    print("==========================")
    choice = input("Enter your choice: ")
    

    try:
        choice = int(choice)
    except ValueError:
        print("Opção inválida. Por favor, tente novamente.")
        print("")
        input("Pressione Enter para continuar...")
        continue

    if choice == 1:
        Opcao1()
    if choice == 3:
        Opcao3()
    elif choice == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Obrigado por usar o programa.")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
        print("")
        input("Pressione Enter para continuar...")
        
