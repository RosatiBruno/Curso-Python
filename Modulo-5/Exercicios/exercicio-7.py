informacoes = {}   #! Declaração do Dicionário vazio
informacoes["nome"] = input("Informe o nome do aluno: ")
nota1 = float(input("Digite a 1ª nota do aluno: "))
nota2 = float(input("Digite a 2ª nota do aluno: "))
nota3 = float(input("Digite a 3ª nota do aluno: "))

informacoes["media"] = (nota1 + nota2 + nota3) / 3

if informacoes["media"] >= 7 :
    informacoes["situacao"] = "Aprovado"

elif informacoes["media"] >= 5 :
    informacoes["situacao"] = "Em exame"

else :
    informacoes["situacao"] = "Reprovado"

print("-" * 30)
print(informacoes)
