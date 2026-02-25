import soma
import divisao
import multiplicacao
import subtracao
import limpar_tela

while True:
    try:
        limpar_tela.clear_terminal()
        print("Calculadora Simples")
        print("1. Soma")
        print("2. Divisão")
        print("3. Multiplicação")
        print("4. Subtração")
        print("5. Sair")

        escolha = input("Escolha uma operação (1-5): ")

        if escolha == '5':
            print("Encerrando a calculadora.")
            break
        elif escolha in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                resultado = soma.Calcular(num1, num2)
                print("Resultado da soma:", resultado)
            elif escolha == '2':
                resultado = divisao.Calcular(num1, num2)
                print("Resultado da divisão:", resultado)
            elif escolha == '3':
                resultado = multiplicacao.Calcular(num1, num2)
                print("Resultado da multiplicação:", resultado)
            elif escolha == '4':
                resultado = subtracao.Calcular(num1, num2)
                print("Resultado da subtração:", resultado)
            print()  # Print a newline for better readability
            print("operação realizada com sucesso!")
        else:
            print("Opção inválida. Por favor, escolha uma operação válida.")
            
    except Exception as e:
        print("Erro:", str(e))
        
    input("Press the <ENTER> key to continue...")
