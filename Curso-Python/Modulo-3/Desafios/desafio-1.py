horaInicial = int(input('Deseja iniciar em qual hora? '))
horaFinal = int(input('Deseja terminar em qual hora? '))
while ((horaInicial > horaFinal) or (horaInicial < 0) or (horaInicial > 23) or (horaFinal < 0) or (horaFinal > 23)):
  horaInicial = int(input('Deseja iniciar em qual hora? '))
  horaFinal = int(input('Deseja terminar em qual hora? '))
for h in range(horaInicial, horaFinal + 1, 1):
  for m in range(0, 60, 1):
    for s in range(0, 60, 1):
      print(h ,':', m ,':', s, 'h')
