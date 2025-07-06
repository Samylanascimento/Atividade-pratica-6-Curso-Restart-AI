def calculadora():

    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            operacao = input("Digite a operação (+, -, *, /): ")

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
               
                if num2 == 0:
                    raise ZeroDivisionError
                resultado = num1 / num2
            else:
                raise ValueError("Operação inválida.")

          
            print(f"\nO resultado de {num1} {operacao} {num2} é: {resultado}")
            break

        except ValueError as e:
     
            if "Operação inválida" in str(e):
                print("\nErro: Operação inválida. Por favor, use +, -, * ou /.")
            else:
                print("\nErro: Entrada inválida. Por favor, insira apenas números.")
            print("Vamos tentar novamente.\n")
        
        except ZeroDivisionError:
           
            print("\nErro: Não é possível dividir por zero.")
            print("Vamos tentar novamente.\n")
        
        except Exception as e:
          
            print(f"\nOcorreu um erro inesperado: {e}")
            print("Vamos tentar novamente.\n")



calculadora()
