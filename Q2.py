def contar_par_impar():
 
    cont_pares = 0
    cont_impares = 0

    print("Digite números inteiros (ou 'fim' para sair):")

    while True:
        entrada = input("> ")

        if entrada.lower() == 'fim':
            break

        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"{numero} é PAR.")
                cont_pares += 1
            else:
                print(f"{numero} é ÍMPAR.")
                cont_impares += 1
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira um número inteiro ou 'fim'.")

    print("\n--- Relatório Final ---")
    print(f"Quantidade de números pares inseridos: {cont_pares}")
    print(f"Quantidade de números ímpares inseridos: {cont_impares}")
    print("Programa encerrado.")

# Inicia o contador
contar_par_impar()
