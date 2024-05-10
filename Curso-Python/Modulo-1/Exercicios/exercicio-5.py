valorA = float(input("Digite o primeiro valor \n"))
valorB = float(input("Digite o segundo valor \n"))

soma = valorA + valorB
sub = valorA - valorB

testeSoma = soma > 10
testeSub = sub < 0

print(f"A soma entre os números resulta em: {soma}")
print(f"A subtração entre os números resulta em: {sub}")
print(f"O resultado da soma é maior que 10? {testeSoma}")
print(f"O resultado da subtração é menor que 0? {testeSub}")