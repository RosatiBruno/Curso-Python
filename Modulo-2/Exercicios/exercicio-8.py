nmr1 = float(input("Digite o primeiro número: \n"))
nmr2 = float(input("Digite o segundo número: \n"))

print("+ : Soma")
print("- : Subtração")
print("* : Multiplicação")
print("/ : Divisão")

resp = input("Digite a opção desejada:")

while (resp != "+") and (resp != "-") and (resp != "*") and (resp != "/") :
    print(f"A opção {resp} não existe! Digite novamente!")
    resp = input("Digite a opção desejada:")

if (resp == "+") :
    respConta = nmr1 + nmr2

elif (resp == "-") :
    respConta = nmr1 - nmr2

elif (resp == "*") :
    respConta = nmr1 * nmr2

else :
    respConta = nmr1 / nmr2

print(f"O resultado da operação {nmr1} {resp} {nmr2} resulta em {respConta}")
