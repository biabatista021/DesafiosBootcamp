def menu():
    menu = '''
        [1] Depósito
        [2] Saque
        [3] Extrato
        [4] Criar conta
        [5] Criar usuário 
        [6] Finalizar operação
    '''
    escolha = int(input("Insira o número da opção desejada: "))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f} \n"
    else:
        print("Digite um valor de depósito válido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, num_saque):
    if saldo < valor:
        print("Você não possui saldo o suficiente para retirar essa quantia.")

    elif num_saque > 3:
        print("Você já alcançou a quantidade de saques diários.")

    elif valor > 500:
        print("Você não pode sacar uma quantia maior que 500 reais.")

    elif valor > 0:
        saldo -= valor
        num_saque += 1
        extrato += f"Saque: R$ {valor:.2f} \n"

    else:
        print("Digite uma quantia válida.")
    
    return saldo, extrato

def mostrar_extrato(saldo, / ,*, extrato):
    print("\n\nEXTRATO ATUAL")
    print("Não foram feitas movimentações ainda." if not extrato else extrato)
    print(f"\nSaldo: R${saldo: .2f}")

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF: ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("Este CPF já está cadastrado!")
        return
    nome = input("Digite seu nome completo: ")
    endereco = input("Digite seu endereço (rua, num - bairro - cidade/estado): ")
    nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

    usuarios.append({"nome": nome, "nascimento": nascimento, "cpf": cpf, "endereco": endereco})

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] = cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, num_conta, usuarios):
    cpf = input("Informe seu CPF: ")
    usuario = filtrar_usuario(cpf,usuarios)
    if usuario:
        print("Conta criada!")
        return {"agencia": agencia, "num_conta": num_conta, "usuario": usuario }
    
    print("Usuário não encontrado!")

def main():
    A = "0001"
    saldo = 0
    num_saque = 0
    extrato = ""
    valor = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            valor = float(input("De quanto é seu depósito? "))
            
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 2:
            valor = float(input("De quanto é seu saque? "))

            saldo, extrato = sacar(saldo= saldo, valor= valor, extrato= extrato, num_saque= num_saque,)

        elif opcao == 3:
            mostrar_extrato(saldo, extrato= extrato)

        elif opcao == 4:
            num_conta = len(contas) + 1
            conta = criar_conta(A, num_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 5:
            criar_usuario(usuarios)

        elif opcao == 6:
            break
        else:
            print("Por favor, insira uma opção válida.")

main()