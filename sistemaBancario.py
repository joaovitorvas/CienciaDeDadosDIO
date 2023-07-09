menu = """

[D] - Depositar
[S] - Sacar
[E] - Extrato
[Q] - Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
extratos = []

def extrato():
    return

def deposito(): 
    return

while True:

    opcao = input(menu).upper()

    if opcao == 'D':
        valor = float(input(f"Digite o valor do depósito: R$ "))
        while valor < 0.01:
            print('Operação invalida, tente novamente')
            valor = float(input(f"Digite o valor do depósito: R$ "))
        saldo += valor
        extrato = f'Deposito feito no valor de R$ {valor:.2f}'
        extratos.append(extrato)

    if opcao == 'S':
        if numero_saques < LIMITE_SAQUES:
            valor = float(input(f"Digite o valor do saque: R$ "))
            while valor < 0.01:
                print('Operação invalida, tente novamente')
                valor = float(input(f"Digite o valor do saque: R$ "))
            if valor <= 500 and valor <= saldo:
                saldo -= valor
                extrato = f'Saque feito no valor de R$ {valor:.2f}'
                extratos.append(extrato)
                numero_saques += 1
            elif valor > saldo:
                print('Saldo insuficiente')
            else:
                print('O limite do valor de saque foi excedido!')
        else:
            print('Limite de saques excedidos!')
    if opcao == 'E':
        print(f"Saldo igual a: R$ {saldo:.2f}")
        for i in extratos:
            print(i)
    if opcao == 'Q':
        break
