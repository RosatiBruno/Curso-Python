def organizar(nmr1, nmr2, nmr3) :
    if (nmr1 > nmr2 > nmr3) :
        print(f"{nmr1} {nmr2} {nmr3}")
    elif (nmr1 > nmr3 > nmr2) :
        print(f"{nmr1} {nmr3} {nmr2}")
    elif (nmr2 > nmr1 > nmr3) :
        print(f"{nmr2} {nmr1} {nmr3}")
    elif (nmr2 > nmr3 > nmr1) :
        print(f"{nmr2} {nmr3} {nmr1}")
    elif (nmr3 > nmr1 > nmr2) :
        print(f"{nmr3} {nmr1} {nmr2}")
    elif (nmr3 > nmr2 > nmr1) :
        print(f"{nmr3} {nmr2} {nmr1}")


nmr1 = input("Digite um número: ")
nmr2 = input("Digite outro número: ")
nmr3 = input("Digite outro número: ")
organizar(nmr1, nmr2, nmr3)
