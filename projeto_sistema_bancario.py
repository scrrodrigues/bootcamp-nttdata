menu = """Selecione a opção desejada:
                [1] Depósito
                [2] Saque
                [3] Extrato
                [0] Sair
                ===> """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    
    operacao = input(menu)
    
    if operacao == "1":
        valor = float(input("Digite o valor que contido no envelope de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f} \n"
        else:
            print("A operação falhou! \n O valor Informado é inválido. \n Tente Novamente!!!")
        
    elif operacao == "2":
        valor = float(input("Digite o valor que você deseja sacar: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("A operação falhou! \n Você não tem saldo suficiente, verifique seu extrato e tente novamente.")
        elif excedeu_limite:
            print("A operação falhou! \n Você excedeu o limite diário de saque.")
        elif excedeu_saques:
            print("A operação falhou! \n O número de saques diário foi excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de R$ {valor:.2f} \n"
            numero_saques += 1
            print(f"Você sacou R$ {valor:.2f} \n")

        else:
            print("A operação falhou! \n O valor informado é inválido.")
                  
    elif operacao == "3":
            print("\n#################### EXTRATO ####################")
            print("Não foram realizaas movimentações." if not extrato else extrato)
            print(f"\n Saldo: R$ {saldo:.2f}")
            print("\n##################################################")
             
    elif operacao == "0":
        break

    else: 
        print("Opção inválida, selecione novamente a operação desejada!!!")
        