saldo = 0
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE = 500
extrato = ""

menu = """

                MENU 

    1 - Depositar
    2 - Sacar
    3 - Extrato
    0 - Sair

    
"""

while True:

    print(menu)
    opcao = float(input("Informe a opção desejada: "))

    if opcao == 1:
        deposito = float(input("Digite o valor desejado para depósito: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print("\nOperação de depósito realizada com sucesso!")
        else:
            print("\nFalha na operação! O valor informado é inválido.")

    elif opcao == 2:
        saque = float(input("Digite valor desejado para o saque: "))

        excedeu_saldo = saque > saldo
        excedeu_limite = saque > LIMITE
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\nFalha na operação! Saldo insuficiente.")
        elif excedeu_limite:
            print("\nFalha na operação! Valor de saque superior ao limite.")
        elif excedeu_saques:
            print("\nFalha na operação! Número máximo de saques excedidos.")
        elif saque > 0 :
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1
            print("\nOperação de saque sucedida! Retire seu dinheiro!")
        else:
            print("\nFalha na operação! Valor inserido é inválido.")


    elif opcao == 3:
        print("\n=============EXTRATO==============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("==================================")    

    elif opcao == 0:
        break

    else:
        print("\nOpção inválida! Selecione novamente a operação desejada.")
