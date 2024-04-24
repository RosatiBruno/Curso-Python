anoNasc = int(input("Digite em qual ano você nasceu \n"))
anoAtual = int(input("Digite em que ano estamos \n"))

carteira = anoAtual - anoNasc

if (carteira >= 18) :
    print(f"Você pode tirar a certeira pois tem {carteira} anos de idade")
    