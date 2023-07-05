
menu = """
**************
d - Depositar
s - Sacar
e - Extrato
q - Sair
**************
"""

saldo = 0
limite = float(500)
extratosBancarios = {"Deposito": [], "Saques": [], "Geral": []}
nSaques = 0
LIMITE_SAQUES = 3

while True:
    opMenu = input(menu)

    if opMenu == "d":
        valorDeposito = float(input("Valor de deposito: R$ "))
        if valorDeposito > 0:
            saldo += valorDeposito
            extratosBancarios["Deposito"].append(f"Deposito: R$ {valorDeposito:.2f}")
            extratosBancarios["Geral"].append(f"Deposito: R$ {valorDeposito:.2f}")
        else:
            print("Depositar acima - R$ 0")

    elif opMenu.upper() == "s":
        if nSaques < LIMITE_SAQUES:

            valorSaque = float(input("Valor de saque: R$ "))
            if valorSaque > 0:
                if valorSaque <= limite and valorSaque <= saldo:
                    extratosBancarios["Saques"].append(f"Saque: R$ {valorSaque:.2f}")
                    extratosBancarios["Geral"].append(f"Saque: R$ {valorSaque:.2f}")
                    print("Saque com Sucesso!")
                    nSaques += 1
                else:
                    print(f"O limite de saque é de {limite:.2f}")
            else:
                print("Você deve informar um valor de saque válido!")
        else:
            print("Você não pode efetuar o saque, você escedeu o limite diário (3 saques)")

    elif opMenu.upper() == "e":
        for extratoGeral in extratosBancarios["Geral"]:
            print(f"Extrato Geral: R${extratoGeral}")
        for extratoSaque in extratosBancarios[" Saques"]:
            print(f"Extrato Saque: R${extratoSaque}")
        for extratoDeposito in extratosBancarios[" Deposito"]:
            print(f"Extrato Depsoito: R${extratoDeposito}")

    elif opMenu.upper() == "q":
        print("Até logo!")
        break

    else:
        print("Erro! Por favor digite uma outra opção.")

print("Até logo!")