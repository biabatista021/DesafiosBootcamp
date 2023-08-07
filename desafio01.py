print('''
    [1] Depósito
    [2] Saque
    [3] Extrato  
    [4] Finalizar operação
''')

saldo = 0
num_saque = 0
extrato = ""
valor = 0

while True:
    opcao = int(input("Insira o número da opção desejada: "))

    if opcao == 1:
        valor = int(input("De quanto é seu depósito? "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f} \n"

        else:
            print("Digite um valor de depósito válido.")

    elif opcao == 2:
        valor = int(input("De quanto é seu saque? "))

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

    elif opcao == 3:
        print("\n\nEXTRATO ATUAL")
        print("Não foram feitas movimentações ainda." if not extrato else extrato)
        print(f"\nSaldo: R${saldo: .2f}")

    elif opcao == 4:
         break
    else:
         print("Por favor, insira uma opção válida.")