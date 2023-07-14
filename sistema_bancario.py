def menu():
    menu = """

                    MENU 

        1 - Depositar
        2 - Sacar
        3 - Extrato
        4 - Criar nova conta
        5 - Listar contas
        6 - Criar novo usuário
        7 - Listar usuários
        0 - Sair

    """
    return menu

def depositar(saldo, deposito, extrato,/):
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
        print("\nOperação de depósito realizada com sucesso!")
    else:
        print("\nFalha na operação! O valor informado é inválido.")
    return saldo, extrato

def sacar(*,saque, saldo, extrato, numero_saques, LIMITE, LIMITE_SAQUES):

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
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n=============EXTRATO==============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo: .2f}")
    print("==================================")    

def novo_usuario(usuarios):
    cpf = int(input("Informe o CPF (somente números): "))
    usuario_atual = filtrar_usuarios(cpf, usuarios)

    if usuario_atual:
        print("\n   Usuário ja existente!   ")
        return
    else:
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        usuarios.append({"nome": nome.title(), "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco.title()})
        print("\n   Usuário criado com sucesso!   ")

def filtrar_usuarios(cpf, usuarios):
    usuario_filtrado = [usuario_atual for usuario_atual in usuarios if usuario_atual["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def listar_usuarios(usuarios):
    for usuario_atual in usuarios:
        print(f"""
              
            CPF:\t{usuario_atual['cpf']}
            Data Nacimento:\t{usuario_atual['data_nascimento']}
            Nome:\t{usuario_atual['nome']}
            Endereço:\t{usuario_atual['endereco']}

        """)

def criar_conta(AGENCIA, numero_conta, usuarios):
    cpf = int(input("Informe o CPF (somente números): "))
    usuario_atual = filtrar_usuarios(cpf, usuarios)

    if usuario_atual:
        print("\n    Conta criada com sucesso!    ")
        return {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario_atual}
    else:
        print("\n   Usuário não encontrado!   ")

def listar_contas(contas):
    for conta in contas:
        print(f"""
              
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}

        """)

def main():
    saldo = 0
    numero_saques = 0
    LIMITE_SAQUES = 3
    LIMITE = 500
    AGENCIA = '0001'
    extrato = ""
    usuarios =[]
    contas = []
    numero_conta = 1

    while True:

        print(menu())
        opcao = float(input("Informe a opção desejada: "))

        if opcao == 1:
            deposito = float(input("Digite o valor desejado para depósito: "))
            saldo, extrato = depositar(saldo, deposito, extrato)

        elif opcao == 2:
            saque = float(input("Digite valor desejado para o saque: "))
            saldo, extrato = sacar(saque=saque, saldo=saldo, extrato=extrato, numero_saques=numero_saques, LIMITE=LIMITE, LIMITE_SAQUES=LIMITE_SAQUES)

        elif opcao == 3:
           exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                numero_conta += 1
                contas.append(conta)
        
        elif opcao == 5:
            listar_contas(contas)

        elif opcao == 6:
            novo_usuario(usuarios)

        elif opcao == 7:
            listar_usuarios(usuarios)

        elif opcao == 0:
            break

        else:
            print("\nOpção inválida! Selecione novamente a operação desejada.")

main()