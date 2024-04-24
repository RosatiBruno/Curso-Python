qtdCigarrosPorDia = int(input("Informe a quantidade de cigarros fumados por dia \n"))
qtdAnosFumando = int(input("Informe a quantos anos você fuma \n"))

tempoPerdido = qtdCigarrosPorDia * 365
qtdCigarrosTotal = qtdCigarrosPorDia * 365 * qtdAnosFumando
diasPerdidos = (qtdCigarrosTotal * 10) / 60 / 24

print(f"Você fuma à {tempoPerdido} dias")
print(f"O que da o equivalente a {qtdCigarrosTotal} cigarros")
print(f"Você perdeu o equivalente a {diasPerdidos} de vida")
