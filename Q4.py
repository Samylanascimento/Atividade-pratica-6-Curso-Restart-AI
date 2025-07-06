def calcular_media_turma():
 
    notas = []
    print("Insira as notas da turma (0 a 10). Digite 'fim' para calcular a média.")
    while True:
        entrada = input("Digite a nota: ")

        if entrada.lower() == 'fim':
            break

        try:
            nota = float(entrada)

            if 0 <= nota <= 10:
                notas.append(nota)
                print(f"Nota {nota} adicionada.")
            else:
                print("Nota inválida. Por favor, insira um valor entre 0 e 10.")
        
        except ValueError:
            print("Entrada inválida. Por favor, digite um número ou 'fim'.")

    if notas:
        media = sum(notas) / len(notas)
        print("\n--- Resultado Final ---")
        print(f"Foram inseridas {len(notas)} notas válidas.")
        print(f"A média da turma é: {media:.2f}")
    else:
        print("\nNenhuma nota válida foi inserida. Não é possível calcular a média.")
    
    print("Programa encerrado.")

# Inicia a calculadora de média
calcular_media_turma()
