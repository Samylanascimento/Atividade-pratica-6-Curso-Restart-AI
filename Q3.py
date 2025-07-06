def verificar_senha_forte():
  
    print("Crie uma senha forte (ou digite 'sair' para encerrar).")
    print("Requisitos: no mínimo 8 caracteres e pelo menos 1 número.")
    
    while True:
        senha = input("\nDigite a senha: ")

        if senha.lower() == 'sair':
            print("Programa encerrado.")
            break


        if len(senha) < 8:
            print("Senha inválida: deve ter pelo menos 8 caracteres.")
            continue

       
        tem_numero = False
        for caractere in senha:
            if caractere.isdigit():
                tem_numero = True
                break
        
        if not tem_numero:
            print("Senha inválida: deve conter pelo menos um número.")
            continue

       
        print("Senha forte criada com sucesso!")
        break

# Inicia o verificador de senha
verificar_senha_forte()
