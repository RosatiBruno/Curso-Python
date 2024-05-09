from datetime import timedelta

dias = int(input("Digite uma quantidade de dias: "))
horas = int(input("Digite uma quantidade de horas: "))
minutos = int(input("Digite uma quantidade de minutos: "))
segundos = int(input("Digite uma quantidade de segundos: "))

#! Pega a função timedelta, e dentro dela indica que a variavel 'minutos' esta em minutos e converte isso para o total em segundos. Depois,
#! faz a mesma coisa com as horas e com os dias.

totalEmSegundos = segundos + timedelta(minutes=minutos).total_seconds() + timedelta(hours=horas).total_seconds() + timedelta(days=dias).total_seconds()

print(f"Esse tempo convertido para segundos resulta em: {totalEmSegundos}")