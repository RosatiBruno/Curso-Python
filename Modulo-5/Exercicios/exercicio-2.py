def maiorNumero(stringTela, *numerosEmpacotados):
    maiorNmrEmp = 0

    for cont in numerosEmpacotados :
        if cont > maiorNmrEmp :
            maiorNmrEmp = cont
            
    print(f"A mensagem digitada era: '{stringTela}' e o maior número era {maiorNmrEmp}")

stringTela = input("Digite uma mensagem: ")
numerosEmpacotados = []
while True :
    numero = input("Digite no mínimo um número inteiro aleatório (Ou deixe em branco para prosseguir): ")
    if (numero == "") :
        break
    try :
        numerosEmpacotados.append(int(numero))
    except ValueError:
        print("Digite apenas números inteiros!")

maiorNumero(stringTela, *numerosEmpacotados)
