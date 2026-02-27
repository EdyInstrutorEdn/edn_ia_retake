import os
import maioridade
import escolaridade
import media


def Opcao1():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("============================")
    print("Classificação por idade")
    print("============================")

    try:
        classification = int(input("Digite a sua idade: "))

        if classification < 0:
            print("Idade não pode ser negativa.")
        else:
            result = maioridade.Maioridade(classification)
            print("")
            print(f"Sua faixa etária é: {result}")

    except ValueError:
        print("Por favor, digite apenas números válidos.")

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


def Opcao4():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("============================")
    print("Classificação por experiência")
    print("============================")

    try:
        anos = int(input("Digite seus anos de experiência: "))

        if anos < 0:
            print("O tempo de experiência não pode ser negativo.")
        else:
            niveis = {
                range(0, 2): "Júnior",
                range(2, 5): "Pleno",
                range(5, 100): "Sênior"
            }

            resultado = "Nível não definido"

            for faixa, nivel in niveis.items():
                if anos in faixa:
                    resultado = nivel
                    break

            print("")
            print(f"Seu nível de experiência é: {resultado}")

    except ValueError:
        print("Por favor, digite apenas números válidos.")

    print("")
    input("Pressione Enter para continuar...")


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("===== Menu Principal =====")
    print("1. Mairoridade")
    print("2. Escolaridade")
    print("3. Média")
    print("4. Nível de Experiência")

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
        continue
    elif choice == 4:
        Opcao4()
        continue
    elif choice == 2:
        Opcao2()
        continue
    if choice == 3:
        Opcao3()
        continue
    elif choice == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Obrigado por usar o programa.")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
        print("")
        input("Pressione Enter para continuar...")
