import textwrap

def exibir_menu():
    menu = """\n
            Selecione a opção desejada:
                [1]\t Depósito
                [2]\t Saque
                [3]\t Extrato
                [4]\t Cadastrar Usuário
                [5]\t Abrir Conta
                [6]\t Listar Contas
                [0]\t Sair
                ===> """
    return input(textwrap.dedent(menu))

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
          
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

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

    return saldo, extrato

def depositar(saldo, valor, extrato, /):
        if valor > 0:
           saldo += valor
           extrato += f"Depósito de R$ {valor:.2f} \n"
        else:
           print("A operação falhou! \n O valor Informado é inválido. \n Tente Novamente!!!")
        return saldo, extrato

def visualizar_extrato(saldo, /, *, extrato):
    print("\n#################### EXTRATO ####################")
    print("Não foram realizaas movimentações." if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")
    print("\n##################################################")

def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente Números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (Logradouro, n° - Bairro - Cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None   

def abrir_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta Criada com sucesso!!!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n Usuário não encontrado, não é possível abrir a conta!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\ 
            Agência:\t\t{conta["agencia"]}
            Conta Corrrente:\t\t{conta["numero_conta"]}
            Titular:\t\t{conta["usuario"]["nome"]}
        """

        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
    
        operacao = exibir_menu()
    
        if operacao == "1":
            valor = float(input("Digite o valor que contido no envelope de depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)     

        elif operacao == "2":
            valor = float(input("Digite o valor que você deseja sacar: "))

        elif operacao == "3":
            visualizar_extrato(saldo, extrato=extrato)

        elif operacao == "4":
            cadastrar_usuario(usuarios)

        elif operacao == "5":
            numero_conta = len(contas) + 1
            conta = abrir_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif operacao == "6":
            listar_contas(contas)

        elif operacao == "0":
            break

        else: 
            print("Opção inválida, selecione novamente a operação desejada!!!")

main()