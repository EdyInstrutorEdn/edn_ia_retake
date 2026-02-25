import Calculadora.limpar_tela as limpar_tela
import Calculadora.soma as soma
import Calculadora.subtracao as subtracao
import Calculadora.multiplicacao as multiplicacao
import Calculadora.divisao as divisao

while True:
    try:
        limpar_tela.clear_terminal()
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))
 
        if operacao == '+':
            resultado = soma.Calcular(num1, num2)
            print(f"Resultado: {num1} + {num2} = {resultado}")
        elif operacao == '-':
            resultado = subtracao.Calcular(num1, num2)
            print(f"Resultado: {num1} - {num2} = {resultado}")
        elif operacao == '*':
            resultado = multiplicacao.Calcular(num1, num2)
            print(f"Resultado: {num1} * {num2} = {resultado}")
        elif operacao == '/':
            resultado = divisao.Calcular(num1, num2)
            print(f"Resultado: {num1} / {num2} = {resultado}")
        else:
            print("Operação inválida. Por favor, escolha uma operação válida.")
        
    
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
    except Exception as e:
        print("Erro:", str(e))
        
    input("Press the <ENTER> key to continue...")