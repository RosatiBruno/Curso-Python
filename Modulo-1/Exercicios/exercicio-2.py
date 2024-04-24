dia = int(input("Digite a quantidade de dias \n"))
hrs = int(input("Digite a quantidade de horas \n"))
minu = int(input("Digite a quantidade de minutos \n"))
seg = int(input("Digite a quantidade de segundos \n"))

total = seg + (minu * 60) + (hrs * 60 * 60) + (dia * 24 * 60 * 60)

print(f"{dia} dia(s), {hrs} hora(s), {minu} minuto(s), {seg} segund(s), resultam, no total, em {total} segundos")